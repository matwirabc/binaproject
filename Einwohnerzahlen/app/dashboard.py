import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from scripts.load import lade_bereinigte_daten
from scripts.visualize import (
    plot_einwohnerentwicklung,
    plot_altersstruktur,
    plot_geschlechterverteilung,
    plot_altersverteilung_ein_jahr,
    plot_prozentuale_entwicklung_altersgruppen
)

#Daten laden
df_all = lade_bereinigte_daten("data/Verarbeitet/Struktur_Bereinigt.xlsx")

#Benutzeroberfläche
st.title("Bevölkerungsentwicklung in der Schweiz")
st.markdown("**Datenbasis:** Bundesamt für Statistik (BFS), 2013–2023")

#Auswahl der Region und Jahr
alle_regionen = sorted(df_all["Region"].unique())
alle_jahre = sorted(df_all["Jahr"].unique(), reverse=True)

region = st.selectbox("Region auswählen", alle_regionen)

#Diagramm 1: Einwohnerentwicklung
st.header("Einwohnerentwicklung")
fig1 = plot_einwohnerentwicklung(df_all, region)
if fig1:
    st.pyplot(fig1)

#Diagramm 2: Altersstruktur über Zeit
st.header("Altersstruktur über Zeit")
fig2 = plot_altersstruktur(df_all, region)
if fig2:
    st.pyplot(fig2)

#Diagramm 3: Altersverteilung eines Jahres
st.header("Altersverteilung in einem Jahr")
jahr_alter = st.selectbox("Jahr für Altersverteilung auswählen", alle_jahre, key="jahr_alter")
fig3 = plot_altersverteilung_ein_jahr(df_all, region, jahr_alter)
if fig3:
    st.pyplot(fig3)

#Diagramm 4–6: Prozentuale Entwicklung nach Altersgruppe
st.header("Prozentuale Entwicklung der Altersgruppen")
figs = plot_prozentuale_entwicklung_altersgruppen(df_all, region)
for fig in figs:
    st.pyplot(fig)

#Diagramm 7: Geschlechterverteilung
st.header("Geschlechterverteilung")
jahr_geschlecht = st.selectbox("Jahr für Geschlechterverteilung auswählen", alle_jahre, key="jahr_geschlecht")
fig4 = plot_geschlechterverteilung(df_all, region, jahr_geschlecht)
if fig4:
    st.pyplot(fig4)
