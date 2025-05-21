import pandas as pd
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows

# === Dateipfade ===
eingabe_datei = r"C:\Users\Igor\Desktop\github\Bevölkerung\Rohdaten\Struktur.xlsx"
ausgabe_datei = r"C:\Users\Igor\Desktop\github\Bevölkerung\Rohdaten\Struktur_Bereinigt.xlsx"

# Lade alle Blattnamen
xls = pd.ExcelFile(eingabe_datei)
alle_blaetter = xls.sheet_names

# Nur Jahresblätter ab 2013
relevante_blaetter = [s for s in alle_blaetter if s.isdigit() and int(s) >= 2013]
relevante_blaetter.sort()

# Neue Excel-Datei
wb = Workbook()
wb.remove(wb.active)

# Spalten A–I (Index 0–8)
spalten_behalten = list(range(0, 9))

# Neue Spaltennamen
neue_spalten = [
    "Region", "Total", "0–19", "20–64", "65+",
    "Männlich", "Weiblich", "Schweizer", "Ausländer"
]

# Verarbeitung
for blatt in relevante_blaetter:
    df = pd.read_excel(eingabe_datei, sheet_name=blatt)

    # Entferne Zeilen 1–4 (Index 0–3) + Zeile 37 (Index 36)
    df_bereinigt = df.iloc[4:36, spalten_behalten].copy()

    # Spaltenüberschriften setzen
    df_bereinigt.columns = neue_spalten

    # Neues Tabellenblatt schreiben
    ws = wb.create_sheet(title=blatt)
    for row in dataframe_to_rows(df_bereinigt, index=False, header=True):
        ws.append(row)

# Speichern
wb.save(ausgabe_datei)
print(f"✓ Datei gespeichert unter:\n{ausgabe_datei}")
