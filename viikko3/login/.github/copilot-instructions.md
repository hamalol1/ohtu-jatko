# Copilot instructions for viikko3/login

This project is the Flask login/register application in this folder. Keep edits scoped to this subproject unless the task explicitly says otherwise.

## Build, test, and validation

All commands in this project are run with the `uv` prefix from `viikko3/login`.

- Install or refresh dependencies: `uv sync`
- Start the app locally: `uv run python src/index.py`
- Run a single login suite: `uv run robot src/tests/login.robot`
- Run a single register suite: `uv run robot src/tests/register.robot`
- Run the full browser suite: `uv run robot src/tests`

The app listens on `http://localhost:5001` and the Robot tests expect it to be running before execution. There is no separate lint or type-check command configured in `pyproject.toml`; the effective validation here is the Robot browser test suite.

## High-level architecture

- `src/index.py` is the entry point and starts Flask on port `5001`.
- `src/app.py` contains the HTTP routes and redirect logic for `/`, `/login`, `/register`, `/welcome`, `/ohtu`, `/ping`, and `/tests/reset`.
- `src/services/user_service.py` owns validation and authentication rules. Route handlers should delegate to `UserService` instead of doing their own validation.
- `src/repositories/user_repository.py` is the in-memory persistence layer. It stores `User` objects in a list and exposes `find_by_username`, `create`, and `delete_all` for test reset behavior.
- `src/entities/user.py` defines the `User` model.
- `src/tests/` contains Robot Framework acceptance tests. `src/AppLibrary.py` is the HTTP helper library used by the test suite to create users and reset the app state.
- Template output lives in `src/templates/` and should be checked whenever a flow or validation message changes.

## Project conventions specific to this codebase

- Keep the route layer thin: `src/app.py` should read request data and call the service layer; it should not contain business rules.
- Validation rules currently live in `UserService.validate()` and are the authoritative rules for this app:
  - username is required
  - password is required
  - username must be at least 3 characters long
  - password must be at least 8 characters long
  - username must be unique
- Errors are raised as `UserInputError` or `AuthenticationError` in `user_service.py`; route handlers catch them and display the message via `flash(...)`.
- The application uses in-memory state only. Do not introduce a database or another persistence mechanism unless the task explicitly calls for it.
- Browser tests rely on `Reset Application` to clear the repository before scenarios. If a change affects login/register behavior, check the matching Robot files together: `src/tests/login.robot` and `src/tests/register.robot`.
- The test reset endpoint is intentionally exposed at `/tests/reset` for acceptance testing and should remain compatible with the existing Robot workflow.

## Working style in this repo

- Prefer small, focused edits that keep the Flask MVC-style separation intact: route handlers, service logic, and repository logic each stay in their own layer.
- When changing validation or UI text, update the corresponding Robot tests so the acceptance suite reflects the intended behavior.
- Keep changes local to this app folder; do not introduce cross-project dependencies or restructure unrelated assignments in the repository.
