import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# === Einwohnerentwicklung ===
def plot_einwohnerentwicklung(df_all, region):
    df = df_all[df_all["Region"] == region]
    if df.empty:
        return None

    df = df.sort_values("Jahr")
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.lineplot(data=df, x="Jahr", y="Total", marker="o", color="#000000", ax=ax)
    ax.set_ylabel("Einwohnerzahl")
    ax.set_title(f"Einwohnerentwicklung in {region}")
    ax.grid(True)
    return fig

# === Altersstruktur über Jahre ===
def plot_altersstruktur(df_all, region):
    df = df_all[df_all["Region"] == region]
    if df.empty:
        return None

    df = df.sort_values("Jahr")
    df_alter = df[["Jahr", "0–19", "20–64", "65+"]].melt(
        id_vars="Jahr", var_name="Altersgruppe", value_name="Bevölkerung"
    )

    fig, ax = plt.subplots(figsize=(10, 5))
    sns.lineplot(data=df_alter, x="Jahr", y="Bevölkerung", hue="Altersgruppe",
                 palette=["#000000", "#B3B3B3", "#D9D9D9"], marker="o", ax=ax)
    ax.set_ylabel("Anzahl Personen")
    ax.set_title(f"Altersstruktur in {region}")
    ax.grid(True)
    return fig

# === Geschlechterverteilung ===
def plot_geschlechterverteilung(df_all, region, jahr):
    df = df_all[(df_all["Region"] == region) & (df_all["Jahr"] == jahr)]
    if df.empty:
        return None

    maennlich = df["Männlich"].values[0]
    weiblich = df["Weiblich"].values[0]
    total = maennlich + weiblich

    df_geschlecht = pd.DataFrame({
        "Geschlecht": ["Männer", "Frauen"],
        "Anteil (%)": [maennlich / total * 100, weiblich / total * 100]
    })

    fig, ax = plt.subplots(figsize=(6, 4))
    sns.barplot(data=df_geschlecht, x="Geschlecht", y="Anteil (%)",
                palette=["#000000", "#D9D9D9"], ax=ax)
    ax.set_ylim(0, 100)
    ax.set_title(f"Anteil Männer und Frauen in {region}, {jahr}")
    ax.bar_label(ax.containers[0], fmt="%.1f%%")
    return fig

# === Altersverteilung eines Jahres (Anteile) ===
def plot_altersverteilung_ein_jahr(df_all, region, jahr):
    df = df_all[(df_all["Region"] == region) & (df_all["Jahr"] == jahr)]
    if df.empty:
        return None

    altersgruppen = ["0–19", "20–64", "65+"]
    werte = df[altersgruppen].values[0]
    df_verteilung = pd.DataFrame({
        "Altersgruppe": altersgruppen,
        "Anteil (%)": [wert / sum(werte) * 100 for wert in werte]
    })

    fig, ax = plt.subplots(figsize=(6, 4))
    sns.barplot(data=df_verteilung, x="Altersgruppe", y="Anteil (%)",
                palette=["#000000", "#B3B3B3", "#D9D9D9"], ax=ax)
    ax.set_ylim(0, 100)
    ax.set_title(f"Anteil Altersgruppen in {region}, {jahr}")
    ax.bar_label(ax.containers[0], fmt="%.1f%%")
    return fig

# === Prozentuale Veränderung Altersgruppen (3 Plots) ===
def plot_prozentuale_entwicklung_altersgruppen(df_all, region):
    df = df_all[df_all["Region"] == region].sort_values("Jahr")
    df_pct = df.copy()
    df_pct[["0–19", "20–64", "65+"]] = df_pct[["0–19", "20–64", "65+"]].pct_change() * 100
    df_pct = df_pct.reset_index(drop=True).drop_duplicates(subset="Jahr")

    figs = []
    farben = {"0–19": "#000000", "20–64": "#B3B3B3", "65+": "#D9D9D9"}

    for gruppe in ["0–19", "20–64", "65+"]:
        fig, ax = plt.subplots(figsize=(6, 3))
        sns.lineplot(data=df_pct, x="Jahr", y=gruppe, marker="o", color=farben[gruppe], ax=ax)
        ax.set_title(f"Veränderung {gruppe} (%)")
        ax.axhline(0, color="gray", linestyle="--")
        figs.append(fig)

    return figs
