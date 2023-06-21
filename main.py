def notenrechner():
    notenliste = []
    gesamt_summe = 0

    while True:
        try:
            max_punkte = float(input("Gib die maximal erreichbaren Punkte ein: "))
            punkte = float(input("Gib die erreichten Punkte ein: "))
        except ValueError:
            print("Ungültige Eingabe. Bitte gib eine Zahl ein.")
            continue

        prozent = (punkte / max_punkte) * 100
        note = round(prozent / 10) / 2

        print("Erreichte Prozent: ", prozent)
        print("Note: ", note)

        if note >= 4.5:
            print("Sehr gut!")
        elif note >= 3.5:
            print("Gut!")
        elif note >= 2.5:
            print("Befriedigend!")
        elif note >= 1.5:
            print("Ausreichend!")
        else:
            print("Nicht bestanden!")

        while True:
            antwort = input("Möchtest du diese Note zur Notenliste hinzufügen? (ja/nein): ")
            if antwort.lower() == "ja":
                notenliste.append(note)
                gesamt_summe += note
                break
            elif antwort.lower() == "nein":
                break
            else:
                print("Ungültige Eingabe. Bitte antworte mit 'ja' oder 'nein'.")

        if antwort.lower() == "nein":
            if len(notenliste) == 0:
                print("Es wurden noch keine Noten zur Notenliste hinzugefügt.")
                continue
            else:
                break

    durchschnitt = gesamt_summe / len(notenliste) if len(notenliste) > 0 else 0

    if len(notenliste) > 0:
        print("Notenliste: ", notenliste)
        print("Durchschnitt mit den eingegebenen Noten: ", durchschnitt)
    else:
        print("Es wurden keine Noten zur Notenliste hinzugefügt.")

notenrechner()