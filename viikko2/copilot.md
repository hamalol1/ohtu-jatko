## Kuinka hyödyllisiksi koit koodin täydennyksen ehdotukset?
Yleisesti ottaen Copilot on erinomainen työkalu, joka parantaa työn tehokkuutta huomattavasti. Pelkkä ghost text ei tuntunut kovinkaan hyödylliseltä tai ihmeelliseltä. Se voi nopeuttaa pienten rutiinirivien kirjoittamista, mutta ei muuta koodaamista kovin merkittävästi.

## Pitikö Copilotin selitys Pylint-varoituksesta paikkansa?
Kyllä piti. Copilot kertoi mistä oli kyse, miksi ja miten korjata.

## Tekikö agentti toimivan ratkaisun, ja testit?
Agent-mode on todella tehokas ja hyödyllinen oikein käytettynä. Teki uudet metodit ja testit, jotka toimivat heti.

## Eroaako testeissä joku siitä miten testejä tehtiin edellisellä viikolla?
Erosi merkittävästi riippuvuuksien hallinnan osalta. Koska PlayerStats-luokka käyttää verkkoyhteyden tekevää PlayerReader-luokkaa, agentti ei käyttänyt testeissä oikeaa lukijaa. Se loi Stub-luokan, jolle injektoitiin testitiedostossa kovakoodattu, keksitty lista pelaajia. Viime viikolla emme joutuneet eristämään ulkoisia rajapintoja tällä tavalla. Stubin ansiosta testit ovat nopeita, eivätkä ne kaadu vaikka verkkoyhteys katkeaisi, jolloin ne testaavat aidosti vain PlayerStats-luokan omaa järjestelylogiikkaa.

## Löysikö Pylint agentin koodista virheitä?
Kyllä löysi. Vaikka koodi toimi täydellisesti, agentti ei noudattanut kaikkia tyylisääntöjä. Se jätti esimerkiksi docstringit puuttumaan ja kirjasi pysyvän muuttujan pienellä alkukirjaimella (url vs URL).

## Mitä muuta opit?
Opin, että tekoäly on tehokas apukehittäjä, jolle voi delegoida isompia loogisia kokonaisuuksia tai jolta voi pyytää selityksiä vaikeisiin virheilmoituksiin.
