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


# Wie hat sich die Anzahl der Passagiere über die Jahre hinweg in den verschiedenen Kantonen verändert?
# Fokus: regionale Unterschiede & Entwicklungen

# Unterscheiden sich Langstrecken- (z. B. InterRegio) und Kurzstreckenverkehr (z. B. Regionalzug) im Nutzungsmuster?
# Fokus: Vergleich von Verkehrstypen

# Gibt es ähnliche Entwicklungen zwischen bestimmten Kantonen (z. B. Zürich vs. Bern)?
# Fokus: Cluster-/Korrelationserkennung


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# CSV-Datei laden
df = pd.read_csv("anzahlbahnhof.csv")

# Mapping von Bahnhöfen zu Kantonen
ort_zu_kanton = {
    "Aarau": "AG", "Baden": "AG", "Basel SBB": "BS", "Bellinzona": "TI", "Bern": "BE", "Biel/Bienne": "BE",
    "Chur": "GR", "Fribourg/Freiburg": "FR", "Genève": "GE", "Genève-Aéroport": "GE", "Genève-Eaux-Vives": "GE",
    "Lausanne": "VD", "Lugano": "TI", "Luzern": "LU", "Neuchâtel": "NE", "Olten": "SO", "St. Gallen": "SG",
    "Thun": "BE", "Uster": "ZH", "Winterthur": "ZH", "Yverdon-les-Bains": "VD", "Zürich HB": "ZH",
    "Zürich Oerlikon": "ZH", "Zürich Stadelhofen": "ZH", "Zürich Altstetten": "ZH", "Zürich Enge": "ZH",
    "Zürich Hardbrücke": "ZH", "Zug": "ZG", "Sion": "VS", "Schaffhausen": "SH", "Burgdorf": "BE",
    "Solothurn": "SO", "Bulle": "FR", "Wil SG": "SG", "Locarno": "TI", "Romanshorn": "TG", "Sierre/Siders": "VS",
    "Gossau SG": "SG", "Kreuzlingen": "TG", "Martigny": "VS", "Brig": "VS", "Pfäffikon SZ": "SZ",
    "Wädenswil": "ZH", "Rapperswil": "SG", "Wohlen AG": "AG", "Arth-Goldau": "SZ", "Langenthal": "BE",
    "Liestal": "BL", "Baar": "ZG", "Thalwil": "ZH"
}

# Datenvorbereitung
df["Kanton"] = df["Bahnhof_Gare_Stazione"].map(ort_zu_kanton)
df["Anzahl Bahnhofbenutzer"] = df["Anzahl Bahnhofbenutzer"].fillna(0)
df = df.drop(columns=["Unité"])
pivot_df = df.groupby(["Jahr", "Kanton"])["Anzahl Bahnhofbenutzer"].sum().unstack()
pivot_df_clean = pivot_df[pivot_df.index != 2013]
mittelwerte_clean = pivot_df_clean.mean()

# Top 5 Kantone identifizieren
top5_kantone = mittelwerte_clean.sort_values(ascending=False).head(5).index.tolist()
gruppen = {"Top-Kantone": [], "Gruppiert": []}
for kanton in mittelwerte_clean.index:
    if kanton in top5_kantone:
        gruppen["Top-Kantone"].append(kanton)
    else:
        gruppen["Gruppiert"].append(kanton)

# Zeitstrahl (Historische Entwicklung)
fig, ax = plt.subplots(figsize=(14, 6))
for kanton in gruppen["Top-Kantone"]:
    ax.plot(pivot_df_clean.index, pivot_df_clean[kanton], label=kanton, color="black", linestyle="-", linewidth=2)
gruppe_df = pivot_df_clean[gruppen["Gruppiert"]].sum(axis=1)
ax.plot(gruppe_df.index, gruppe_df, label="Andere Kantone (gruppiert)", color="gray", linestyle="--", linewidth=1.5)
ax.set_title("Tägliche Bahnhofbenutzer pro Jahr – Top 5 + Gruppierung (ohne 2013)")
ax.set_xlabel("Jahr")
ax.set_ylabel("Anzahl Bahnhofbenutzer pro Tag")
ax.set_xticks(pivot_df_clean.index)
ax.set_yticks([0, 500000, 1000000, 1500000, 1800000])
ax.set_yticklabels(["0", "500k", "1 Mio", "1.5 Mio", "1.8 Mio"])
ax.grid(axis='y', linestyle='--', alpha=0.6)
ax.legend(title="Kanton", bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0.)
plt.tight_layout(rect=[0, 0, 0.85, 1])
plt.show()

