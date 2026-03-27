# Flask Bloggapplikasjon

## Prosjektbeskrivelse

Dette prosjektet er en enkel blogg-applikasjon utviklet med Python, Flask og SQLite.
Formålet med prosjektet er å demonstrere grunnleggende backend-utvikling, inkludert bruk av databaser, routing i Flask, template rendering med Jinja2 og håndtering av brukerinput.

Applikasjonen lar brukere opprette, vise og redigere bloggposter. Det er også mulig å legge til kommentarer på innlegg, samt filtrere innlegg basert på tags.

Prosjektet er utviklet som en del av prosjekt-eksamen i PRO1002 og viser hvordan sentrale konsepter som CRUD-operasjoner, databasehåndtering og strukturert kode kan brukes i en webapplikasjon.

---

## Funksjonalitet

Applikasjonen inneholder følgende funksjoner:

* Opprette nye bloggposter
* Se en liste over alle bloggposter
* Åpne og lese en enkelt bloggpost
* Redigere eksisterende bloggposter
* Legge til kommentarer på bloggposter
* Filtrere bloggposter etter tags
* Flash-meldinger for å gi tilbakemelding til brukeren
* Enkel validering av brukerinput
* SQLite-database for lagring av data
* Jinja2 templates med template inheritance

---

## Teknologier brukt

Prosjektet er utviklet med følgende teknologier:

* Python
* Flask
* SQLite
* Jinja2
* HTML og CSS
* Pytest for testing
* Git og GitHub for versjonskontroll

---

## Prosjektstruktur

Prosjektet er strukturert på følgende måte:

```id="q0p9km"
flask-blog-project
│
├── app.py
├── db.py
├── init_db.py
├── requirements.txt
├── README.md
│
├── database
│   └── blog.db
│
├── templates
│   ├── base.html
│   ├── home.html
│   ├── post.html
│   ├── create_post.html
│   ├── edit_post.html
│   └── tag.html
│
├── static
│   └── style.css
│
└── tests
    ├── test_app.py
    └── test_db.py
```

Strukturen skiller mellom applikasjonslogikk, databasekode, templates og statiske filer. Dette gjør prosjektet mer oversiktlig og lettere å vedlikeholde.

---

## Oppsett og installasjon

Følg disse stegene for å kjøre prosjektet lokalt.

### 1. Klon repository

```id="puhjv0"
git clone <repository-url>
cd flask-blog-project
```

### 2. Installer avhengigheter

```id="epg1ns"
python3 -m pip install -r requirements.txt
```

### 3. Opprett databasen

```id="jyt12t"
python3 init_db.py
```

Dette vil opprette SQLite-databasen og nødvendige tabeller.

### 4. Start applikasjonen

```id="b4naw9"
python3 app.py
```

Åpne deretter nettleseren og gå til:

```id="5yo14l"
http://127.0.0.1:5000
```

---

## Kjøre tester

Testene er skrevet ved hjelp av pytest.

For å kjøre testene:

```id="g01gs5"
python3 -m pytest
```

Testene sjekker blant annet at applikasjonen fungerer og at databaseoperasjoner returnerer forventede resultater.

---

## Sikkerhetshensyn

Noen grunnleggende sikkerhetstiltak er implementert i applikasjonen:

* Parameteriserte SQL-spørringer for å redusere risiko for SQL-injection
* Enkel validering av brukerinput i skjemaer
* Automatisk HTML-escaping gjennom Jinja templates for å redusere risiko for XSS

Dette er en enkel applikasjon, men tiltakene viser bevissthet rundt vanlige sikkerhetsutfordringer i webapplikasjoner.

---

## Begrensninger

Prosjektet er en forenklet bloggplattform og har noen begrensninger:

* Ingen autentisering eller brukerkontoer
* Det er foreløpig ikke mulig å slette innlegg eller kommentarer
* Begrenset testdekning
* Enkelt brukergrensesnitt

---

## Mulige forbedringer

Hvis prosjektet skulle videreutvikles, kunne følgende forbedringer implementeres:

* Brukerinnlogging og autentisering
* Mulighet for å slette bloggposter og kommentarer
* Bedre feilhåndtering og egne feilsider (for eksempel 404)
* Flere automatiserte tester
* Bedre responsivt design for mobil

---

## Forfatter

Studentprosjekt utviklet som en del av et kurs i backend-utvikling med Flask og SQLite.
