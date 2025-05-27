from scripts.transform import bereinige_rohdaten

eingabe = "data/Rohdaten/Rohdatei_Einwohner.xlsx"
ausgabe = "data/Verarbeitet/Struktur_Bereinigt.xlsx"

# Bereinigen und speichern
daten_bereinigt = bereinige_rohdaten(eingabe, ausgabe)

