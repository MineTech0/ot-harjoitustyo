>Tässä repossa Helsingin yliopiston *Ohjelmistotekniikka* kurssin palautukset ja harjoitustyö PassSafe.
# PassSafe

Sovelluksen tarkoitus on toimia salasananhallintaohjelmana, joka mahdollistaa käyttäjien salasanojen tallentamisen ja hallinnan turvallisesti ja luotettavasti. Käyttäjät voivat tallentaa eri palveluiden käyttäjätunnuksia ja salasanoja sovellukseen, joka salaustekniikkaa käyttäen pitää ne turvassa.


## Dokumentaatio

[Vaatimusmäärittely](https://github.com/MineTech0/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

[Tuntikirjanpito](https://github.com/MineTech0/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)

[Changelog](https://github.com/MineTech0/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md)

## Asennus

1. Asenna riippuvuudet komennolla:

```bash
poetry install
```
2. Alusta tietokanta komennolla:

```bash
poetry run invoke init-db
```

3. Käynnistä sovellus komennolla:

```bash
poetry run invoke start
```

## Komentorivitoiminnot

### Ohjelman suorittaminen

Ohjelman pystyy suorittamaan komennolla:

```bash
poetry run invoke start
```

### Testaus

Testit suoritetaan komennolla:

```bash
poetry run invoke test
```

### Testikattavuus

Testikattavuusraportin voi generoida komennolla:

```bash
poetry run invoke coverage-report
```

Raportti generoituu _htmlcov_-hakemistoon.

### Pylint

```bash
poetry run invoke lint
```

### Formatointi

```bash
poetry run invoke format
```