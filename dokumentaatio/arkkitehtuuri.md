# Arkkitehtuurikuvaus

## Rakenne

Koodi on jaettu kolmeen pakkausen: `ui`, `services` ja `repositories`. Pakkaus `ui` sisältää käyttöliittymän, `services` sovelluslogiikan ja `repositories` tietokantakäsittelyn.

![Pakkausrakenne](./kuvat/pakkauskaavio.png)

## Käyttöliittymä

Sovelluksessa on 3 näkymää `login_view`, `register_view`, `main_view.` Nämä näkymät perivät `base_view` luokan, jossa on jaettua toiminnallisuutta ja metodeja näyttää info ja error dialogeja.

`login_view` on kirjautusmis sivu, joka avautuu ensimmäisenä sovelluksen käynistyksessä.

`register_view` on rekisteröitymissivu, jossa käyttäjä voi luoda uuden käyttäjän.

`main_view` on pääsivu, jossa käyttäjä voi tarkastella tallennettuja tilejä ja tallentaan uusia.

`ui` moduuli toimii kaikkien näkymien ylänäkymänä ja vastaa navigoinnista näkymien välillä. 

# Päätoiminnallisuudet

## Käyttäjän Rekisteröityminen
```mermaid
sequenceDiagram
    User->>UI: click "Rekisteröidy"
    UI->>UI: navigate("register")
    User->>UI: enter "username"
    User->>UI: enter "password"
    User->>UI: click "Rekisteröidy"
    UI->>UI: self.validateInputs()
    UI->>user_service: user_service.create_user("username", "password")
    user_service->>utils: utils.hash_password("password")
    utils->>user_service: "hashed_password"
    user_service->>user_repository: user_repository.create_user("username", "hashed_password")
    UI->>UI:show_info("Rekisteröityminen onnistui")
    UI->>UI: navigate("login")
```
