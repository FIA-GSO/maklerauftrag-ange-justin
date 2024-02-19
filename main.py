# Maklerauftrag Programm Makler Algorithmus

raeume = []

def anfang():
    print("### Willkommen zum Maklerprogramm ###")
    antwort = input("Möchten Sie einen Raum hinzufügen? (ja/nein): ")

    while antwort.lower() == "ja":
        hinzufuegen_raum()
        antwort = input("Möchten Sie einen weiteren Raum hinzufügen? (ja/nein): ")

    zusammenfassung_raeume()


def hinzufuegen_raum():
    raum_name = input("Geben Sie den Namen des Raums ein: ")
    raum_groesse = int(input("Geben Sie die Größe des Raums in Quadratmetern ein: "))
    raum = {"Name": raum_name, "Größe": raum_groesse}
    raeume.append(raum)
    print("Raum erfolgreich hinzugefügt!\n")


def zusammenfassung_raeume():
    print("\nZusammenfassung der Räume:")
    for raum in raeume:
        print(f"Raum: {raum['Name']} - Größe: {raum['Größe']} Quadratmeter")

    gesamtgroesse = sum(raum["Größe"] for raum in raeume)
    print(f"\nGesamtgröße aller Räume: {gesamtgroesse} Quadratmeter")

anfang()
