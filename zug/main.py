


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import plotly.graph_objs as go
from scipy.stats import pearsonr
from scipy.stats import pearsonr, linregress




##==== Vorbereitung der Datensätze ====##
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

df["Kanton"] = df["Bahnhof_Gare_Stazione"].map(ort_zu_kanton)
df["Anzahl Bahnhofbenutzer"] = df["Anzahl Bahnhofbenutzer"].fillna(0)
df = df.drop(columns=["Unité"])
pivot_df = df.groupby(["Jahr", "Kanton"])["Anzahl Bahnhofbenutzer"].sum().unstack()
pivot_df_clean = pivot_df[pivot_df.index != 2013]
mittelwerte_clean = pivot_df_clean.mean()

##==== Abos & Halbtax ====##

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

##==== Prognose und Korelation  ====##

# Daten einlesen
df = pd.read_csv("final_bahnhof_abos.csv")
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import pearsonr, linregress

# CSV laden
df = pd.read_csv("final_bahnhof_abos.csv")

# Durchschnitt pro Kanton berechnen
df_avg = df.groupby("Kanton")[["Anzahl Bahnhofbenutzer", "Generalabonnement", "Halbtaxabonnement"]].mean().reset_index()

# Korrelation und Regressionslinie (GA)
ga_corr, _ = pearsonr(df_avg["Anzahl Bahnhofbenutzer"], df_avg["Generalabonnement"])
slope_ga, intercept_ga, _, _, _ = linregress(df_avg["Anzahl Bahnhofbenutzer"], df_avg["Generalabonnement"])

# Korrelation und Regressionslinie (Halbtax)
ht_corr, _ = pearsonr(df_avg["Anzahl Bahnhofbenutzer"], df_avg["Halbtaxabonnement"])
slope_ht, intercept_ht, _, _, _ = linregress(df_avg["Anzahl Bahnhofbenutzer"], df_avg["Halbtaxabonnement"])

# Visualisierung
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# GA-Plot
axes[0].scatter(df_avg["Anzahl Bahnhofbenutzer"], df_avg["Generalabonnement"], color="black")
axes[0].plot(df_avg["Anzahl Bahnhofbenutzer"],
             intercept_ga + slope_ga * df_avg["Anzahl Bahnhofbenutzer"],
             linestyle="--", color="gray")
for _, row in df_avg.iterrows():
    axes[0].text(row["Anzahl Bahnhofbenutzer"], row["Generalabonnement"], row["Kanton"], fontsize=8)
axes[0].set_title(f"GA vs Bahnhofnutzung (r = {ga_corr:.2f})")
axes[0].set_xlabel("Ø Bahnhofbenutzer pro Tag")
axes[0].set_ylabel("Ø Generalabonnemente")

# Halbtax-Plot
axes[1].scatter(df_avg["Anzahl Bahnhofbenutzer"], df_avg["Halbtaxabonnement"], color="black")
axes[1].plot(df_avg["Anzahl Bahnhofbenutzer"],
             intercept_ht + slope_ht * df_avg["Anzahl Bahnhofbenutzer"],
             linestyle="--", color="gray")
for _, row in df_avg.iterrows():
    axes[1].text(row["Anzahl Bahnhofbenutzer"], row["Halbtaxabonnement"], row["Kanton"], fontsize=8)
axes[1].set_title(f"Halbtax vs Bahnhofnutzung (r = {ht_corr:.2f})")
axes[1].set_xlabel("Ø Bahnhofbenutzer pro Tag")
axes[1].set_ylabel("Ø Halbtaxabos")

plt.tight_layout()
plt.show()

##==== Prognose und Zeitstrahl Bahnhof Nutzung ====## -> Hier mit Strichpunkten arbeiten. 
# Farben gemäss IBCS
IBCS_BLACK = "#000000"
IBCS_GRAY = "#888888"

# Finalen Datensatz laden
combined_df = pd.read_csv("final_bahnhof_abos.csv")

# Formatierungshilfe
def format_mio(x):
    return f"{x / 1e6:.1f} Mio"

# Zeitraum eingrenzen (ab 2013)
combined_df = combined_df[combined_df["Jahr"].between(2013, 2023)]

# Schweizweite Aggregation
df_ch = combined_df.groupby("Jahr")[["Anzahl Bahnhofbenutzer", "Generalabonnement", "Halbtaxabonnement"]].sum().reset_index()
df_ch["Kanton"] = "CH"

# Kantonale Aggregation
df_kanton = combined_df.groupby(["Jahr", "Kanton"])[["Anzahl Bahnhofbenutzer", "Generalabonnement", "Halbtaxabonnement"]].sum().reset_index()

# Liste aller Kantone
alle_kantone = sorted(df_kanton["Kanton"].unique())
start_kanton = "ZH"

