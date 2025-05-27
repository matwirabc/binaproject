import pandas as pd
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows
import os

def bereinige_rohdaten(eingabe_datei: str, ausgabe_datei: str) -> dict:
    """
    Bereinigt alle Tabellenblätter aus der Strukturdatei:
    - behält nur Zeilen 5–36 (Index 4–35)
    - behält nur Spalten A–I (Index 0–8)
    - ersetzt Spaltenüberschriften
    - speichert bereinigte Datei
    - gibt ein dict mit Jahres-DataFrames zurück
    """

    # Nur Jahresblätter ab 2013
    xls = pd.ExcelFile(eingabe_datei)
    relevante_blaetter = [s for s in xls.sheet_names if s.isdigit() and int(s) >= 2013]
    relevante_blaetter.sort()

    # Spalten A–I (Index 0–8)
    spalten_behalten = list(range(0, 9))
    neue_spalten = [
        "Region", "Total", "0–19", "20–64", "65+",
        "Männlich", "Weiblich", "Schweizer", "Ausländer"
    ]

    # Neue Excel-Datei vorbereiten
    wb = Workbook()
    wb.remove(wb.active)

    # Ergebnis-Dictionary
    daten_bereinigt = {}

    for blatt in relevante_blaetter:
        df = pd.read_excel(eingabe_datei, sheet_name=blatt)
        df_bereinigt = df.iloc[4:36, spalten_behalten].copy()
        df_bereinigt.columns = neue_spalten

        daten_bereinigt[blatt] = df_bereinigt.copy()

        # In neues Tabellenblatt schreiben
        ws = wb.create_sheet(title=blatt)
        for row in dataframe_to_rows(df_bereinigt, index=False, header=True):
            ws.append(row)

    # Speichern der bereinigten Excel-Datei
    os.makedirs(os.path.dirname(ausgabe_datei), exist_ok=True)
    wb.save(ausgabe_datei)

    print(f"✓ Bereinigte Datei gespeichert unter: {ausgabe_datei}")
    return daten_bereinigt
