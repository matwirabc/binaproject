import pandas as pd
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows
import os

# === Dateipfade ===
verzeichnis = r"C:\Users\Igor\Desktop\github\Bevölkerung\Rohdaten"
eingabe_datei = os.path.join(verzeichnis, "Struktur_Bereinigt.xlsx")
ausgabe_datei = os.path.join(verzeichnis, "Struktur_Auswertung.xlsx")

# === Excel-Datei einlesen ===
excel_file = pd.ExcelFile(eingabe_datei)
sheet_names = sorted(excel_file.sheet_names)

# Altersgruppen für Wachstumsberechnung
altersgruppen = ["0–19", "20–64", "65+"]

# Alle Daten in Dictionary einlesen
dataframes = {
    name: pd.read_excel(eingabe_datei, sheet_name=name)
    for name in sheet_names
}

# Neue Arbeitsmappe vorbereiten
wb = Workbook()
wb.remove(wb.active)

# Berechne prozentuale Veränderungen ab dem zweiten Jahr
for i in range(1, len(sheet_names)):
    prev_year = sheet_names[i - 1]
    curr_year = sheet_names[i]

    df_prev = dataframes[prev_year].copy().set_index("Region")
    df_curr = dataframes[curr_year].copy().set_index("Region")

    for group in altersgruppen:
        col_name = f"{group}_Wachstum"
        df_curr[col_name] = ((df_curr[group] - df_prev[group]) / df_prev[group]) * 100

    df_curr.reset_index(inplace=True)
    dataframes[curr_year] = df_curr

# Sicherstellen, dass auch das erste Jahr ohne Wachstum drin ist
dataframes[sheet_names[0]] = dataframes[sheet_names[0]]

# Alle Blätter in Ausgabedatei schreiben
for name, df in dataframes.items():
    ws = wb.create_sheet(title=name)
    for row in dataframe_to_rows(df, index=False, header=True):
        ws.append(row)

# Datei speichern
wb.save(ausgabe_datei)
print(f"✓ Auswertungsdatei gespeichert unter:\n{ausgabe_datei}")
