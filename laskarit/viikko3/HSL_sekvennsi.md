```mermaid
sequenceDiagram
    participant main
    participant Laitehallinto
    participant Rautatietori
    participant Ratikka6
    participant Bussi244
    participant lippu_luukku
    participant kallen_kortti

    main ->> Laitehallinto: HKLLaitehallinto()
    main ->> Rautatietori: Lataajalaite()
    main ->> Ratikka6: Lukijalaite()
    main ->> Bussi244: Lukijalaite()
    main ->> Laitehallinto: lisaa_lataaja(Rautatietori)
    main ->> Laitehallinto: lisaa_lukija(Ratikka6)
    main ->> Laitehallinto: lisaa_lukija(Bussi244)
    main ->> lippu_luukku: Kioski()
    main ->> lippu_luukku: osta_matkakortti("Kalle")
    lippu_luukku ->> kallen_kortti: Matkakortti("Kalle")
    lippu_luukku -->> main: kallen_kortti
    main ->> Rautatietori: lataa_arvoa(kallen_kortti, 3)
    Rautatietori ->> kallen_kortti: kasvata_arvoa(3)
    main ->> Ratikka6: osta_lippu(kallen_kortti, 0)
    Ratikka6 ->> kallen_kortti: vahenna_arvoa(1.5)
    Bussi244 -->> main: True
    main ->> Bussi244: osta_lippu(kallen_kortti, 2)
    Bussi244 -->> main: False