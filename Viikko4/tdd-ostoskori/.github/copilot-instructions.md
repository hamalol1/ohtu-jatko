# Copilot instructions for tdd-ostoskori

This is a small Python 3.14 TDD exercise. Work from this project directory, not from the repository parent, unless a task explicitly spans multiple coursework projects.

## Build, test, and validation

- Install or refresh dependencies: `uv sync`
- Run the full test suite: `uv run pytest`
- Run one test file: `uv run pytest src/tests/ostoskori_test.py`
- Run one test method:
  `uv run pytest src/tests/ostoskori_test.py::TestOstoskori::test_ostoskorin_hinta_ja_tavaroiden_maara_alussa`
- Select tests by name with `uv run pytest -k "<name fragment>"`
- This project has no configured lint or type-check command.

The pytest configuration comes from `pyproject.toml`; pytest is the only development dependency. Keep `uv.lock` consistent with dependency changes made through `uv`.

## High-level architecture

- `src/tuote.py` defines `Tuote`, the product value used by the cart domain. It exposes `nimi()` and `hinta()` and stores mutable sale data fields that may be part of an exercise extension.
- `src/ostos.py` defines `Ostos`, which aggregates one `Tuote` with a quantity.
- `src/ostoskori.py` defines `Ostoskori`, the cart facade. It currently contains the exercise API but leaves its methods implemented as `pass` or returning a stub value.
- `src/index.py` is a placeholder and contains no running application entry point.
- `src/tests/ostoskori_test.py` is the pytest/unittest test module for cart behavior.

The intended relationships are `Ostoskori` -> `Ostos` -> `Tuote`: `Ostoskori` should use `Ostos` objects to represent products already in the cart and preserve quantities instead of duplicating cart-line behavior.

## Project conventions

- Module and public API names are in Finnish: `Ostoskori`, `Tuote`, `Ostos`, `tavaroita_korissa`, `lisaa_tuote`, and similar names should be retained.
- Source modules in `src/` import each other by bare module name, for example `from tuote import Tuote`; retain this pattern when running directly from the project environment.
- Tests use `unittest.TestCase` classes and `assertEqual` assertions, even though pytest discovers and runs them.
- A cart quantity is owned by `Ostos`; `muuta_lukumaaraa()` changes it and clamps it at zero. The cart API is responsible for deciding whether to add another line or update an existing line.
- `Ostoskori` is an unfinished TDD exercise: methods with `pass` or fixed placeholder results are not to be treated as completed behavior. Implement their behavior together with focused tests.
- Add tests to `src/tests/ostoskori_test.py` as methods on `TestOstoskori`, and keep the cart instance created in `setUp` as the test fixture.


- Tests executed with `uv run pytest`
- Code of `ostos.py` and `tuote.py` should not be changed
- Tests should not be edited unless explicitly asked
- Always implement absolutely minimal code that makes the tests pass
