import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# IBCS-konforme Farbpalette
ibcs_palette = {
    "Ist": "#000000",
    "Plan": "#0070C0",
    "Prognose": "#B3B3B3",
    "Vorjahr": "#D9D9D9",
    "Positiv": "#00B050",
    "Negativ": "#FF0000",
    "Männlich": "#000000",
    "Weiblich": "#D9D9D9"
}

# === 1. Einwohnerentwicklung ===
def plot_einwohnerentwicklung(df, region=None):
    if region:
        df = df[df['Region'] == region]
    df = df.set_index('Region').T.reset_index().rename(columns={'index': 'Jahr'})
    df_long = df.melt(id_vars='Jahr', var_name='Region', value_name='Einwohner')

    sns.set_style("whitegrid")
    plt.figure(figsize=(10, 5))
    sns.lineplot(data=df_long, x='Jahr', y='Einwohner', hue='Region', palette=[ibcs_palette["Ist"]])
    plt.title(f"Einwohnerentwicklung {'der Region ' + region if region else 'in der Schweiz'}")
    plt.ylabel("Einwohnerzahl")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


# === 2. Altersstrukturentwicklung ===
def plot_altersstruktur(df, region):
    df = df[df["Region"] == region]
    df = df.set_index("Region").T.reset_index().rename(columns={'index': 'Jahr'})
    df = df[["Jahr", "0–19", "20–64", "65+"]]
    df = df[1:]  # Header-Zeile entfernen

    df_long = df.melt(id_vars="Jahr", var_name="Altersgruppe", value_name="Bevölkerung")

    plt.figure(figsize=(10, 5))
    sns.lineplot(
        data=df_long,
        x="Jahr",
        y="Bevölkerung",
        hue="Altersgruppe",
        palette=["#000000", "#B3B3B3", "#D9D9D9"]  # IBCS: Ist + Prognose + Vorjahr
    )
    plt.title(f"Altersentwicklung in {region}")
    plt.ylabel("Anzahl Personen")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


# === 3. Geschlechteranteil ===
def plot_geschlechteranteil(df, year):
    df = df.copy()
    df = df[["Region", "Männlich", "Weiblich"]]
    df["Total"] = df["Männlich"] + df["Weiblich"]
    df["Männer %"] = (df["Männlich"] / df["Total"]) * 100
    df["Frauen %"] = (df["Weiblich"] / df["Total"]) * 100
    df_long = df.melt(
        id_vars="Region",
        value_vars=["Männer %", "Frauen %"],
        var_name="Geschlecht",
        value_name="Anteil (%)"
    )

    plt.figure(figsize=(10, 5))
    sns.barplot(
        data=df_long,
        x="Region",
        y="Anteil (%)",
        hue="Geschlecht",
        palette=[ibcs_palette["Männlich"], ibcs_palette["Weiblich"]]
    )
    plt.title(f"Geschlechterverteilung {year}")
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()