# Prognose mit linearer Regression (3 Jahre)
jahre = pivot_df_clean.index.to_numpy().reshape(-1, 1)
prognose_jahre = np.array([2024, 2025, 2026]).reshape(-1, 1)
alle_jahre = np.concatenate((jahre.flatten(), prognose_jahre.flatten()))

prognosen = {}
for kanton in gruppen["Top-Kantone"]:
    model = LinearRegression().fit(jahre, pivot_df_clean[kanton].to_numpy())
    prognosen[kanton] = model.predict(np.vstack((jahre, prognose_jahre)))

model = LinearRegression().fit(jahre, gruppe_df.to_numpy())
prognosen["Andere Kantone (gruppiert)"] = model.predict(np.vstack((jahre, prognose_jahre)))

plt.figure(figsize=(14, 6))
farben = ["black", "dimgray", "#333333", "#555555", "#777777"]
linienstile = ["--", "-.", ":", (0, (5, 1)), (0, (3, 3))]

for i, kanton in enumerate(gruppen["Top-Kantone"]):
    color = farben[i % len(farben)]
    linestyle = linienstile[i % len(linienstile)]
    plt.plot(jahre.flatten(), prognosen[kanton][:len(jahre)], linestyle="-", color=color, linewidth=2)
    plt.plot(prognose_jahre.flatten(), prognosen[kanton][len(jahre):], linestyle=linestyle, color=color, linewidth=2.5, label=f"{kanton}")

plt.plot(jahre.flatten(), prognosen["Andere Kantone (gruppiert)"][:len(jahre)], linestyle="-", color="lightgray", linewidth=1.5)
plt.plot(prognose_jahre.flatten(), prognosen["Andere Kantone (gruppiert)"][len(jahre):], linestyle=(0, (2, 2)), color="lightgray", linewidth=1.5, label="Andere (Prognose)")

plt.title("Zeitstrahl der Bahnhofbenutzer – Historisch & Prognose")
plt.xlabel("Jahr")
plt.ylabel("Anzahl Bahnhofbenutzer pro Tag")
plt.xticks(ticks=alle_jahre, labels=[str(int(j)) for j in alle_jahre])
plt.yticks(ticks=[0, 500000, 1000000, 1500000, 1800000], labels=["0", "500k", "1 Mio", "1.5 Mio", "1.8 Mio"])
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.legend(title="Kanton", bbox_to_anchor=(1.02, 1), loc='upper left')
plt.tight_layout(rect=[0, 0, 0.85, 1])
plt.show()


### Abodaten

# CSV-Dateien laden


# Daten einlesen
abos_df = pd.read_excel("abos.xlsx")
plz_df = pd.read_excel("ortsverzeichnis.xlsx", skiprows=1)

# Spaltennamen bereinigen
abos_df.columns = abos_df.columns.str.strip()
plz_df.columns = plz_df.columns.str.strip()

# Datentypen anpassen (PLZ als Integer)
abos_df["PLZ"] = abos_df["PLZ"].astype(int)
plz_df["PLZ"] = plz_df["PLZ"].astype(int)

# Kantonskürzel per PLZ aus Ortsverzeichnis mappen
abos_df = abos_df.merge(plz_df[["PLZ", "Kantonskürzel"]], on="PLZ", how="left")

# Bezeichnung umwandeln
abos_df = abos_df.rename(columns={"Kantonskürzel": "kanton_abo"})

# Ausgabe prüfen (optional)
print(abos_df.head())


# Abo-Daten nach Jahr und Kanton aggregieren
abo_agg = abos_df.groupby(["Jahr", "kanton_abo"])[["Generalabonnement", "Halbtaxabonnement"]].sum().reset_index()

# Umbenennen für Klarheit
abo_agg = abo_agg.rename(columns={"kanton_abo": "Kanton"})

# Original Bahnhof-Daten (nicht pivotiert) vorbereiten
bahnhof_df = df[["Jahr", "Kanton", "Anzahl Bahnhofbenutzer"]].copy()

# Bahnhof- & Abo-Daten zusammenführen
combined_df = bahnhof_df.merge(abo_agg, on=["Jahr", "Kanton"], how="left")

## Runden
# Nur numerische Spalten auswählen
numerische_spalten = ["Anzahl Bahnhofbenutzer", "Generalabonnement", "Halbtaxabonnement"]

# NaN-Werte auffüllen (z. B. bei leeren Abos)
combined_df[numerische_spalten] = combined_df[numerische_spalten].fillna(0)

# Runden und als int speichern
combined_df[numerische_spalten] = combined_df[numerische_spalten].round(0).astype(int)


# Ausgabe prüfen
print(combined_df.head())

combined_df.to_csv("final_bahnhof_abos.csv", index=False)




