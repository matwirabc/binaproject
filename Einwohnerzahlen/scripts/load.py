import pandas as pd

def lade_bereinigte_daten(pfad: str) -> pd.DataFrame:
    """Lädt alle bereinigten Blätter und kombiniert sie zu einem DataFrame mit Jahres-Spalten"""
    excel_file = pd.ExcelFile(pfad)
    jahre = sorted([s for s in excel_file.sheet_names if s.isdigit()])

    df_alle = pd.concat([
        pd.read_excel(pfad, sheet_name=jahr).assign(Jahr=int(jahr))
        for jahr in jahre
    ])
    return df_alle
