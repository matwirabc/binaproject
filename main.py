##IBSC 2013 - 2024 -> historische vergleich, prognose nur mit 2024, prognose bis 3 jahren
# standart trends pro datensatz, 2 trends & prognose,
# vergleich von langgstreken vs. kurzstrecken interregio, nöd regio.
# under und overfitting wichtig für die arbeit!!
# lineare regression für die prognose
# geammtzahl der kantone bzw. der anzahl zusammenfassen. unnötige daten vermeiden
# korrelationsanalyse, lineare regreession, zeitreihe.

# Frage: Entwickeln sich gewisse Kantone ähnlich? (z. B. Zürich vs. Bern)
# Frage: Gibt es eine starke Korrelation zwischen Jahr und Anzahl Bahnhofbenutzer?

# Korrelation zwischen Bahnhöfen
# Wenn du Bahnhof-Daten (nicht aggregiert auf Kanton) hast: Gibt es Bahnhöfe, deren Nutzung sich stark miteinander verändert?


# Langstrecke vs. Kurzstrecke (Interregio vs. Regional)
# Wenn du Bahnhöfe oder Linien zuordnen kannst:
# Hypothese: Zunahme in Langstrecken korreliert mit Rückgang oder Stagnation in Kurzstrecken?
# Du könntest dazu Cluster bilden: Bahnhof = „Langstreckenhub“ oder „Kurzstreckenbahnhof“.

#https://data.sbb.ch/explore/dataset/zugzahlen/table/?sort=jahr -> Anzahl Züge pro Strecke


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Pfad zur Datei
file_path = '/Users/robin/Documents/GitHub/BINA/passagierfrequenz.csv'

# Lade die CSV-Datei
data = pd.read_csv(file_path)

# Spalte hinzufügen
jahr_index = data.columns.get_loc('Kt_Ct_Cantone')