# Funktion zur Erstellung eines Vergleichsdiagramms für eine Metrik
def create_f3_chart(metric, title, y_label):
    fig = go.Figure()

    for kanton in alle_kantone:
        sichtbar = (kanton == start_kanton)
        df_kt = df_kanton[df_kanton["Kanton"] == kanton]
        df_ch_tmp = df_ch.copy()

        # Linie: Kanton
        fig.add_trace(go.Scatter(
            x=df_kt["Jahr"],
            y=df_kt[metric],
            mode="lines+markers+text",
            name=kanton,
            visible=sichtbar,
            line=dict(color=IBCS_BLACK, width=2),
            marker=dict(color=IBCS_BLACK),
            text=[format_mio(v) for v in df_kt[metric]],
            textposition="top center",
            textfont=dict(size=9),
            legendgroup=kanton
        ))

        # Linie: CH-Vergleich (gestrichelt)
        fig.add_trace(go.Scatter(
            x=df_ch_tmp["Jahr"],
            y=df_ch_tmp[metric],
            mode="lines+markers+text",
            name="CH – Vergleich",
            visible=sichtbar,
            line=dict(color=IBCS_GRAY, width=2, dash="dot"),
            marker=dict(color=IBCS_GRAY),
            text=[format_mio(v) for v in df_ch_tmp[metric]],
            textposition="top center",
            textfont=dict(size=9),
            legendgroup=kanton,
            showlegend=False
        ))

    # Dropdown-Menü erstellen
    buttons = []
    for i, kanton in enumerate(alle_kantone):
        sichtbarkeit = [False] * (2 * len(alle_kantone))
        sichtbarkeit[2 * i] = True
        sichtbarkeit[2 * i + 1] = True
        buttons.append(dict(
            label=kanton,
            method="update",
            args=[
                {"visible": sichtbarkeit},
                {"title.text": f"{title} ({kanton} vs. CH, 2013–2023)"}
            ]
        ))

    # Layout
    fig.update_layout(
        title=dict(text=f"{title} ({start_kanton} vs. CH, 2013–2023)", x=0.01, xanchor="left"),
        xaxis=dict(title="Jahr", tickmode='linear', dtick=1, linecolor=IBCS_GRAY),
        yaxis=dict(title=y_label, gridcolor="#dddddd", linecolor=IBCS_GRAY),
        plot_bgcolor="white",
        paper_bgcolor="white",
        height=500,
        width=900,
        showlegend=False,
        updatemenus=[{
            "buttons": buttons,
            "direction": "down",
            "showactive": True,
            "x": 1.05,
            "y": 1.15
        }]
    )
    return fig

# Diagramme erzeugen
fig1 = create_f3_chart("Anzahl Bahnhofbenutzer", "F3: Bahnhofnutzung", "Bahnhofbenutzer pro Tag")
fig2 = create_f3_chart("Generalabonnement", "F3: Generalabonnemente", "Anzahl GA")
fig3 = create_f3_chart("Halbtaxabonnement", "F3: Halbtaxabonnemente", "Anzahl Halbtax")

# Anzeigen
fig1.show()
fig2.show()
fig3.show()




##### F1 und F2


# Farben gemäss IBCS
IBCS_BLACK = "#000000"
IBCS_GRAY = "#888888"

# Daten laden
df = pd.read_csv("final_bahnhof_abos.csv")

# Hilfsfunktion: Formatierung in Mio
def format_mio(x):
    return f"{x / 1e6:.1f} Mio"

# Bahnhofnutzung pro Jahr und Kanton
df_kanton = df.groupby(["Jahr", "Kanton"])["Anzahl Bahnhofbenutzer"].sum().reset_index()
df_kanton["Text"] = df_kanton["Anzahl Bahnhofbenutzer"].apply(format_mio)

# Gesamtschweiz berechnen
df_ch = df.groupby("Jahr")["Anzahl Bahnhofbenutzer"].sum().reset_index()
df_ch["Kanton"] = "CH"
df_ch["Text"] = df_ch["Anzahl Bahnhofbenutzer"].apply(format_mio)

# Alle Daten zusammenführen
df_all = pd.concat([df_kanton, df_ch], ignore_index=True)

# Liste aller Kantone
alle_kantone = sorted(df_all["Kanton"].unique())
start_kanton = "ZH"
start_index = alle_kantone.index(start_kanton)

# Plot erstellen
fig = go.Figure()

for kanton in alle_kantone:
    sichtbar = (kanton == start_kanton)
    daten = df_all[df_all["Kanton"] == kanton]

    # Historische Werte
    fig.add_trace(go.Scatter(
        x=daten["Jahr"],
        y=daten["Anzahl Bahnhofbenutzer"],
        mode="lines+markers+text",
        name=f"{kanton} (real)",
        visible=sichtbar,
        line=dict(color=IBCS_BLACK, width=2),
        marker=dict(color=IBCS_BLACK),
        text=daten["Text"],
        textposition="top center",
        textfont=dict(size=9, color=IBCS_BLACK),
        showlegend=False
    ))

    # Prognose ab 2024–2026
    vergangen = daten[daten["Jahr"] <= 2023]
    X = vergangen["Jahr"].values.reshape(-1, 1)
    y = vergangen["Anzahl Bahnhofbenutzer"].values

    if len(X) >= 2:
        model = LinearRegression().fit(X, y)
        zukunftsjahre = np.array([2024, 2025, 2026]).reshape(-1, 1)
        prognose = model.predict(zukunftsjahre)
        prognose_text = [format_mio(p) for p in prognose]

        fig.add_trace(go.Scatter(
            x=zukunftsjahre.flatten(),
            y=prognose,
            mode="lines+markers+text",
            name=f"{kanton} (Prognose)",
            visible=sichtbar,
            line=dict(color=IBCS_GRAY, width=2, dash="dot"),
            marker=dict(color=IBCS_GRAY),
            text=prognose_text,
            textposition="top center",
            textfont=dict(size=9, color=IBCS_GRAY),
            showlegend=False
        ))

# Dropdown-Buttons
buttons = []
for i, kanton in enumerate(alle_kantone):
    sichtbarkeit = []
    for k in alle_kantone:
        sichtbarkeit.extend([k == kanton, k == kanton])  # Real und Prognose
    buttons.append(dict(
        label=kanton,
        method="update",
        args=[
            {"visible": sichtbarkeit},
            {"title.text": f"Zeitreihe & Prognose tägliche Bahnhofnutzung in {kanton} (2023–2026)"}
        ]
    ))

# Layout nach IBCS
fig.update_layout(
    title=dict(
        text=f"Zeitreihe & Prognose tägliche Bahnhofnutzung in {start_kanton} (2023–2026)",
        x=0.01,
        xanchor="left",
        font=dict(size=16, color=IBCS_BLACK)
    ),
    xaxis=dict(
        title="Jahr",
        tickmode='linear',
        dtick=1,
        linecolor=IBCS_GRAY,
        tickfont=dict(size=9, color=IBCS_BLACK),
        title_font=dict(size=10, color=IBCS_BLACK)
    ),
    yaxis=dict(
        title="Bahnhofbenutzer",
        gridcolor="#dddddd",
        zeroline=False,
        linecolor=IBCS_GRAY,
        tickfont=dict(size=9, color=IBCS_BLACK),
        title_font=dict(size=10, color=IBCS_BLACK)
    ),
    plot_bgcolor="white",
    paper_bgcolor="white",
    height=500,
    width=900,
    showlegend=False,
    updatemenus=[{
        "buttons": buttons,
        "direction": "down",
        "showactive": True,
        "active": start_index,
        "x": 1.05,
        "y": 1.15
    }]
)

# Anzeige
fig.show()

##==== Zeitstrahl top 5 Kantone ====##
# Top 5 Kantone identifizieren
top5_kantone = mittelwerte_clean.sort_values(ascending=False).head(5).index.tolist()
gruppen = {"Top-Kantone": [], "Gruppiert": []}
for kanton in mittelwerte_clean.index:
    if kanton in top5_kantone:
        gruppen["Top-Kantone"].append(kanton)
    else:
        gruppen["Gruppiert"].append(kanton)

# Zeitstrahl Top 5
fig, ax = plt.subplots(figsize=(14, 6))
for kanton in gruppen["Top-Kantone"]:
    ax.plot(pivot_df_clean.index, pivot_df_clean[kanton], label=kanton, color="black", linestyle="-", linewidth=2)
gruppe_df = pivot_df_clean[gruppen["Gruppiert"]].sum(axis=1)
ax.plot(gruppe_df.index, gruppe_df, label="Andere Kantone (gruppiert)", color="gray", linestyle="--", linewidth=1.5)
ax.set_title("Tägliche Bahnhofbenutzer – Top 5 + Gruppierung (ohne 2013)")
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

plt.title("Zeitstrahl der Bahnhofbenutzer pro Tag – Historisch & Prognose")
plt.xlabel("Jahr")
plt.ylabel("Anzahl Bahnhofbenutzer pro Tag")
plt.xticks(ticks=alle_jahre, labels=[str(int(j)) for j in alle_jahre])
plt.yticks(ticks=[0, 500000, 1000000, 1500000, 1800000], labels=["0", "500k", "1 Mio", "1.5 Mio", "1.8 Mio"])
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.legend(title="Kanton", bbox_to_anchor=(1.02, 1), loc='upper left')
plt.tight_layout(rect=[0, 0, 0.85, 1])
plt.show()