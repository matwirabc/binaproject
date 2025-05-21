# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.17.1
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# # Flugverkehrsanalyse Schweiz (2016 - 2024)
# ---
#
# **Datum:** 20. Mai 2025
# **Modul:** BINA
# **Semesterarbeit**
#
# ---

# ## Einleitung
#
# Im Jahr 2023 gab es insgesamt 53.3  Millionen Passagiere im Linien- und Charterverkehr (swissinfo, 2024). Um den Schweizer Luftfahrtsektor effektiv steuern zu können, sind fundierte Entscheidungsgrundlagen unerlässlich. Doch die grosse Menge an Rohdaten über Flugbewegungen macht es Politik und Betreibern schwer, klare operative Muster, historische Entwicklungen oder zukünftige Trends zu erkennen. Dies wiederum erschwert die Planung, die Ressourcenallokation und die Leistungsbewertung.

# **Zielsetzung:** Um die verschiedenen Stakeholder bei der Planung zu unterstützen, analysiert die Arbeit Flugbewegungsdaten der Schweiz für den Zeitraum Januar 2016 bis Dezember 2024. Ziel ist es, ein klares Bild des Ist-Zustands und der historischen Entwicklung des Flugverkehrs zu schaffen, daraus operative Muster abzuleiten und erste datengestützte Entscheidungsideen für die relevanten Stakeholder zu formulieren. Exemplarisch wird zudem das Potenzial prädiktiver Analysemethoden aufgezeigt.
#
# Die Untersuchung folgt dabei einem strukturierten Vorgehen, angelehnt an das "From Data to Decisions"-Framework, und präsentiert die Ergebnisse nach den Standards der International Business Communication Standards (IBCS), um Klarheit und eine hohe Relevanz für Entscheidungen sicherzustellen. Analysiert werden die Bewegungen an den wichtigsten Schweizer Flughäfen im genannten Zeitraum. Der Prozess umfasst gemäss Marr (2020) folgende Schritte:
# 1.  Definition der Ziele und Informationsbedürfnisse.
# 2.  Sammlung und Aufbereitung der Flugdaten.
# 3.  Analyse der Daten hinsichtlich relevanter Kennzahlen, historischer Trends und exemplarischer Vorhersagemodelle.
# 4.  Präsentation der gewonnenen Informationen.
# 5.  Ableitung von potenziellen datengestützten Entscheidungen und Handlungsempfehlungen.
#
# Der Fokus dieser Analyse liegt auf der deskriptiven und explorativen Auswertung der Daten, ergänzt durch erste prädiktive Anwendungen. Dabei wird keine tiefgehenden Kausalanalysen externer Faktoren durchgeführt. Auch spezifische operative Details wie Flugzeugtypen oder detaillierte Verspätungsursachen sind nicht Teil dieser Arbeit.

# ## Management Summary
#
# Die effektive Steuerung des Schweizer Luftfahrtsektors erfordert klare, datengestützte Einblicke, die aus der grossen Menge der verfügbaren Rohdaten oft nur schwer zu gewinnen sind. Dies limitiert die Möglichkeiten von Politik und Betreibern bei Planung, Ressourcenallokation und Leistungsbewertung. Um hier eine fundierte Basis zu schaffen, analysiert die Arbeit Flugbewegungsdaten aus der Schweiz der Jahre 2016 bis 2024. Das Ziel ist es, den Ist-Zustand und historische Trends des Flugverkehrs aufzuzeigen und daraus operative Muster sowie konkrete Ideen für Entscheidungen abzuleiten. Exemplarisch wurde zudem das Potenzial prädiktiver Analysen demonstriert, indem zwei Modelle zur Vorhersage des täglichen Flugaufkommens am Flughafen Zürich (LSZH) für die nächsten 90 Tage (Stand: Ende 2024) entwickelt wurden. Das Prophet-Modell, das explizit Trends und saisonale Muster berücksichtigt, deutet auf tendenziell steigende tägliche Flugzahlen hin. Ergänzend wurde ein lineares Regressionsmodell mit zeitbasierten Features trainiert. Dieses Modell zeigte auf einem Test-Set der letzten 90 Tage einen Mean Absolute Error (MAE) von 66.72 Flügen. Das bedeutet, dass die lineare Regression die tatsächliche tägliche Fluganzahl im Testzeitraum durchschnittlich um rund 67 Flüge verfehlte, was einen ersten Anhaltspunkt für die Vorhersagegenauigkeit dieses Ansatzes liefert. Die Analyse folgt einem strukturierten Ansatz und stellt die Ergebnisse übersichtlich dar. Der Fokus liegt dabei auf den Daten der wichtigsten Flughäfen und den daraus resultierenden Mustern.
#
# **Wichtigste Erkenntnisse**:
# * Das Flugaufkommen am Flughafen Zürich (LSZH) zeigte über den Zeitraum 2016-2024 deutliche Schwankungen: Wachstum bis 2019 (204'531 Flüge), ein starker Einbruch in den Jahren 2020 (89'176 Flüge) und 2021 (98'924 Flüge) bedingt durch die COVID-19-Pandemie, gefolgt von einer schnellen Erholung. Im Jahr 2024 übertraf das Volumen mit 215'020 Flügen wieder das Vor-Pandemie-Niveau. Im nationalen Vergleich hatte Zürich über den gesamten Analysezeitraum hinweg die führende Rolle. Der Flughafen wickelte 1'390'722 Flüge ab, was einem Anteil von 47.3% am Gesamtvolumen aller analysierten Flughäfen entspricht. Das Gesamtvolumen aller Flüge war 2'941'079.
# * Die Fluggesellschaft SWISS (Code 'SWR') hat über den analysierten Zeitraum eine führende Position im Schweizer Luftraum. Mit insgesamt 836'644 Flügen, führt sie 28.9% aller Flüge aus. Am Flughafen Zürich war die SWISS 'SWR' für 714'104 Flüge verantwortlich, was 51.8% der Flüge an diesem Flughafen entspricht.
# * Internationale Flüge machen konstant den Grossteil des Verkehrs aus (ca. 91.4% des Flugverkehrs mit Schweizer Bezug). Die Route zwischen Zürich (LSZH) und London Heathrow (EGLL) stellt auch historisch eine Schlüsselverbindung dar, sowohl bei Ankünften (häufigste Herkunft mit 30'840 Flügen) als auch bei Abflügen (häufigstes Ziel mit 29'289 Flügen) von/nach Zürich.
# * Die Prognose für den Flughafen Zürich (LSZH), deutet auf tendenziell steigende tägliche Flugzahlen für die nächsten 90 Tage (Stand: Ende 2024) hin, unter Berücksichtigung historischer Daten und saisonaler Muster.
# * Die durchschnittliche erfasste Netzwerksichtbarkeitsdauer zeigte für alle Flüge einen Median von 73.1 Minuten. Für den gefilterten plausiblen Bereich (1 Min - 20 Std) lag der Median bei 73.1 Minuten und der Durchschnitt bei 106.3 Minuten. Am Flughafen Zürich lag der Median bei 76.2 Minuten und der Durchschnitt bei 126.1 Minuten (basierend auf gefilterten Daten). Dies deutet auf potenziell etwas längere operative Zeiten oder Flugdauern in Zürich hin.
#
# **Potenzielle Entscheidungen/Handlungsempfehlungen**:
# * **Flughafenbetreiber:** Können die historischen Trenddaten und die positive kurzfristige Prognose zur Anpassung und Bestätigung langfristiger Kapazitätsplanungen sowie Investitionsentscheidungen nutzen. Die Ressourcenallokation (Personal, Gates) sollte saisonale Spitzen (aus Prophet-Komponenten ersichtlich) und die prognostizierten Nachfragesteigerungen berücksichtigen, um operative Effizienz sicherzustellen.
# * **Fluggesellschaften:** Können ihre Marktpositionsanalyse durch die detaillierten Daten zu Airline-Anteilen und die historische Entwicklung verfeinern. Routenstrategien sollten basierend auf der Performance von Schlüsselverbindungen (wie beispielsweise Zürich-London) und den allgemeinen langfristigen Nachfragetrends sowie der positiven prognostizierten Entwicklung angepasst werden.
# * **Regulierung/Flugsicherung:** Die langfristigen Daten zur Verkehrsentwicklung, die deutliche Erholung und die Prognosen können zur Neubewertung der Luftrauminfrastruktur und zur Antizipation zukünftiger Kapazitätsbedarfe dienen. Erkenntnisse zur Netzwerksichtbarkeitsdauer können in Analysen zur Luftraumeffizienz einfliessen.
#
# **Nächste Schritte (Feedback Loop):** Eine Verfeinerung der Prognosemodelle (z.B. durch Einbeziehung externer Faktoren wie Ölpreise, Wirtschaftsindikatoren, spezifische Events oder Pandemie-Indikatoren und Hyperparameter-Optimierung) und eine detailliertere Untersuchung der Ursachen für beobachtete historische Trendbrüche (z.B. detaillierter Einfluss von COVID-19, Wirtschaftskrisen) könnten die Präzision der Entscheidungsgrundlagen weiter verbessern. Zudem wäre die Entwicklung von Szenarioanalysen (optimistisch, pessimistisch, Basis) für robustere Planungen wertvoll.
#
# ---

# ## 1. Schritt: Definition von Zielen und Informationsbedürfnissen
#
# **Ziel:** Klare Definition der strategischen Ziele dieser Analyse und der daraus abgeleiteten Informationsbedürfnisse ("Was müssen wir wissen?"). Identifikation der Zielgruppen ("Wer muss was wissen?") und Formulierung von Key Analytics Questions (KAQs). Die Definition der Informationsbedürfnisse soll sicherstellen, dass die Analyse auf die relevantesten Fragen fokussiert und nicht nur auf verfügbare Daten (Marr, 2020).
#
# ### 1.1 Strategischer Kontext und Zielsetzung
#
# Die Analyse des Flugverkehrs ist für diverse Akteure in der Schweiz von strategischer Bedeutung. Ziel dieser spezifischen Analyse ist es, ein klares Bild des Ist-Zustands und der historischen Entwicklung des Flugbetriebs im Zeitraum Januar 2016 bis Dezember 2024 zu erhalten. Dies dient als Grundlage für operative Bewertungen, strategische Anpassungen und eine erste Einschätzung zukünftiger Entwicklungen. Der Fokus liegt auf Verkehrsaufkommen, Hauptakteuren (Airlines), wichtigen Routen, betrieblichen Charakteristika und der Demonstration prädiktiver Methoden.
#
# ### 1.2 Target Audience
#
# Die Stakeholder für diese Analyse sind die folgenden Entscheidungsträger:
# * **Flughafenmanagement (z.B. Zürich, Genf):** Benötigen Informationen zur Auslastung (KAQ 1), zu den wichtigsten Airlines (KAQ 2) und Routen (KAQ 3) für Ressourcenplanung, operative Steuerung, strategische Entwicklung und zur Antizipation von Nachfrage (KAQ 6).
# * **Fluggesellschaften (z.B. SWISS, EasyJet):** Interessiert an Marktanteilen (KAQ 2), Konkurrenzaktivitäten (KAQ 2), Routenperformance (KAQ 3) und Nachfrageprognosen (KAQ 6) zur Bewertung der eigenen Position und Optimierung des Netzwerks.
# * **Flugsicherung (z.B. Skyguide):** Fokus auf Verkehrsfluss (KAQ 1), Luftraumnutzung, potenziellen Engpässen (approximiert durch KAQ 5) und zukünftiger Luftraumbelastung (KAQ 6).
# * **Politische Entscheidungsträger/Behörden:** Beobachtung der Gesamtentwicklung (KAQ 1), Verhältnis national/international (KAQ 4), und langfristiger Trends (KAQ 1, KAQ 6) als Input für regulatorische Überlegungen oder Infrastrukturplanungen.
#
# ### 1.3 Key Analytics Questions (KAQs)
#
# Basierend auf den Zielen und der relevanten Stakheolder leiten wir folgende zentrale Analysefragen (KAQs) ab:
#
# 1.  **KAQ 1:** Wie hat sich das gesamte Flugaufkommen über die Schweizer Hauptflughäfen im Zeitraum 2016-2024 entwickelt und wie verteilt es sich aktuell? *(Strategische Relevanz: Marktdynamik, Ressourcenauslastung, langfristige Trends)*
# 2.  **KAQ 2:** Welche Fluggesellschaften waren im Schweizer Luftraum und an den Hauptflughäfen im Zeitraum 2016-2024 am aktivsten und wie hat sich ihre Relevanz verändert? *(Strategische Relevanz: Key Partner/Competitor Dynamics, Marktanteilsentwicklung)*
# 3.  **KAQ 3:** Welches sind die häufigsten Flugrouten (Herkunft/Ziel) für die wichtigsten Schweizer Flughäfen und wie hat sich deren Bedeutung im Zeitraum 2016-2024 entwickelt? *(Strategische Relevanz: Nachfrageanalyse, Infrastrukturbedarf, Routenprofitabilität)*
# 4.  **KAQ 4:** Wie verteilt sich der Flugverkehr auf nationale und internationale Segmente und gab es Verschiebungen im Zeitraum 2016-2024? *(Strategische Relevanz: Marktstruktur, internationale Anbindung, nationale Versorgung)*
# 5.  **KAQ 5:** Wie verteilt sich die **Netzwerksichtbarkeitsdauer** der Flüge, und gibt es signifikante Unterschiede oder zeitliche Veränderungen (2016-2024)? *(Strategische Relevanz: Indikator für operative Charakteristika/Effizienz, Luftraumnutzung)*
# 6.  **KAQ 6 (Prädiktiv):** Wie könnte sich das Flugaufkommen für einen ausgewählten Flughafen (z.B. LSZH) in den nächsten Monaten entwickeln, basierend auf historischen Daten und saisonalen Mustern? *(Strategische Relevanz: Antizipation von Nachfrage, proaktive Ressourcenplanung)*
#
# ### 1.4 Potenzielle Entscheidungsfelder
#
# Die Beantwortung dieser KAQs soll potenzielle Entscheidungen in folgenden Bereichen unterstützen:
# * **Langfristige Strategie & Investitionen:** Basierend auf historischen Trends (KAQ 1-5) und Prognosen (KAQ 6).
# * **Ressourcenallokation:** Optimierung der Personal- und Infrastrukturplanung.
# * **Routenentwicklung & Netzwerkplanung:** Bewertung und Anpassung von Flugplänen.
# * **Marktpositionierung & Wettbewerbsanalyse:** Benchmarking für Airlines und Flughäfen.
# * **Operative Effizienz & Kapazitätsmanagement:** Input für Flugsicherungsanalysen und Flughafenbetrieb.
#
# ### 1.5 Angewandte Standards: IBCS
#
# Zur Sicherstellung einer klaren, konsistenten und entscheidungsorientierten Kommunikation werden die International Business Communication Standards (IBCS) angewendet.
#
# ---

# ## 2. Schritt: Sammlung und Aufbereitung der Daten (Collect Data)
#
# **Ziel:** Identifikation, Sammlung, Bereinigung und Anreicherung der relevanten Daten, um die in Schritt 1 definierten KAQs beantworten zu können. Kritische Bewertung von Datenquellen, -typen, -formaten und -qualität (Marr, 2020).
#
# ### 2.1 Datenquelle, Umfang und Art
#
# * **Primäre Datenquelle und Methodik:** Als Basis für diese Analyse dienen Rohdaten des OpenSky Networks. Die automatische Erfassung und initiale Aufbereitung dieser Daten erfolgte mittels eines Python-Skripts, das Flugbewegungsdaten basierend auf ADS-B (Automatic Dependent Surveillance–Broadcast) Signalen von OpenSky abfragt. Eine genauere Beschreibung dazu ist in Abschnitt 2.3.1 dieses Notebooks vorhanden.
# * **Verwendete Datei im Notebook:** Für die Standardausführung dieser Analyse wird eine vorab generierte CSV-Datei (`data/swiss_flight_data_20160101_20241231.csv`) verwendet. Diese Datei enthält die mittels des genannten Skripts von OpenSky gesammelten und aufbereiteten Daten. Dieser Ansatz dient primär der Zeitersparnis bei wiederholten Analysedurchläufen und der Sicherstellung der Reproduzierbarkeit mit einem festen Datensatz. Das Notebook hat die Option, die Daten über das Skript live neu vom OpenSky Network abzurufen (`EXECUTE_OPENSKY_LIVE_DATA_COLLECTION = True`), was jedoch aufgrund des Zeitaufwands nicht standardmässig aktiviert ist.
# * **Zeitraum:** 1. Januar 2016 bis 31. Dezember 2024.
# * **Räumlicher Fokus:** Flugbewegungen mit Bezug zu den definierten Schweizer Flughäfen (`SCHWEIZER_FLUGHAFEN`).
# * **Datenart:** Die Analyse basiert ausschliesslich auf **strukturierten Aktivitätsdaten** (Flugbewegungs-Records mit Zeitstempeln, Positionen, Kennungen). Es werden keine externen Datenquellen (z.B. Wetter, Events, Wirtschaft) oder unstrukturierten Daten (z.B. Nachrichten, Social Media) integriert.
#
# ### 2.2 Datenqualität und Limitationen
#
# Die Aussagekraft der Analyse wird durch folgende Punkte beeinflusst:
# * **Datenherkunft und Aufbereitung:** Die Daten stammen vom OpenSky Network und wurden durch das in Abschnitt 2.3.1 dokumentierte Skript gesammelt und vorverarbeitet. Wird die standardmässig genutzte CSV-Datei verwendet, so repräsentiert diese einen Snapshot der Daten, wie sie zum Zeitpunkt der Erstellung der CSV über das Skript von OpenSky verfügbar und verarbeitet wurden. Die Qualität und Vollständigkeit der Daten in der CSV hängen somit von der Abdeckung und Datenintegrität des OpenSky Network zu jenem Zeitpunkt sowie der Logik und den Parametern des Sammelskripts (z.B. API-Abfragefrequenz, Fehlerbehandlung) ab. Bei einer Live-Abfrage gelten die jeweils aktuellen Bedingungen des OpenSky Network und des Skripts.
#
#   **Hinweis zu historischen Daten von OpenSky:**
#   Aufgrund technischer Probleme im Jahr 2023 gingen einige historische Daten verloren (OpenSky Network, o. J.).
#   OpenSky weist daher darauf hin, dass die folgenden Zeiträume von Forschungsarbeiten auszuschliessen, um die Datengenauigkeit zu gewährleisten (alle Zeiten in UTC):
#
#   * `2023-01-02 23:00:00` → `2023-01-03 10:00:00`
#   * `2023-01-18 11:00:00` → `2023-01-23 07:00:00`
#   * `2023-06-21 13:00:00` → `2023-06-21 22:00:00`
#   * `2023-11-15 06:00:00` → `2023-11-16 08:00:00`
#   * `2023-11-20 01:00:00` → `2023-11-20 03:00:00`
#   * `2023-12-02 08:00:00` → `2023-12-05 03:00:00`
#   * `2024-05-20 10:00:00` → `2024-05-21 05:00:00`
#
#   Für eine genauere Analyse sollten diese Datenlücken berücksichtigt werden sollen. Da die Datenaufbereitung jedoch bereits viel Zeit in Anspruch nahm und der Fokus der Arbeit nicht der produktive Einsatz der Erkenntnisse umzusetzen, wurden diese Lücken ignoriert.
#
# * **Approximationen:**
#     * Die "Netzwerksichtbarkeitsdauer" (`network_duration_minutes`), berechnet aus `firstseen` und `lastseen`, ist lediglich eine **Approximation** der tatsächlichen Flugzeit im vom OpenSky Network erfassten relevanten Luftraum.
#     * Der `airline_code` (extrahiert aus `callsign`) ist ebenfalls nur eine **Approximation** und nicht immer eine offizielle IATA- oder ICAO-Kennung.
# * **Datenschutz und Eigentumsrechte:** Es wurde keine formale Datenschutz-Folgenabschätzung durchgeführt. Die Nutzungsrechte der Daten basieren auf den öffentlich zugänglichen Daten des OpenSky Network und dessen Nutzungsbedingungen. Grundsätzlich sind die Daten von OpenSky für nichtkommerzielle Zwecke frei verfügbar.
# * **Prädiktive Modelle:** Die in dieser Arbeit demonstrierten Vorhersagemodelle sind exemplarisch und nicht für den produktiven Einsatz optimiert. Externe Faktoren, die das Flugaufkommen beeinflussen (z.B. Pandemien, Wirtschaftskrisen, geopolitische Ereignisse, spezifische Grossveranstaltungen), werden in den hier verwendeten einfachen Modellen nicht explizit als separate Variablen berücksichtigt, können aber implizit in den historischen Datenmustern enthalten sein.
#
# **Konsequenz:** Alle Ergebnisse, insbesondere Prognosen, müssen vor dem Hintergrund dieser Limitationen und der spezifischen Art der Datengewinnung und -aufbereitung betrachtet werden.
#
# ### 2.3 Bibliotheken und Konfiguration
#
# Laden der notwendigen Python-Bibliotheken und globale Einstellungen.

# +
import pandas as pd
from datetime import datetime, timezone, timedelta
import logging
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import numpy as np
import io
import os
import time

# Für die optionale Konvertierung des Notebooks zu HTML
os.system('jupyter nbconvert --to html flightsnotebook.ipynb')

# Libraries Prophet und SkLearn
try:
    from prophet import Prophet
    # from prophet.plot import plot_plotly, plot_components_plotly # Optional für interaktive Plots
    PROPHET_AVAILABLE = True
except ImportError:
    PROPHET_AVAILABLE = False
    logging.warning("Prophet library not found. Prophet Predictions werden übersprungen.")

try:
    from sklearn.linear_model import LinearRegression
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import mean_squared_error, mean_absolute_error
    SKLEARN_AVAILABLE = True
except ImportError:
    SKLEARN_AVAILABLE = False
    logging.warning("Scikit-learn library not found. Linear Regression Predictions werden übersprungen.")


# Logging Konfiguration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# --- Analysekonfiguration ---
FLUGHAFEN_MAP = {
    'LSZH': 'Zürich', 'LSGG': 'Genève', 'LSZB': 'Bern-Belp',
    'LSZA': 'Lugano-Agno', 'LSZR': 'St. Gallen-Altenrhein', 'LFSB': 'Basel-Mulhouse (EuroAirport)'
}
SCHWEIZER_FLUGHAFEN = list(FLUGHAFEN_MAP.keys())
FLUGHAFEN_ZU_ANALYSIEREN = list(FLUGHAFEN_MAP.keys())

# Standard-Dateiname (Fallback falls EXECUTE_OPENSKY_LIVE_DATA_COLLECTION=false)
CSV_DATEINAME = "data/swiss_flight_data_20160101_20241231.csv"
ANALYSE_START_DATUM = pd.to_datetime("2016-01-01", utc=True)
ANALYSE_ENDE_DATUM = pd.to_datetime("2024-12-31", utc=True)

EXECUTE_OPENSKY_LIVE_DATA_COLLECTION = False # Um Zeit zu sparen sollte die Variable auf False bleiben
OPENSKY_LIB_AVAILABLE = False

# --- IBCS Style Defaults ---
plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['font.sans-serif'] = ['Arial', 'Helvetica', 'sans-serif']
plt.rcParams['axes.labelcolor'] = '#333333'; plt.rcParams['xtick.color'] = '#333333'; plt.rcParams['ytick.color'] = '#333333'
plt.rcParams['axes.edgecolor'] = '#CCCCCC'; plt.rcParams['figure.titleweight'] = 'bold'; plt.rcParams['axes.titleweight'] = 'bold'
plt.rcParams['axes.titlelocation'] = 'left'; plt.rcParams['axes.grid'] = False; plt.rcParams['figure.facecolor'] = 'white'
plt.rcParams['axes.facecolor'] = 'white'; plt.rcParams['axes.spines.top'] = False; plt.rcParams['axes.spines.right'] = False
plt.rcParams['axes.spines.left'] = False; plt.rcParams['axes.spines.bottom'] = True; plt.rcParams['xtick.bottom'] = True
plt.rcParams['ytick.left'] = False; plt.rcParams['axes.titlesize'] = 14; plt.rcParams['axes.labelsize'] = 10

IBCS_SCHWARZ = '#000000'; IBCS_DUNKELGRAU = '#5A5A5A'; IBCS_MITTELGRAU = '#8C8C8C'
IBCS_HELLGRAU = '#D3D3D3'; IBCS_ROT = '#FF0000'; IBCS_GRUEN = '#008000'

logging.info(f"Analysierte Flughäfen: {', '.join(FLUGHAFEN_ZU_ANALYSIEREN)}")
# -

# ## 2.3.1 (Optional) Live-Datensammlung vom OpenSky Network
#
# **Ziel:** Dieser Abschnitt ermöglicht die optionale Sammlung von Flugdaten direkt von der OpenSky Network API für den im Notebook definierten Analysezeitraum und die relevanten Flughäfen. Dies kann nützlich sein, um aktuellere Daten zu erhalten oder den Datenerfassungsprozess nachzuvollziehen.
#
# **Voraussetzungen:**
# * Die Python-Bibliothek `pyopensky` muss installiert sein (`pip install pyopensky`).
# * Eine funktionierende Internetverbindung ist erforderlich.
# * Für den Zugriff auf die OpenSky Network Trino-Schnittstelle (die `pyopensky` für historische Daten nutzt) sind OpenSky Network Zugangsdaten erforderlich.
# * **Achtung:** Das Abrufen von Daten über einen langen Zeitraum (mehrere Jahre) kann sehr lange dauern und eine grosse Menge an Daten generieren.
#
# **Steuerung:**
# Die Ausführung dieses Codeblocks wird durch die globale Variable `EXECUTE_OPENSKY_LIVE_DATA_COLLECTION` gesteuert.
# * Wenn `EXECUTE_OPENSKY_LIVE_DATA_COLLECTION = False` (Standard), wird dieser Block übersprungen, und das Notebook verwendet die unter `CSV_DATEINAME` definierte CSV-Datei.
# * Wenn `EXECUTE_OPENSKY_LIVE_DATA_COLLECTION = True`, versucht der Code, die Daten abzurufen, zu verarbeiten und als neue CSV-Datei im `data/` Verzeichnis zu speichern. Wenn die Ausführung erfolgreich war, wird die Variable `CSV_DATEINAME` auf die neue Datei aktualisiert.
#
# **Datenformat:**
# Damit die Daten in einem Format sind mit der eine Analyse später einfacher möglich ist, werden einige Operationen durchgeführt um ein angemessen Format zu erhalten:
# * Umbenennung von Columns.
# # * Konvertierung von Zeitstempeln.
# * Bestimmung von `flight_type` und `locality`.
# * Berechnung von `network_duration_minutes` und `airline_code`.

# +
# Der folgende Teil wird nur ausgeführt, wenn die Datensammlung mit OpenSky explizit erwünscht ist.
if EXECUTE_OPENSKY_LIVE_DATA_COLLECTION:
    logging.warning("EXECUTE_OPENSKY_LIVE_DATA_COLLECTION ist True. Versuche, Live-Daten von OpenSky zu sammeln.")
    logging.warning("Dies kann lange dauern und erfordert die pyopensky-Bibliothek und eine funktionierende OpenSky-Verbindung.")

    try:
        from pyopensky.trino import Trino
        OPENSKY_LIB_AVAILABLE = True
        logging.info("Pyopensky erfolgreich importiert.")
    except ImportError:
        OPENSKY_LIB_AVAILABLE = False
        logging.error("Live-Datensammlung mit OpenSky übersprungen aufgrund ImportError.")

    if OPENSKY_LIB_AVAILABLE:
        OPENSKY_START_TIME = ANALYSE_START_DATUM
        OPENSKY_STOP_TIME = ANALYSE_ENDE_DATUM
        OPENSKY_AIRPORTS_TO_QUERY = FLUGHAFEN_ZU_ANALYSIEREN

        OPENSKY_OUTPUT_DIR = "data"
        os.makedirs(OPENSKY_OUTPUT_DIR, exist_ok=True)

        start_str_ds = OPENSKY_START_TIME.strftime('%Y%m%d')
        end_str_ds = OPENSKY_STOP_TIME.strftime('%Y%m%d')
        OPENSKY_CSV_FILENAME_TEMPLATE = f"swiss_flight_data_opensky_{start_str_ds}_{end_str_ds}.csv"
        NEW_CSV_FILE_PATH = os.path.join(OPENSKY_OUTPUT_DIR, OPENSKY_CSV_FILENAME_TEMPLATE)

        opensky_start_ts = int(OPENSKY_START_TIME.timestamp())
        opensky_stop_ts = int(OPENSKY_STOP_TIME.timestamp())

        def safe_timestamp_os(ts_input):
            if pd.isna(ts_input): return None
            try:
                if isinstance(ts_input, (int, float)):
                    if ts_input > 1e12: ts_input /= 1000
                    return datetime.fromtimestamp(int(ts_input), timezone.utc)
                elif isinstance(ts_input, str):
                     return pd.to_datetime(ts_input, utc=True, errors='coerce').to_pydatetime()
                elif isinstance(ts_input, datetime):
                    return ts_input.replace(tzinfo=timezone.utc) if ts_input.tzinfo is None else ts_input.astimezone(timezone.utc)
                elif isinstance(ts_input, pd.Timestamp):
                    return ts_input.tz_localize(timezone.utc) if ts_input.tzinfo is None else ts_input.tz_convert(timezone.utc).to_pydatetime()
                logging.warning(f"Unerwarteter Typ für Zeitstempel in safe_timestamp_os: {type(ts_input)}, Wert: {ts_input}")
                return None
            except (ValueError, TypeError, OverflowError) as e:
                logging.warning(f"Fehler bei safe_timestamp_os für '{ts_input}': {e}")
                return None

        def fetch_flight_data_os(trino_conn, airport_icao, start_timestamp, stop_timestamp) -> pd.DataFrame:
            logging.info(f"Rufe Daten für {airport_icao} ab: Von {datetime.fromtimestamp(start_timestamp, timezone.utc)} bis {datetime.fromtimestamp(stop_timestamp, timezone.utc)}")
            max_retries = 3; retry_delay = 10
            for attempt in range(max_retries):
                try:
                    results_df = trino_conn.flightlist(start_timestamp, stop_timestamp, airport=airport_icao)
                    if results_df is None:
                        logging.warning(f"OpenSky API gab None zurück für {airport_icao}. Versuch {attempt + 1}/{max_retries}.")
                        if attempt < max_retries - 1: time.sleep(retry_delay); continue
                        return pd.DataFrame()
                    if isinstance(results_df, pd.DataFrame):
                        if not results_df.empty:
                            logging.info(f"{len(results_df)} Datensätze für {airport_icao} von OpenSky erhalten.")
                            rename_map = {'departure': 'estdepartureairport', 'arrival': 'estarrivalairport'}
                            results_df.rename(columns=rename_map, inplace=True, errors='ignore')
                        else: logging.info(f"Keine Datensätze für {airport_icao} im Zeitraum gefunden.")
                        return results_df
                    else:
                        logging.error(f"Unerwarteter Ergebnistyp von OpenSky: {type(results_df)} für {airport_icao}")
                        return pd.DataFrame()
                except Exception as e:
                    logging.error(f"Fehler beim Abrufen der Daten für {airport_icao} (Versuch {attempt + 1}/{max_retries}): {e}")
                    if "authentication failed" in str(e).lower():
                        logging.error("Authentifizierungsfehler mit OpenSky.")
                        return pd.DataFrame()
                    if attempt < max_retries - 1: time.sleep(retry_delay)
                    else: logging.error(f"Maximale Trials für {airport_icao} erreicht.")
                    return pd.DataFrame()
            return pd.DataFrame()

        def process_raw_data_os(input_df: pd.DataFrame, query_airport_icao: str) -> list:
            if not isinstance(input_df, pd.DataFrame) or input_df.empty: return []
            processed_data_list = []
            logging.info(f"Verarbeite {len(input_df)} Datensätze für {query_airport_icao}...")
            for row_tuple in input_df.itertuples(index=False):
                try:
                    dep_airport_candidate = getattr(row_tuple, 'estdepartureairport', None)
                    arr_airport_candidate = getattr(row_tuple, 'estarrivalairport', None)
                    callsign_val = getattr(row_tuple, 'callsign', None)
                    icao24_val = getattr(row_tuple, 'icao24', None)
                    firstseen_val = safe_timestamp_os(getattr(row_tuple, 'firstseen', None))
                    lastseen_val = safe_timestamp_os(getattr(row_tuple, 'lastseen', None))

                    dep_airport_icao = dep_airport_candidate.strip().upper() if isinstance(dep_airport_candidate, str) and len(dep_airport_candidate) in [3,4] else None
                    arr_airport_icao = arr_airport_candidate.strip().upper() if isinstance(arr_airport_candidate, str) and len(arr_airport_candidate) in [3,4] else None

                    flight_type_val = 'Unknown'
                    if arr_airport_icao == query_airport_icao and dep_airport_icao != query_airport_icao : flight_type_val = 'ARRIVAL'
                    elif dep_airport_icao == query_airport_icao and arr_airport_icao != query_airport_icao: flight_type_val = 'DEPARTURE'
                    elif arr_airport_icao == query_airport_icao and dep_airport_icao == query_airport_icao:
                        flight_type_val = 'DEPARTURE'
                        logging.debug(f"Flug von/zu demselben query_airport {query_airport_icao}: {row_tuple}")
                    elif arr_airport_icao == query_airport_icao and dep_airport_icao is None: flight_type_val = 'ARRIVAL'
                    elif dep_airport_icao == query_airport_icao and arr_airport_icao is None: flight_type_val = 'DEPARTURE'

                    data_entry = {
                        'icao24': icao24_val, 'firstseen': firstseen_val, 'lastseen': lastseen_val,
                        'departure_airport': dep_airport_icao, 'arrival_airport': arr_airport_icao,
                        'callsign': callsign_val.strip().upper() if isinstance(callsign_val, str) else None,
                        'query_airport': query_airport_icao, 'flight_type': flight_type_val
                    }
                    if all([data_entry['icao24'], data_entry['firstseen'], data_entry['lastseen'], data_entry['query_airport']]) and data_entry['flight_type'] != 'Unknown':
                        processed_data_list.append(data_entry)
                except Exception as e:
                    logging.warning(f"Fehler bei der Verarbeitung Zeile für {query_airport_icao}: {e}. Zeile: {row_tuple}")
            return processed_data_list

        def get_flight_locality_os(row_series, swiss_airports_list):
            dep = str(row_series['departure_airport']).upper() if pd.notna(row_series['departure_airport']) else None
            arr = str(row_series['arrival_airport']).upper() if pd.notna(row_series['arrival_airport']) else None
            dep_is_swiss = pd.notna(dep) and dep in swiss_airports_list
            arr_is_swiss = pd.notna(arr) and arr in swiss_airports_list
            if dep_is_swiss and arr_is_swiss: return 'National'
            elif (dep_is_swiss and pd.notna(arr) and not arr_is_swiss) or \
                 (arr_is_swiss and pd.notna(dep) and not dep_is_swiss): return 'International'
            elif (dep_is_swiss and pd.isna(arr)) or (arr_is_swiss and pd.isna(dep)): return 'International (Unvollständig)'
            elif pd.notna(dep) and pd.notna(arr) and not dep_is_swiss and not arr_is_swiss: return 'Andere / Nicht-CH-Bezug'
            elif pd.isna(dep) and pd.isna(arr): return 'Unbekannt (Keine Route)'
            else: return 'Unbekannt (Sonstige)'

        # --- Hauptausführung der Datensammlung ---
        opensky_data_successfully_collected = False
        try:
            logging.info("Try Verbindung mit Trino herzustellen.")
            trino_conn = Trino()
            logging.info("Verbindung zu Trino erfolgreich hergestellt.")
            all_collected_flight_data = []
            for airport_code in OPENSKY_AIRPORTS_TO_QUERY:
                logging.info(f"--- Starte Datensammlung für Flughafen: {FLUGHAFEN_MAP.get(airport_code, airport_code)} ({airport_code}) ---")
                raw_df_airport = fetch_flight_data_os(trino_conn, airport_code, opensky_start_ts, opensky_stop_ts)
                if isinstance(raw_df_airport, pd.DataFrame) and not raw_df_airport.empty:
                    processed_list_airport = process_raw_data_os(raw_df_airport, airport_code)
                    if processed_list_airport:
                        all_collected_flight_data.extend(processed_list_airport)
                        logging.info(f"{len(processed_list_airport)} verarbeitete Datensätze für {airport_code} hinzugefügt.")
                else: logging.warning(f"Keine Daten für {airport_code} erhalten oder DataFrame war leer.")
                time.sleep(1)

            if not all_collected_flight_data:
                logging.warning("Keine validen Flugdaten über alle Flughäfen hinweg von OpenSky gesammelt.")
            else:
                df_opensky = pd.DataFrame(all_collected_flight_data)
                logging.info(f"Insgesamt {len(df_opensky)} Datensätze von OpenSky verarbeitet.")
                df_opensky['firstseen'] = pd.to_datetime(df_opensky['firstseen'], errors='coerce', utc=True)
                df_opensky['lastseen'] = pd.to_datetime(df_opensky['lastseen'], errors='coerce', utc=True)
                initial_rows_os = len(df_opensky)
                df_opensky.dropna(subset=['icao24', 'firstseen', 'lastseen', 'query_airport', 'flight_type'], inplace=True)
                logging.info(f"{initial_rows_os - len(df_opensky)} fehlerhafte Zeilen entfernt.")

                if df_opensky.empty:
                    logging.error("Nach Bereinigung sind keine Daten mehr vorhanden.")
                else:
                    subset_cols_dedup = ['icao24', 'firstseen', 'lastseen', 'departure_airport', 'arrival_airport']
                    initial_rows_before_dedup = len(df_opensky)
                    df_opensky.drop_duplicates(subset=subset_cols_dedup, keep='first', inplace=True)
                    logging.info(f"{initial_rows_before_dedup - len(df_opensky)} Duplikate entfernt.")

                    df_opensky['network_duration_minutes'] = (df_opensky['lastseen'] - df_opensky['firstseen']).dt.total_seconds() / 60
                    df_opensky.loc[df_opensky['network_duration_minutes'] < 0, 'network_duration_minutes'] = np.nan
                    df_opensky['airline_code'] = df_opensky['callsign'].astype(str).str[:3].str.upper()
                    df_opensky.loc[df_opensky['airline_code'].isin(['NON', 'NAN', '', 'N/A', 'UND', 'NULL']) | (df_opensky['airline_code'].str.len() < 3), 'airline_code'] = np.nan
                    df_opensky['locality'] = df_opensky.apply(get_flight_locality_os, args=(SCHWEIZER_FLUGHAFEN,), axis=1)
                    final_columns_os = ['icao24', 'firstseen', 'lastseen', 'query_airport', 'flight_type', 'callsign',
                                        'departure_airport', 'arrival_airport', 'network_duration_minutes',
                                        'airline_code', 'locality']
                    df_opensky = df_opensky[[col for col in final_columns_os if col in df_opensky.columns]]

                    df_save_os = df_opensky.copy()
                    df_save_os['firstseen'] = df_save_os['firstseen'].dt.strftime('%Y-%m-%d %H:%M:%S%z')
                    df_save_os['lastseen'] = df_save_os['lastseen'].dt.strftime('%Y-%m-%d %H:%M:%S%z')
                    df_save_os.to_csv(NEW_CSV_FILE_PATH, index=False, encoding='utf-8')
                    logging.info(f"Erfolgreich {len(df_save_os)} Datensätze in '{NEW_CSV_FILE_PATH}' gespeichert.")
                    CSV_DATEINAME = NEW_CSV_FILE_PATH # CSV-Datei aktualisieren!
                    logging.info(f"CSV_DATEINAME wurde auf '{CSV_DATEINAME}' aktualisiert.")
                    opensky_data_successfully_collected = True
        except Exception as e_main_os:
            logging.error(f"Fehler während OpenSky-Datensammlung: {e_main_os}")
        if not opensky_data_successfully_collected:
            logging.warning(f"OpenSky-Datensammlung nicht erfolgreich. Fallback auf: '{CSV_DATEINAME}'")
else:
    logging.info(f"EXECUTE_OPENSKY_LIVE_DATA_COLLECTION ist False. Überspringe Live-Datensammlung. Verwende: '{CSV_DATEINAME}'")

logging.info(f"Datenquelle für Analyse: {CSV_DATEINAME}")
logging.info(f"Analysezeitraum: {ANALYSE_START_DATUM.date()} - {ANALYSE_ENDE_DATUM.date()}")
# -

# ### 2.4 Laden der Rohdaten
# Einlesen der Daten und erste Inspektion. Die Variable `CSV_DATEINAME` wurde möglicherweise im vorherigen optionalen Schritt (2.3.1) aktualisiert.

# +
logging.info(f"Lade Rohdaten aus {CSV_DATEINAME}...")
df_rohdaten = None
rohdaten_info = "" # Für Anhang
try:
    datums_columns = ['firstseen', 'lastseen']
    try:
        df_rohdaten = pd.read_csv(CSV_DATEINAME, parse_dates=datums_columns, sep=',', engine='python', on_bad_lines='warn')
    except (ValueError, pd.errors.ParserError): # Fallback auf Semikolon
        logging.warning("Komma als Trennzeichen fehlgeschlagen oder Parser-Fehler, versuche Semikolon.")
        df_rohdaten = pd.read_csv(CSV_DATEINAME, parse_dates=datums_columns, sep=';', engine='python', on_bad_lines='warn')
    # Fallback mit automatischer Erkennung von Trennzeichen
    except Exception as e_sep:
         logging.warning(f"Explizite Trennzeichenerkennung fehlgeschlagen ({e_sep}), versuche 'sep=None' für automatische Erkennung.")
         df_rohdaten = pd.read_csv(CSV_DATEINAME, parse_dates=datums_columns, sep=None, engine='python', on_bad_lines='warn')


    logging.info(f"{len(df_rohdaten)} Roh-Datensätze erfolgreich geladen.")
    logging.info(f"Columns: {list(df_rohdaten.columns)}")

    print("--- Erste 5 Zeilen der Rohdaten ---")
    display(df_rohdaten.head())
    print("\n--- Datentypen der Rohdaten ---")
    display(df_rohdaten.dtypes.to_frame('Datentyp'))

    buffer = io.StringIO()
    df_rohdaten.info(buf=buffer)
    rohdaten_info = buffer.getvalue() # Für Anhang
    print("\n--- Info zu Non-Null Counts und Speicherbedarf (Rohdaten) ---")
    print(rohdaten_info)

except FileNotFoundError:
    logging.error(f"Datei {CSV_DATEINAME} nicht gefunden.")
except pd.errors.EmptyDataError:
    logging.error(f"Datei {CSV_DATEINAME} ist leer.")
except Exception as e:
    logging.error(f"Fehler beim Laden der Datei '{CSV_DATEINAME}': {e}")
# -

# ### 2.5 Datenbereinigung und -formatierung
# Sicherstellung korrekter Datentypen, Behandlung fehlender Werte in kritischen Kollonen sowie Konsistenzprüfungen.

# + tags=["scroll_output"]
df_cleaned = pd.DataFrame() # Initialisiere leeren DataFrame für den Fall, dass df_rohdaten None ist
bereinigt_info = "" # Für Anhang
bereinigt_describe = None # Für Anhang

if df_rohdaten is not None and not df_rohdaten.empty:
    logging.info("Beginne Datenbereinigung und -formatierung...")
    df_cleaned = df_rohdaten.copy()

    # --- Filtere Daten Analysezeitraum ---
    logging.info(f"Filtere Rohdaten auf den Zeitraum: {ANALYSE_START_DATUM.date()} bis {ANALYSE_ENDE_DATUM.date()}")
    # Sicherstellen, der Date-Formate
    for col_time_filter in ['firstseen', 'lastseen']:
        if col_time_filter in df_cleaned.columns:
            if not pd.api.types.is_datetime64_any_dtype(df_cleaned[col_time_filter]):
                df_cleaned[col_time_filter] = pd.to_datetime(df_cleaned[col_time_filter], errors='coerce')
            if pd.api.types.is_datetime64_any_dtype(df_cleaned[col_time_filter]):
                 if df_cleaned[col_time_filter].dt.tz is None:
                     df_cleaned[col_time_filter] = df_cleaned[col_time_filter].dt.tz_localize('UTC', ambiguous='NaT', nonexistent='NaT')
                 else:
                     df_cleaned[col_time_filter] = df_cleaned[col_time_filter].dt.tz_convert('UTC')
            else: # Falls Konvertierung Probleme macht
                logging.warning(f"Column {col_time_filter} konnte nicht in datetime konvertiert werden.")


    if 'firstseen' in df_cleaned.columns and pd.api.types.is_datetime64_any_dtype(df_cleaned['firstseen']):
        original_rows_before_date_filter = len(df_cleaned)
        df_cleaned = df_cleaned[
            (df_cleaned['firstseen'] >= ANALYSE_START_DATUM) &
            (df_cleaned['firstseen'] <= ANALYSE_ENDE_DATUM)
        ]
        rows_after_date_filter = len(df_cleaned)
        if original_rows_before_date_filter > rows_after_date_filter:
            logging.info(f"{original_rows_before_date_filter - rows_after_date_filter} Zeilen ausserhalb des gesetzten Analysezeitraums entfernt.")
        elif original_rows_before_date_filter == rows_after_date_filter and original_rows_before_date_filter > 0 :
             logging.info("Alle Daten sind innerhalb des Analysezeitraums.")
    else:
        logging.warning("Column 'firstseen' nicht im korrekten Datumsformat.")


    # --- UTC für firstseen und lastseen sicherstellen
    date_columns_clean = ['firstseen', 'lastseen']
    for column in date_columns_clean:
        if column in df_cleaned.columns:
            if not pd.api.types.is_datetime64_any_dtype(df_cleaned[column]):
                 df_cleaned[column] = pd.to_datetime(df_cleaned[column], errors='coerce') # errors='coerce' setzt ungültige Daten auf NaT

            if pd.api.types.is_datetime64_any_dtype(df_cleaned[column]):
                if df_cleaned[column].dt.tz is None:
                    try:
                        df_cleaned[column] = df_cleaned[column].dt.tz_localize('UTC', ambiguous='NaT', nonexistent='NaT')
                    except Exception as e_tz: # Falls Mehrdeutigkeit nicht mit NaT lösbar ist
                        logging.error(f"Fehler bei tz_localize für Column {column}: {e_tz}. Zeitstempel könnten inkonsistent sein.")
                        df_cleaned[column] = pd.to_datetime(df_cleaned[column], errors='coerce').dt.tz_localize(None).dt.tz_localize('UTC', ambiguous='NaT', nonexistent='NaT')
                elif str(df_cleaned[column].dt.tz) != 'UTC':
                    df_cleaned[column] = df_cleaned[column].dt.tz_convert('UTC')
            else:
                logging.warning(f"Column {column} konnte nicht in ein datetime-Format konvertiert werden. Use NaT.")
                df_cleaned[column] = pd.NaT
        else:
            logging.warning(f"Benötigte Zeit-Column {column} fehlt. Column wird mit pd.NaT erstellt.")
            df_cleaned[column] = pd.NaT


    # --- Schritt 2: Behandlung fehlender Werte (NaN/NaT) in wichtigen Columns ---
    necessary_columns = ['firstseen', 'lastseen', 'icao24', 'query_airport', 'flight_type']
    # Columns, welche NaN sein dürfen
    important_columns_features = ['callsign', 'departure_airport', 'arrival_airport']

    # Überprüfen, ob erforderliche Columns existieren
    missing_necc_columns_check = [s for s in necessary_columns if s not in df_cleaned.columns]
    if missing_necc_columns_check:
        logging.error(f"Essentielle Columns fehlen und können nicht verarbeitet werden: {', '.join(missing_necc_columns_check)}.")
        df_cleaned = pd.DataFrame() # Leeren, um weitere Fehler zu vermeiden
    else:
        # Entferne Zeilen, wo erforderliche Columns NaN/NaT sind
        initial_rows = len(df_cleaned)
        df_cleaned.dropna(subset=necessary_columns, inplace=True)
        rows_after_dropna = len(df_cleaned)
        if initial_rows > 0 and initial_rows > rows_after_dropna :
            logging.info(f"{initial_rows - rows_after_dropna} Zeilen ({ (initial_rows - rows_after_dropna) / initial_rows * 100:.1f}%) wegen fehlender Werte in kritischen Columns {necessary_columns} entfernt.")
        elif initial_rows == rows_after_dropna and initial_rows > 0:
             logging.info(f"Keine Zeilen aufgrund fehlender Werte in erforderlichen Columns {necessary_columns} entfernt.")

        # Überprüfe wichtige Feature-Columns
        for column in important_columns_features:
             if column not in df_cleaned.columns:
                 logging.warning(f"Wichtige Column '{column}' fehlt. Wird mit None hinzugefügt.")
                 df_cleaned[column] = None
             else: # Prüfe auf fehlende Werte
                 missing_count = df_cleaned[column].isnull().sum()
                 if missing_count > 0 and not df_cleaned.empty:
                      logging.warning(f"Feature-Column '{column}' hat {missing_count} fehlende Werte ({missing_count / len(df_cleaned) * 100:.1f}%).")


    # --- Schritt 3: Konsistenzprüfung der Zeitstempel ---
    if 'firstseen' in df_cleaned.columns and 'lastseen' in df_cleaned.columns and not df_cleaned.empty:
        # Sicherstellen, dass die Columns auch wirklich datetime sind nach allen Konvertierungen
        if pd.api.types.is_datetime64_any_dtype(df_cleaned['firstseen']) and \
           pd.api.types.is_datetime64_any_dtype(df_cleaned['lastseen']):
            invalid_time_order = df_cleaned['lastseen'] < df_cleaned['firstseen']
            if invalid_time_order.any():
                num_invalid = invalid_time_order.sum()
                logging.warning(f"{num_invalid} Zeilen ({num_invalid / len(df_cleaned) * 100:.1f}%) haben 'lastseen' vor 'firstseen'. Diese werden entfernt.")
                df_cleaned = df_cleaned[~invalid_time_order].copy()
        else:
            logging.warning("Zeit-Konsistenzprüfung übersprungen, da 'firstseen' oder 'lastseen' keine gültigen Datumsformate haben.")

    # --- Schritt 4: Normalisierung von Columns ---
    string_columns_to_normalize = ['callsign', 'query_airport', 'departure_airport', 'arrival_airport', 'flight_type', 'icao24']
    for col in string_columns_to_normalize:
        if col in df_cleaned.columns and df_cleaned[col].dtype == 'object': # Nur auf Objekt-Columns anwenden
            original_nulls = df_cleaned[col].isnull().sum()
            # In String umwandeln, Whitespace entfernen, Grossbuchstaben
            df_cleaned[col] = df_cleaned[col].astype(str).str.strip().str.upper()
            # Standard-NaN-ähnliche Strings zu echten NaNs konvertieren
            df_cleaned.loc[df_cleaned[col].isin(['', 'NAN', 'NONE', 'N/A', 'NULL', 'NA', '<NA>', 'UNDEFINED', 'UNDEF']), col] = np.nan
            new_nulls = df_cleaned[col].isnull().sum()
            if new_nulls > original_nulls:
                 logging.info(f"In Column '{col}' wurden {new_nulls - original_nulls} leere/ungültige Strings zu NaN konvertiert.")
        elif col in df_cleaned.columns and df_cleaned[col].isnull().all() and df_cleaned[col].dtype == 'object':
            df_cleaned[col] = np.nan
            logging.info(f"Column '{col}' (nur None-Werte) wurde zu NaN konvertiert.")

    if df_cleaned.empty:
        logging.error("DataFrame ist nach der Bereinigung leer. Abbruch der Analyse.")
    else:
        logging.info(f"Datenbereinigung abgeschlossen. Verbleibende Datensätze: {len(df_cleaned)}")
        print("\n--- Erste 5 Zeilen nach Bereinigung ---");
        display(df_cleaned.head())
        print("\n--- Datentypen nach Bereinigung ---");
        display(df_cleaned.dtypes.to_frame('Datentyp'))

        buffer_info_b = io.StringIO()
        df_cleaned.info(buf=buffer_info_b)
        bereinigt_info = buffer_info_b.getvalue() # Für Anhang
        print("\n--- Info zu Non-Null Counts und Speicherbedarf (Bereinigt) ---");
        print(bereinigt_info)
        print("\n--- Deskriptive Statistik für numerische Columns (Bereinigt) ---")
        bereinigt_describe = df_cleaned.describe(include=np.number) # Für Anhang
        display(bereinigt_describe.style.format('{:.2f}'))
else:
    logging.error("Laden der Rohdaten fehlgeschlagen oder DataFrame war leer. Überspringe Bereinigung.")
    df_cleaned = pd.DataFrame()
# -

# ### 2.6 Feature Engineering
# Erstellung neuer, für die Analyse relevanter Columns basierend auf den bereinigten Daten.

# + tags=["scroll_output"]
if not df_cleaned.empty:
    logging.info("Start Feature Engineering.")
    df_final = df_cleaned.copy() # Arbeite mit einer Kopie des bereinigten DataFrames

    # --- 1. Netzwerksichtbarkeitsdauer ---
    duration_col = 'network_duration_minutes'
    # Sicherstellen, dass Columns existieren und im korrekten Format sind
    if 'firstseen' in df_final.columns and 'lastseen' in df_final.columns and \
       pd.api.types.is_datetime64_any_dtype(df_final['firstseen']) and \
       pd.api.types.is_datetime64_any_dtype(df_final['lastseen']):

        # Überprüfen auf konsistente Zeitzonen
        tz_first = df_final['firstseen'].dt.tz
        tz_last = df_final['lastseen'].dt.tz

        if (tz_first is not None and tz_last is not None and str(tz_first) == str(tz_last)) or \
           (tz_first is None and tz_last is None): # Falls beide naiv sind (sollte nicht passieren)
            time_diff = df_final['lastseen'] - df_final['firstseen']
            df_final[duration_col] = time_diff.dt.total_seconds() / 60

            # Behandlung von ungültigen Dauern
            min_plausible_duration = 0.1
            invalid_duration_mask = (df_final[duration_col] < min_plausible_duration) | (df_final[duration_col].isnull())
            num_invalid_before_set_nan = invalid_duration_mask.sum()

            df_final.loc[invalid_duration_mask, duration_col] = np.nan # Setze ungültige auf NaN
            num_invalid_after_set_nan = df_final[duration_col].isnull().sum()

            if num_invalid_after_set_nan > (num_invalid_before_set_nan - df_final[duration_col].isnull().sum()): # Logge nur, wenn neue NaNs gesetzt wurden
                 logging.warning(f"{num_invalid_after_set_nan - (num_invalid_before_set_nan - df_final[duration_col].isnull().sum())} Flüge hatten eine Dauer < {min_plausible_duration} Min und wurden auf NaN gesetzt.")

            valid_duration_count = df_final[duration_col].notna().sum()
            logging.info(f"'{duration_col}' berechnet. {valid_duration_count} gültige Werte ({valid_duration_count / len(df_final) * 100:.1f}%).")
        else:
             logging.error(f"Zeitzonen von 'firstseen' ({tz_first}) und 'lastseen' ({tz_last}) sind inkonsistent. '{duration_col}' wird auf NaN gesetzt.")
             df_final[duration_col] = np.nan
    else:
        logging.error(f"'{duration_col}' konnte nicht berechnet werden, da 'firstseen'/'lastseen' fehlen oder ungültiges Format haben. Column wird mit NaN gefüllt.")
        df_final[duration_col] = np.nan

    # --- 2. Airline Code ---
    airline_col = 'airline_code'
    if 'callsign' in df_final.columns:
        # Sicherstellen, dass 'callsign' ein String ist und nicht NaN
        df_final['callsign'] = df_final['callsign'].astype(str)
        # Bedingung für gültige Airline-Codes: nicht NaN, Länge >= 3, die ersten 3 Zeichen sind keine Zahlen und nicht generische Platzhalter
        condition = (
            df_final['callsign'].notna() &
            (df_final['callsign'].str.len() >= 3) &
            (~df_final['callsign'].str[:3].str.contains(r'\d', na=False)) & # Keine Ziffern in den ersten 3 Chars
            (~df_final['callsign'].str[:3].isin(['NON', 'NAN', 'N/A', 'UNK', 'UND', 'NONE', 'NULL']))
        )
        df_final[airline_col] = df_final['callsign'].str[:3].str.upper().where(condition, np.nan) # Ansonsten NaN

        valid_airline_count = df_final[airline_col].notna().sum()
        logging.info(f"'{airline_col}' (Approximation aus 'callsign') extrahiert. {valid_airline_count} gültige Codes ({valid_airline_count / len(df_final) * 100:.1f}%).")
    else:
        logging.warning(f"Column 'callsign' fehlt. '{airline_col}' kann nicht extrahiert werden. Column wird NaN gesetzt.")
        df_final[airline_col] = np.nan


    # --- 3. Fluglokalität (National/International) ---
    locality_col = 'locality'
    if 'departure_airport' in df_final.columns and 'arrival_airport' in df_final.columns:

        def determine_flight_locality(row):
            dep = row['departure_airport']
            arr = row['arrival_airport']

            dep_is_valid_str = isinstance(dep, str) and pd.notna(dep)
            arr_is_valid_str = isinstance(arr, str) and pd.notna(arr)
            dep_is_swiss = dep_is_valid_str and dep in SCHWEIZER_FLUGHAFEN
            arr_is_swiss = arr_is_valid_str and arr in SCHWEIZER_FLUGHAFEN

            if dep_is_swiss and arr_is_swiss: return 'National'
            elif (dep_is_swiss and arr_is_valid_str and not arr_is_swiss) or \
                 (arr_is_swiss and dep_is_valid_str and not dep_is_swiss): return 'International'
            # Fälle, wo ein Flughafen CH ist, der andere aber NaN (unvollständig)
            elif (dep_is_swiss and not arr_is_valid_str) or \
                 (arr_is_swiss and not dep_is_valid_str): return 'International (Unvollständig)'
            # Fälle, wo beide Flughäfen bekannt, aber keiner davon CH ist (z.B. Überflug, sollte durch query_airport nicht vorkommen)
            elif dep_is_valid_str and arr_is_valid_str and not dep_is_swiss and not arr_is_swiss: return 'Andere / Nicht-CH-Bezug'
            # Fälle, wo beide Flughäfen NaN sind
            elif not dep_is_valid_str and not arr_is_valid_str: return 'Unbekannt (Keine Route)'
            # Alle anderen denkbaren Kombinationen
            else: return 'Unbekannt (Sonstige)'

        df_final[locality_col] = df_final.apply(determine_flight_locality, axis=1)
        logging.info(f"'{locality_col}' (National/International/Andere) berechnet. Verteilung (Top 5):\n{df_final[locality_col].value_counts(normalize=True, dropna=False).round(3).head()}")
    else:
        logging.warning(f"Columns 'departure_airport' oder 'arrival_airport' fehlen. '{locality_col}' kann nicht berechnet werden. Column wird mit 'Unbekannt (Fehlende Columns)' gefüllt.")
        df_final[locality_col] = 'Unbekannt (Fehlende Columns)'


    # --- 4. Zeitliche Merkmale (Jahr, Monat, Wochentag) ---
    time_features_generated = False
    if 'firstseen' in df_final.columns and pd.api.types.is_datetime64_any_dtype(df_final['firstseen']):
         # Nur extrahieren, wenn es mindestens einen gültigen (nicht NaT) Zeitstempel gibt
         if df_final['firstseen'].notna().any():
             df_final['jahr'] = df_final['firstseen'].dt.year.astype('Int64') # Nullable Integer
             df_final['monat_nr'] = df_final['firstseen'].dt.month.astype('Int64')
             df_final['monat_name'] = df_final['firstseen'].dt.month_name()
             df_final['wochentag_nr'] = df_final['firstseen'].dt.dayofweek.astype('Int64') # Monday=0, Sunday=6
             df_final['wochentag_name'] = df_final['firstseen'].dt.day_name()
             df_final['stunde'] = df_final['firstseen'].dt.hour.astype('Int64') # Stunde des Tages
             df_final['quartal'] = df_final['firstseen'].dt.quarter.astype('Int64') # Quartal

             logging.info("Zeitliche Features ('jahr', 'monat_nr/name', 'wochentag_nr/name', 'stunde', 'quartal') extrahiert.")
             time_features_generated = True
         else:
             logging.warning("Column 'firstseen' enthält nur NaT-Werte. Wird NaN gesetzt.")
    else:
         logging.warning("Column 'firstseen' ungültig oder fehlt für Extraktion zeitlicher Features. Wird NaN gesetzt.")

    if not time_features_generated: # Wenn Features nicht generiert werden können
        for col_tf in ['jahr', 'monat_nr', 'monat_name', 'wochentag_nr', 'wochentag_name', 'stunde', 'quartal']:
            df_final[col_tf] = pd.NA if col_tf in ['jahr', 'monat_nr', 'wochentag_nr', 'stunde', 'quartal'] else None


    final_columns = list(df_final.columns)
    logging.info(f"Feature Engineering abgeschlossen. Finale Columns: {final_columns}")
    print("\n--- Inspektion der Daten nach Feature Engineering (Erste 5 Zeilen) ---");
    display(df_final.head())
    print("\n--- Datentypen ---");
    display(df_final.dtypes.to_frame('Datentyp'))

    # Info und Describe für den Anhang
    buffer_info_final = io.StringIO()
    df_final.info(buf=buffer_info_final)
    final_info = buffer_info_final.getvalue() # Für Anhang
    final_describe = df_final.describe(include='all') # Für Anhang
else:
    logging.error("Bereinigter DataFrame ist leer.")
    df_final = pd.DataFrame()
# -

# ## 3. Schritt: Analyse der Daten (Analyze Data)
#
# **Ziel:** Anwendung primär deskriptiver statistischer Methoden sowie exemplarisch **prädiktiver Verfahren** auf die vorbereiteten Daten (`df_final`), um Muster, Trends und mögliche zukünftige Entwicklungen zu identifizieren und die KAQs aus Schritt 1 zu beantworten (Marr, 2020).
#
# **Hinweis:** Die tiefere Interpretation und Synthese zu handlungsrelevanten Insights erfolgt in Schritt 5.

# ### 3.1 KAQ 1: Entwicklung und Verteilung des gesamten Flugverkehrsaufkommens

# + tags=["scroll_output"]
beobachtungen_dict = {}

if not df_final.empty and 'query_airport' in df_final.columns:
    start_year_data = df_final['jahr'].min() if 'jahr' in df_final.columns and df_final['jahr'].notna().any() else "N/A"
    end_year_data = df_final['jahr'].max() if 'jahr' in df_final.columns and df_final['jahr'].notna().any() else "N/A"

    total_flights_final = len(df_final)
    print(f"**Gesamtzahl analysierter Flugdatensätze (nach Bereinigung & FE, {start_year_data}-{end_year_data}): {total_flights_final:,}**\n")
    print(f"--- Beobachtung: Verkehrsaufkommen pro abgefragtem Flughafen (Gesamtzeitraum {start_year_data}-{end_year_data}) ---")
    # Filtere auf zu analysierende Flughäfen
    relevant_airports_in_data = [ap for ap in FLUGHAFEN_ZU_ANALYSIEREN if ap in df_final['query_airport'].unique()]

    if relevant_airports_in_data:
        airport_counts = df_final[df_final['query_airport'].isin(relevant_airports_in_data)]['query_airport'] \
                            .value_counts().to_frame('Anzahl Flüge')
        if not airport_counts.empty:
            total_analyzed_flights_in_scope = airport_counts['Anzahl Flüge'].sum()
            if total_analyzed_flights_in_scope > 0:
                airport_counts['Anteil (%)'] = (airport_counts['Anzahl Flüge'] / total_analyzed_flights_in_scope * 100).round(1)
            else:
                airport_counts['Anteil (%)'] = 0.0

            airport_counts.index.name = "Flughafen (ICAO)"
            # Füge Komplettnamen für Flughafen hinzu
            airport_counts['Flughafen Name'] = airport_counts.index.map(FLUGHAFEN_MAP)
            airport_counts = airport_counts[['Flughafen Name', 'Anzahl Flüge', 'Anteil (%)']] # Columnsreihenfolge
            # Gesamt Analysiert
            airport_counts.loc['Gesamt Analysiert'] = airport_counts.sum(numeric_only=True)
            # Prozentanteil für Gesamt korrigieren (Summe der Einzelanteile)
            if total_analyzed_flights_in_scope > 0 :
                sum_of_percentages = airport_counts['Anteil (%)'][:-1].sum()
                clipped_sum = np.clip(sum_of_percentages, None, 100.0)
                rounded_clipped_sum = np.round(clipped_sum,1)
                airport_counts.loc['Gesamt Analysiert', 'Anteil (%)'] = rounded_clipped_sum
            else:
                 airport_counts.loc['Gesamt Analysiert', 'Anteil (%)'] = 0.0

            airport_counts.loc['Gesamt Analysiert', 'Flughafen Name'] = 'Gesamt Analysiert'

            display(airport_counts.style.format({'Anzahl Flüge': '{:,.0f}', 'Anteil (%)': '{:.1f}%'}))

            if not airport_counts.drop('Gesamt Analysiert', errors='ignore').empty:
                top_airport_icao = airport_counts.drop('Gesamt Analysiert', errors='ignore').index[0]
                top_airport_name = airport_counts.loc[top_airport_icao, 'Flughafen Name']
                top_share = airport_counts.loc[top_airport_icao, 'Anteil (%)']
                top_count = airport_counts.loc[top_airport_icao, 'Anzahl Flüge']
                beobachtung_kaq1_text = f"{top_airport_name} ({top_airport_icao}) war der verkehrsreichste der analysierten Flughäfen mit {top_count:,.0f} Flügen ({top_share:.1f}% des Volumens der analysierten Flughäfen)."
                print(f"\nBeobachtung KAQ1 (Verteilung): {beobachtung_kaq1_text}")
                beobachtungen_dict['KAQ1_Verteilung'] = beobachtung_kaq1_text
            else:
                print("Keine Daten für die zu analysierenden Flughäfen in den Top-Counts gefunden.")

        else:
            print("Keine Daten für die zu analysierenden Flughäfen gefunden, um Verkehrsaufkommen zu zählen.")
    else:
        logging.warning("Keiner der zu analysierenden Flughäfen (FLUGHAFEN_ZU_ANALYSIEREN) wurde in der Column 'query_airport' des finalen DataFrames gefunden.")
        print("Keine der zu analysierenden Flughäfen im Datensatz gefunden.")

else:
    logging.warning("KAQ1 Analyse (Verkehrsaufkommen) übersprungen.")
    print("KAQ1 Analyse übersprungen: Keine Daten.")
# -

# ### 3.2 Zeitliche Entwicklung (Jährlich und Monatlich) am Beispiel des Flughafens Zürich

# + tags=["scroll_output"]
if not df_final.empty and 'firstseen' in df_final.columns and \
   'query_airport' in df_final.columns and 'jahr' in df_final.columns and \
   FLUGHAFEN_ZU_ANALYSIEREN and 'airport_counts' in locals() and not airport_counts.drop('Gesamt Analysiert', errors='ignore').empty :

    # Bestimme den Primärflughafen aus der vorherigen Analyse (airport_counts)
    valid_airport_counts = airport_counts.drop('Gesamt Analysiert', errors='ignore')
    if not valid_airport_counts.empty:
        target_airport_trend_icao = valid_airport_counts.index[0] # ICAO des verkehrsreichsten Flughafens
        target_airport_trend_name = valid_airport_counts.iloc[0]['Flughafen Name']
        print(f"--- Beobachtung: Jährlicher Verkehrstrend für {target_airport_trend_name} ({target_airport_trend_icao}) ---")

        # Filtere Daten für den Ziel-Flughafen
        df_target_airport = df_final[df_final['query_airport'] == target_airport_trend_icao].copy()

        if not df_target_airport.empty and pd.api.types.is_numeric_dtype(df_target_airport['jahr']) and df_target_airport['jahr'].notna().any():
            yearly_counts = df_target_airport.groupby('jahr').size().to_frame('Anzahl Flüge')
            # Sicherstellen, dass der Index sortiert ist für korrekte pct_change Berechnung
            yearly_counts.sort_index(inplace=True)

            if not yearly_counts.empty:
                yearly_counts['Vorjahresveränderung (%)'] = yearly_counts['Anzahl Flüge'].pct_change() * 100
                display(yearly_counts.style.format({'Anzahl Flüge': '{:,.0f}', 'Vorjahresveränderung (%)': '{:+.1f}%'}))

                # Plot für jährliche Entwicklung
                fig_yearly, ax_yearly = plt.subplots(figsize=(10, 5)) # Etwas breiter für mehr Jahre
                yearly_counts['Anzahl Flüge'].plot(kind='bar', ax=ax_yearly, color=IBCS_SCHWARZ, legend=None, width=0.8)
                ax_yearly.set_title(f'Jährliches Flugaufkommen {target_airport_trend_name} ({target_airport_trend_icao})', fontsize=12, fontweight='bold', loc='left')
                ax_yearly.set_xlabel('Jahr', fontsize=10)
                ax_yearly.set_ylabel('Anzahl Flüge', fontsize=10)
                ax_yearly.yaxis.set_major_formatter(mtick.FuncFormatter(lambda x, _: '{:,.0f}'.format(x)))
                ax_yearly.tick_params(axis='x', rotation=45, labelsize=9)
                ax_yearly.tick_params(axis='y', labelsize=9)
                # IBCS: Achsen hervorheben
                ax_yearly.spines['bottom'].set_color(IBCS_SCHWARZ)
                ax_yearly.spines['bottom'].set_linewidth(1.5)

                plt.tight_layout()
                plt.show()

                # Beobachtung für Management Summary
                peak_year = yearly_counts['Anzahl Flüge'].idxmax()
                peak_flights = yearly_counts['Anzahl Flüge'].max()
                trough_year = yearly_counts['Anzahl Flüge'].idxmin() # Tiefpunkt
                trough_flights = yearly_counts['Anzahl Flüge'].min()
                beobachtung_kaq1_trend_text = f"Am {target_airport_trend_name} erreichte das Aufkommen {peak_year} mit {peak_flights:,.0f} Flügen seinen Höhepunkt und {trough_year} mit {trough_flights:,.0f} seinen Tiefpunkt im Analysezeitraum."
                print(f"Beobachtung KAQ1 (Trend {target_airport_trend_name}): {beobachtung_kaq1_trend_text}")
                beobachtungen_dict[f'KAQ1_Trend_{target_airport_trend_icao}'] = beobachtung_kaq1_trend_text
            else:
                print(f"Keine jährlichen Daten für {target_airport_trend_name} gefunden.")

            # Monatliche Entwicklung für die letzten zwei Jahre im Datensatz
            available_years = sorted(df_target_airport['jahr'].dropna().unique().astype(int))
            if len(available_years) >= 2:
                last_two_full_years = available_years[-2:]
                print(f"\n--- Beobachtung: Monatlicher Verkehrstrend für {target_airport_trend_name} (Jahre: {', '.join(map(str, last_two_full_years))}) ---")
                df_target_last_years = df_target_airport[df_target_airport['jahr'].isin(last_two_full_years)].copy()

                if not df_target_last_years.empty and \
                   pd.api.types.is_datetime64_any_dtype(df_target_last_years['firstseen']) and \
                   df_target_last_years['firstseen'].notna().any():

                    # Resample erfordert einen DatetimeIndex
                    df_target_last_years.set_index('firstseen', inplace=True)
                    # 'ME' für Monatsende (Month End frequency)
                    monthly_counts_detail = df_target_last_years.resample('ME').size().to_frame('Anzahl Flüge')

                    if not monthly_counts_detail.empty:
                        # Index für bessere Lesbarkeit formatieren
                        monthly_counts_detail.index = monthly_counts_detail.index.strftime('%Y-%m (%B)')
                        monthly_counts_detail.index.name = 'Monat'
                        display(monthly_counts_detail.style.format({'Anzahl Flüge': '{:,.0f}'}))
                    else:
                        print(f"Keine monatlichen Daten für die Jahre {', '.join(map(str, last_two_full_years))} für {target_airport_trend_name} gefunden.")
                else:
                    print(f"Keine ausreichenden Daten für monatlichen Trend der Jahre {', '.join(map(str, last_two_full_years))} ({target_airport_trend_name}).")
            elif len(available_years) == 1:
                 print(f"\nNur ein Jahr ({available_years[0]}) im Datensatz für {target_airport_trend_name} vorhanden. Zeige monatlichen Trend für dieses Jahr.")
                 df_target_one_year = df_target_airport[df_target_airport['jahr'] == available_years[0]].copy()
                 if not df_target_one_year.empty and pd.api.types.is_datetime64_any_dtype(df_target_one_year['firstseen']) and df_target_one_year['firstseen'].notna().any():
                    df_target_one_year.set_index('firstseen', inplace=True)
                    monthly_counts_one_year = df_target_one_year.resample('ME').size().to_frame('Anzahl Flüge')
                    if not monthly_counts_one_year.empty:
                        monthly_counts_one_year.index = monthly_counts_one_year.index.strftime('%Y-%m (%B)')
                        monthly_counts_one_year.index.name = 'Monat'
                        display(monthly_counts_one_year.style.format({'Anzahl Flüge': '{:,.0f}'}))
                    else: print(f"Keine monatlichen Daten für {available_years[0]} gefunden.")
                 else: print(f"Keine ausreichenden Daten für monatlichen Trend ({available_years[0]}) für {target_airport_trend_name}.")

            else:
                print(f"Nicht genügend Jahre im Datensatz für {target_airport_trend_name}, um monatliche Trends anzuzeigen.")
        else:
            print(f"Keine ausreichenden Daten ('jahr' Column fehlt oder ist leer) für jährliche Trendanalyse von {target_airport_trend_name}.")
    else:
        print(f"Primärflughafen für Trendanalyse konnte nicht bestimmt werden (airport_counts ist leer nach Filterung).")
else:
    print("Überspringe zeitliche Trendanalyse: Fehlende Daten, Konfiguration oder `airport_counts` nicht verfügbar.")
# -

# ### 3.3 KAQ 2: Aktivität der Fluggesellschaften
# (Code aus vorheriger Version für 3.3, angepasst an `df_final`)

# + tags=["scroll_output"]
airline_col_kaq2 = 'airline_code'
start_year_data_kaq2 = df_final['jahr'].min() if 'jahr' in df_final.columns and df_final['jahr'].notna().any() else "N/A"
end_year_data_kaq2 = df_final['jahr'].max() if 'jahr' in df_final.columns and df_final['jahr'].notna().any() else "N/A"


if not df_final.empty and airline_col_kaq2 in df_final.columns:
    print(f"\n--- Beobachtung: Top 15 Airline-Codes (Gesamter Schweizer Luftraum der Analyse, Approximation, {start_year_data_kaq2}-{end_year_data_kaq2}) ---")
    # Betrachte nur Flüge, die einen Bezug zu den SCHWEIZER_FLUGHAFEN haben, um konsistent zu sein
    df_swiss_related_flights = df_final[df_final['query_airport'].isin(SCHWEIZER_FLUGHAFEN)]
    df_valid_airlines_overall = df_swiss_related_flights.dropna(subset=[airline_col_kaq2])

    if not df_valid_airlines_overall.empty:
        top_airlines_gesamt = df_valid_airlines_overall[airline_col_kaq2].value_counts().head(15).to_frame('Anzahl Flüge')
        total_valid_airline_flights_overall = len(df_valid_airlines_overall) # Gesamtzahl der Flüge mit gültigem Airline-Code

        if total_valid_airline_flights_overall > 0:
            top_airlines_gesamt['Anteil an Flügen mit Airline-Code (%)'] = (top_airlines_gesamt['Anzahl Flüge'] / total_valid_airline_flights_overall * 100).round(1)
        else:
            top_airlines_gesamt['Anteil an Flügen mit Airline-Code (%)'] = 0.0
        top_airlines_gesamt.index.name = 'Airline Code (Approximation)'
        display(top_airlines_gesamt.style.format({'Anzahl Flüge': '{:,.0f}', 'Anteil an Flügen mit Airline-Code (%)': '{:.1f}%'}))

        if not top_airlines_gesamt.empty:
            top_airline_overall_code = top_airlines_gesamt.index[0]
            top_airline_overall_share = top_airlines_gesamt.iloc[0]['Anteil an Flügen mit Airline-Code (%)']
            top_airline_overall_count = top_airlines_gesamt.iloc[0]['Anzahl Flüge']
            beobachtung_kaq2_overall_text = f"Airline-Code '{top_airline_overall_code}' war im analysierten Schweizer Luftraum am häufigsten mit {top_airline_overall_count:,.0f} Flügen ({top_airline_overall_share:.1f}% aller Flüge mit identifizierbarem Airline-Code)."
            print(f"\nBeobachtung KAQ2 (Gesamt CH): {beobachtung_kaq2_overall_text}")
            beobachtungen_dict['KAQ2_Gesamt_CH'] = beobachtung_kaq2_overall_text
    else:
        print("Keine Flüge mit gültigen Airline-Codes im relevanten Schweizer Luftraum gefunden.")

    # Analyse pro Primärflughafen
    if FLUGHAFEN_ZU_ANALYSIEREN and 'query_airport' in df_final.columns and \
       'airport_counts' in locals() and not airport_counts.drop('Gesamt Analysiert', errors='ignore').empty:

        valid_airport_counts_kaq2 = airport_counts.drop('Gesamt Analysiert', errors='ignore')
        if not valid_airport_counts_kaq2.empty:
            primar_flughafen_airline_icao = valid_airport_counts_kaq2.index[0]
            primar_flughafen_airline_name = FLUGHAFEN_MAP.get(primar_flughafen_airline_icao, primar_flughafen_airline_icao)

            print(f"\n--- Beobachtung: Top 10 Airline-Codes für Primärflughafen {primar_flughafen_airline_name} ({primar_flughafen_airline_icao}) ---")
            # Filtere df_final auf den Primärflughafen und gültige Airline-Codes
            df_primar_flughafen_ops = df_final[
                (df_final['query_airport'] == primar_flughafen_airline_icao) &
                (df_final[airline_col_kaq2].notna())
            ]

            if not df_primar_flughafen_ops.empty:
                top_airlines_primar = df_primar_flughafen_ops[airline_col_kaq2].value_counts().head(10).to_frame('Anzahl Flüge')
                total_valid_primar_flights = len(df_primar_flughafen_ops) # Flüge am PrimärFH mit Airline Code

                if total_valid_primar_flights > 0:
                    top_airlines_primar['Anteil am FH mit Airline-Code (%)'] = (top_airlines_primar['Anzahl Flüge'] / total_valid_primar_flights * 100).round(1)
                else:
                    top_airlines_primar['Anteil am FH mit Airline-Code (%)'] = 0.0
                top_airlines_primar.index.name = 'Airline Code (Approximation)'
                display(top_airlines_primar.style.format({'Anzahl Flüge': '{:,.0f}', 'Anteil am FH mit Airline-Code (%)': '{:.1f}%'}))

                if not top_airlines_primar.empty:
                    top_airline_primar_code = top_airlines_primar.index[0]
                    top_airline_primar_share = top_airlines_primar.iloc[0]['Anteil am FH mit Airline-Code (%)']
                    top_airline_primar_count = top_airlines_primar.iloc[0]['Anzahl Flüge']
                    beobachtung_kaq2_primar_text = f"Am Flughafen {primar_flughafen_airline_name} war Airline-Code '{top_airline_primar_code}' am häufigsten ({top_airline_primar_count:,.0f} Flüge, {top_airline_primar_share:.1f}% der Flüge mit Airline-Code an diesem FH)."
                    print(f"\nBeobachtung KAQ2 ({primar_flughafen_airline_name}): {beobachtung_kaq2_primar_text}")
                    beobachtungen_dict[f'KAQ2_{primar_flughafen_airline_icao}'] = beobachtung_kaq2_primar_text
            else:
                print(f"Keine Flüge mit gültigen Airline-Codes für {primar_flughafen_airline_name} gefunden.")
        else:
            print("Primärflughafen für Airline-Analyse konnte nicht bestimmt werden.")
else:
    print("\nÜberspringe Airline-Analyse (KAQ2): DataFrame leer oder 'airline_code' Column fehlt.")
# -

# ### 3.4 KAQ 3: Routenanalyse (Top Herkünfte/Ziele)
# Routenanalyse mit Top Herkünften und Zielen der Flüge.

# + tags=["scroll_output"]
required_cols_kaq3 = ['query_airport', 'flight_type', 'departure_airport', 'arrival_airport', 'jahr']
start_year_data_kaq3 = df_final['jahr'].min() if 'jahr' in df_final.columns and df_final['jahr'].notna().any() else "N/A"
end_year_data_kaq3 = df_final['jahr'].max() if 'jahr' in df_final.columns and df_final['jahr'].notna().any() else "N/A"


if not df_final.empty and all(c in df_final.columns for c in required_cols_kaq3):
    print(f"\n--- Beobachtung: Top 10 Routen pro Flughafen (Gesamtzeitraum {start_year_data_kaq3}-{end_year_data_kaq3}) ---")
    beobachtungen_kaq3_list = [] # Beobachtungen für Management Summary

    # Iteriere nur über die Flughäfen, die auch im Datensatz vorhanden sind und analysiert werden sollen
    active_query_airports = [ap for ap in FLUGHAFEN_ZU_ANALYSIEREN if ap in df_final['query_airport'].unique()]

    for flughafen_icao_kaq3 in active_query_airports:
        flughafen_name_kaq3 = FLUGHAFEN_MAP.get(flughafen_icao_kaq3, flughafen_icao_kaq3)
        print(f"\n**Analyse für {flughafen_name_kaq3} ({flughafen_icao_kaq3}):**")

        # Filtere DataFrame für aktuellen Flughafen
        df_flughafen_spezifisch = df_final[df_final['query_airport'] == flughafen_icao_kaq3]

        if df_flughafen_spezifisch.empty:
            print(f"  Keine Daten für {flughafen_name_kaq3} im DataFrame.")
            continue

        # Arrivals analysieren
        ankuenfte = df_flughafen_spezifisch[df_flughafen_spezifisch['flight_type'] == 'ARRIVAL']
        if not ankuenfte.empty and 'departure_airport' in ankuenfte.columns:
            top_herkuenfte = ankuenfte['departure_airport'].dropna().value_counts().head(10).to_frame('Ankünfte von')
            if not top_herkuenfte.empty:
                 top_herkuenfte.index.name='Herkunft (ICAO)'
                 print(f"  Top Herkunftsflughäfen (Ankünfte in {flughafen_icao_kaq3}):")
                 display(top_herkuenfte.style.format('{:,.0f}'))
                 # Für Management Summary: Top-Herkunft
                 top_dep_icao = top_herkuenfte.index[0]
                 top_dep_name = FLUGHAFEN_MAP.get(top_dep_icao, top_dep_icao) # Name oder ICAO, falls nicht in Map
                 top_dep_count = top_herkuenfte.iloc[0,0]
                 beobachtungen_kaq3_list.append(f"Für {flughafen_name_kaq3} war {top_dep_name} ({top_dep_icao}) mit {top_dep_count:,.0f} Flügen die häufigste Herkunft.")
            else:
                 print(f"  Keine gültigen Herkunftsdaten (departure_airport) für Ankünfte in {flughafen_icao_kaq3} gefunden.")
        else:
            print(f"  Keine Ankunftsdaten ('ARRIVAL') für {flughafen_name_kaq3} oder 'departure_airport' Column fehlt.")

        # Abflüge analysieren
        abfluege = df_flughafen_spezifisch[df_flughafen_spezifisch['flight_type'] == 'DEPARTURE']
        if not abfluege.empty and 'arrival_airport' in abfluege.columns:
            top_ziele = abfluege['arrival_airport'].dropna().value_counts().head(10).to_frame('Abflüge nach')
            if not top_ziele.empty:
                top_ziele.index.name='Ziel (ICAO)'
                print(f"\n  Top Zielflughäfen (Abflüge von {flughafen_icao_kaq3}):")
                display(top_ziele.style.format('{:,.0f}'))
                # Für Management Summary: Top-Ziel
                top_arr_icao = top_ziele.index[0]
                top_arr_name = FLUGHAFEN_MAP.get(top_arr_icao, top_arr_icao)
                top_arr_count = top_ziele.iloc[0,0]
                beobachtungen_kaq3_list.append(f"Von {flughafen_name_kaq3} war {top_arr_name} ({top_arr_icao}) mit {top_arr_count:,.0f} Flügen das häufigste Ziel.")
            else:
                print(f"  Keine gültigen Zieldaten (arrival_airport) für Abflüge von {flughafen_icao_kaq3} gefunden.")
        else:
            print(f"  Keine Abflugsdaten ('DEPARTURE') für {flughafen_name_kaq3} oder 'arrival_airport' Column fehlt.")

    # Zusammenfassung für Management Summary
    if beobachtungen_kaq3_list:
        print("\n--- Zusammenfassung erste Routen-Beobachtungen (KAQ3) ---")
        for b_idx, b_text in enumerate(beobachtungen_kaq3_list[:min(len(beobachtungen_kaq3_list), 4)]): # Zeige max. 4
            print(f"* {b_text}")
            beobachtungen_dict[f'KAQ3_Route_{b_idx}'] = b_text # Speichere für später
    else:
        print("\nKeine zusammenfassenden Routen-Beobachtungen generiert.")
else:
    print("\nÜberspringe Routenanalyse (KAQ3): Erforderliche Columns fehlen oder DataFrame ist leer.")
# -

# ### 3.5 KAQ 4: Segmentierung nach Fluglokalität

# + tags=["scroll_output"]
locality_col_kaq4 = 'locality' # Aus Feature Engineering
start_year_data_kaq4 = df_final['jahr'].min() if 'jahr' in df_final.columns and df_final['jahr'].notna().any() else "N/A"
end_year_data_kaq4 = df_final['jahr'].max() if 'jahr' in df_final.columns and df_final['jahr'].notna().any() else "N/A"

if not df_final.empty and locality_col_kaq4 in df_final.columns:
    print(f"\n--- Beobachtung: Nationaler vs. Internationaler Flugverkehr (Gesamt, basierend auf Schweizer Flügen, {start_year_data_kaq4}-{end_year_data_kaq4}) ---")
    # Betrachte nur Flüge, die einen Bezug zu den SCHWEIZER_FLUGHAFEN haben
    df_swiss_flights_locality = df_final[df_final['query_airport'].isin(SCHWEIZER_FLUGHAFEN)]

    if not df_swiss_flights_locality.empty:
        lokalitaet_gesamt = df_swiss_flights_locality[locality_col_kaq4].value_counts(dropna=False).to_frame('Anzahl Flüge')
        total_swiss_flights_for_locality = len(df_swiss_flights_locality) # Gesamtzahl der Flüge mit CH-Bezug

        if total_swiss_flights_for_locality > 0:
            lokalitaet_gesamt['Anteil (%)'] = (lokalitaet_gesamt['Anzahl Flüge'] / total_swiss_flights_for_locality * 100).round(1)
        else:
            lokalitaet_gesamt['Anteil (%)'] = 0.0
        lokalitaet_gesamt.index.name = 'Lokalität (Abgeleitet)'

        # Gewünschte Reihenfolge für die Anzeige
        # (np.nan wird von value_counts(dropna=False) als eigener Wert behandelt, falls es NaNs in 'locality' gibt)
        desired_order = ['International', 'National', 'International (Unvollständig)',
                         'Andere / Nicht-CH-Bezug', 'Unbekannt (Keine Route)',
                         'Unbekannt (Fehlende Columns)', 'Unbekannt (Sonstige)', np.nan]
        # Reindex, um die gewünschte Reihenfolge zu erhalten und fehlende Kategorien mit 0 zu füllen
        lokalitaet_gesamt = lokalitaet_gesamt.reindex([cat for cat in desired_order if cat in lokalitaet_gesamt.index or pd.isna(cat)], fill_value=0)
        lokalitaet_gesamt.rename(index={np.nan: 'Unbekannt (NaN in Locality)'}, inplace=True)

        # Gesamtzeile
        lokalitaet_gesamt.loc['Gesamt'] = lokalitaet_gesamt.sum(numeric_only=True)
        if total_swiss_flights_for_locality > 0:
            if len(lokalitaet_gesamt) > 1:
                sum_of_individual_percentages = lokalitaet_gesamt['Anteil (%)'][:-1].sum()
                clipped_sum = np.clip(sum_of_individual_percentages, None,100.0)
                # Round the clipped sum
                final_total_percentage = np.round(clipped_sum, 1)
                lokalitaet_gesamt.loc['Gesamt', 'Anteil (%)'] = final_total_percentage
            else:
                # This case implies that 'lokalitaet_gesamt' only contains the 'Gesamt' row
                lokalitaet_gesamt.loc['Gesamt', 'Anteil (%)'] = lokalitaet_gesamt.iloc[0]['Anteil (%)']
        else:
            lokalitaet_gesamt.loc['Gesamt', 'Anteil (%)'] = 0.0

        display(lokalitaet_gesamt.style.format({'Anzahl Flüge': '{:,.0f}', 'Anteil (%)': '{:.1f}%'}))

        # Beobachtung für Management Summary
        international_share = lokalitaet_gesamt.loc['International', 'Anteil (%)'] if 'International' in lokalitaet_gesamt.index else 0
        national_share = lokalitaet_gesamt.loc['National', 'Anteil (%)'] if 'National' in lokalitaet_gesamt.index else 0
        beobachtung_kaq4_text = f"Der Flugverkehr mit Schweizer Bezug war primär 'International' (ca. {international_share:.1f}%), nationale Flüge machten ca. {national_share:.1f}% aus."
        print(f"\nBeobachtung KAQ4 (Gesamt CH-Bezug): {beobachtung_kaq4_text}")
        beobachtungen_dict['KAQ4_Gesamt'] = beobachtung_kaq4_text

        # Aufteilung pro Flughafen (Kreuztabelle)
        if 'query_airport' in df_swiss_flights_locality.columns and FLUGHAFEN_ZU_ANALYSIEREN:
            print("\n--- Beobachtung: Aufteilung Lokalität pro analysiertem Schweizer Flughafen ---")
            try:
                # Filtere auf FLUGHAFEN_ZU_ANALYSIEREN
                df_filtered_airports_locality = df_swiss_flights_locality[df_swiss_flights_locality['query_airport'].isin(FLUGHAFEN_ZU_ANALYSIEREN)]
                if not df_filtered_airports_locality.empty:
                    # Verwende lesbare Namen für die Zeilen der Cross-Table
                    airport_names_map_crosstab = df_filtered_airports_locality['query_airport'].map(lambda x: f"{FLUGHAFEN_MAP.get(x, x)} ({x})")

                    lokalitaet_pro_flughafen = pd.crosstab(
                        airport_names_map_crosstab,
                        df_filtered_airports_locality[locality_col_kaq4],
                        dropna=False # Zeige auch NaN-Kategorien in 'locality', falls vorhanden
                    )
                    # Umbenennen der NaN-Column, falls sie existiert
                    if np.nan in lokalitaet_pro_flughafen.columns:
                        lokalitaet_pro_flughafen.rename(columns={np.nan: 'Unbekannt (NaN in Locality)'}, inplace=True)


                    # Gesamtcolumn hinzufügen
                    lokalitaet_pro_flughafen['Gesamt Flüge pro FH'] = lokalitaet_pro_flughafen.sum(axis=1)
                    # Sortiere Columns gemäss 'desired_order' und füge 'Gesamt' am Ende hinzu
                    current_cols_ordered = [col for col in desired_order if col in lokalitaet_pro_flughafen.columns or (pd.isna(col) and 'Unbekannt (NaN in Locality)' in lokalitaet_pro_flughafen.columns) ]
                    # Ersetze pd.NA durch den umbenannten Columnsnamen für den Abgleich
                    current_cols_ordered = ['Unbekannt (NaN in Locality)' if pd.isna(c) else c for c in current_cols_ordered]
                    # Filtere Duplikate, falls 'Unbekannt (NaN in Locality)' doppelt wäre
                    seen = set()
                    current_cols_ordered_unique = [x for x in current_cols_ordered if not (x in seen or seen.add(x))]

                    final_col_order = [col for col in current_cols_ordered_unique if col in lokalitaet_pro_flughafen.columns] + ['Gesamt Flüge pro FH']
                    lokalitaet_pro_flughafen = lokalitaet_pro_flughafen.reindex(columns=final_col_order, fill_value=0)

                    display(lokalitaet_pro_flughafen.style.format('{:,.0f}'))
                else:
                    print("Keine Daten für ausgewählte Flughäfen zur Kreuztabellierung der Lokalität gefunden.")
            except Exception as e_crosstab:
                logging.error(f"Fehler bei Erstellung der Kreuztabelle für Lokalität pro Flughafen: {e_crosstab}")
    else:
        print("\nKeine Flüge mit Bezug zu Schweizer Flughäfen für Lokalitätsanalyse gefunden.")
else:
    print("\nÜberspringe Lokalitätsanalyse (KAQ4): DataFrame leer oder 'locality' Column fehlt.")
# -

# ### 3.6 KAQ 5: Analyse der Netzwerksichtbarkeitsdauer

# + tags=["scroll_output"]
duration_col_kaq5 = 'network_duration_minutes' # Aus Feature Engineering
start_year_data_kaq5 = df_final['jahr'].min() if 'jahr' in df_final.columns and df_final['jahr'].notna().any() else "N/A"
end_year_data_kaq5 = df_final['jahr'].max() if 'jahr' in df_final.columns and df_final['jahr'].notna().any() else "N/A"

if not df_final.empty and duration_col_kaq5 in df_final.columns:
    print(f"\n--- Beobachtung: Analyse Netzwerksichtbarkeitsdauer ('{duration_col_kaq5}', {start_year_data_kaq5}-{end_year_data_kaq5}) ---")

    # Sicherstellen, dass die Column numerisch ist und gültige Werte enthält
    if pd.api.types.is_numeric_dtype(df_final[duration_col_kaq5]) and df_final[duration_col_kaq5].notna().any():
        df_valid_duration_all = df_final.dropna(subset=[duration_col_kaq5]) # Nur Zeilen mit gültiger Dauer

        print(f"\n**Deskriptive Statistik für '{duration_col_kaq5}' (Alle gültigen Werte, n={len(df_valid_duration_all):,}):**")
        stats_all_duration = df_valid_duration_all[duration_col_kaq5].describe()
        display(stats_all_duration.to_frame('Dauer (Minuten)').style.format('{:.1f}'))

        median_dauer_all = stats_all_duration['50%']
        mean_dauer_all = stats_all_duration['mean']
        beobachtung_kaq5_stats_all_text = f"Median der Netzwerksichtbarkeitsdauer (alle gültigen Flüge): {median_dauer_all:.1f} Min (Durchschnitt: {mean_dauer_all:.1f} Min)."
        print(f"\nBeobachtung KAQ5 (Statistik, alle): {beobachtung_kaq5_stats_all_text}")
        beobachtungen_dict['KAQ5_Stats_All'] = beobachtung_kaq5_stats_all_text

        # Filterung auf einen plausiblen Bereich für detailliertere Analyse (z.B. Ausreisser entfernen)
        # Z.B. Flüge zwischen 1 Minute und 20 Stunden (1200 Minuten)
        min_dauer_filter, max_dauer_filter = 1, 20 * 60
        df_gefilterte_dauer = df_valid_duration_all[
            (df_valid_duration_all[duration_col_kaq5] >= min_dauer_filter) &
            (df_valid_duration_all[duration_col_kaq5] <= max_dauer_filter)
        ].copy()

        if not df_gefilterte_dauer.empty:
            num_filtered = len(df_gefilterte_dauer)
            num_excluded = len(df_valid_duration_all) - num_filtered
            print(f"\n**Deskriptive Statistik (Gefiltert: {min_dauer_filter} Min - {max_dauer_filter/60:.0f} Std, n={num_filtered:,}, {num_excluded:,} ausgeschlossen):**")
            stats_filtered_duration = df_gefilterte_dauer[duration_col_kaq5].describe()
            display(stats_filtered_duration.to_frame('Dauer (Minuten)').style.format('{:.1f}'))

            median_dauer_filt = stats_filtered_duration['50%']
            mean_dauer_filt = stats_filtered_duration['mean']
            beobachtung_kaq5_stats_filt_text = f"Median der Netzwerksichtbarkeitsdauer (gefiltert {min_dauer_filter}min-{max_dauer_filter/60:.0f}h): {median_dauer_filt:.1f} Min (Durchschnitt: {mean_dauer_filt:.1f} Min)."
            print(f"\nBeobachtung KAQ5 (Statistik, gefiltert): {beobachtung_kaq5_stats_filt_text}")
            beobachtungen_dict['KAQ5_Stats_Filtered'] = beobachtung_kaq5_stats_filt_text

            # Durchschnittliche Dauer pro Flughafen
            if 'query_airport' in df_gefilterte_dauer.columns and FLUGHAFEN_ZU_ANALYSIEREN:
                 relevant_airports_for_duration = [ap for ap in FLUGHAFEN_ZU_ANALYSIEREN if ap in df_gefilterte_dauer['query_airport'].unique()]
                 if relevant_airports_for_duration:
                     print(f"\n**Beobachtung: Durchschnittliche und mediane Dauer pro Flughafen:**")
                     avg_dauer_pro_fh = df_gefilterte_dauer[df_gefilterte_dauer['query_airport'].isin(relevant_airports_for_duration)] \
                                         .groupby('query_airport')[duration_col_kaq5].agg(['mean', 'median', 'count'])
                     avg_dauer_pro_fh.columns = ['Ø Dauer (Min)', 'Median Dauer (Min)', 'Anzahl Flüge (gefiltert)']
                     avg_dauer_pro_fh.index.name = 'Flughafen (ICAO)'
                     avg_dauer_pro_fh['Flughafen Name'] = avg_dauer_pro_fh.index.map(FLUGHAFEN_MAP) # Klarnamen hinzufügen
                     avg_dauer_pro_fh = avg_dauer_pro_fh[['Flughafen Name', 'Ø Dauer (Min)', 'Median Dauer (Min)', 'Anzahl Flüge (gefiltert)']] # Columnsreihenfolge

                     display(avg_dauer_pro_fh.sort_values('Ø Dauer (Min)', ascending=False)
                             .style.format({'Ø Dauer (Min)': '{:.1f}', 'Median Dauer (Min)': '{:.1f}', 'Anzahl Flüge (gefiltert)': '{:,.0f}'}))

                     if len(avg_dauer_pro_fh) > 1: # Nur sinnvoll bei mehr als einem Flughafen
                          max_avg_fh_icao = avg_dauer_pro_fh['Ø Dauer (Min)'].idxmax()
                          min_avg_fh_icao = avg_dauer_pro_fh['Ø Dauer (Min)'].idxmin()
                          max_avg_fh_name = avg_dauer_pro_fh.loc[max_avg_fh_icao, 'Flughafen Name']
                          min_avg_fh_name = avg_dauer_pro_fh.loc[min_avg_fh_icao, 'Flughafen Name']
                          beobachtung_kaq5_fh_text = (f"Die durchschnittliche Netzwerksichtbarkeitsdauer (gefiltert) variiert zwischen den Flughäfen, "
                                                      f"von {avg_dauer_pro_fh.loc[min_avg_fh_icao, 'Ø Dauer (Min)']:.1f} Min ({min_avg_fh_name}) "
                                                      f"bis {avg_dauer_pro_fh.loc[max_avg_fh_icao, 'Ø Dauer (Min)']:.1f} Min ({max_avg_fh_name}).")
                          print(f"\nBeobachtung KAQ5 (Flughäfen, gefiltert): {beobachtung_kaq5_fh_text}")
                          beobachtungen_dict['KAQ5_FH_Vergleich'] = beobachtung_kaq5_fh_text
                 else:
                    print("Keine der zu analysierenden Flughäfen in den gefilterten Daten für Daueranalyse gefunden.")
        else:
            print(f"\nKeine Flüge im plausiblen Dauerbereich ({min_dauer_filter}-{max_dauer_filter} Min) für gefilterte Analyse gefunden.")
    else:
        print(f"Column '{duration_col_kaq5}' ist nicht numerisch oder enthält keine gültigen (nicht-NaN) Werte. Analyse übersprungen.")
else:
    print(f"\nÜberspringe Analyse der Netzwerksichtbarkeitsdauer (KAQ5): DataFrame leer oder Column '{duration_col_kaq5}' fehlt.")
# -

# ### 3.7 KAQ 6 (Prädiktiv): Flugverkehrsprognose (Beispiel LSZH)
# Anwendung von Zeitreihenmodellen zur Vorhersage des täglichen Flugaufkommens für einen ausgewählten Flughafen.
# Diese Analyse ist exemplarisch und demonstriert mögliche Ansätze.

# + tags=["scroll_output"]
PREDICTION_AIRPORT_ICAO = 'LSZH'

PREDICTION_AIRPORT_NAME = FLUGHAFEN_MAP.get(PREDICTION_AIRPORT_ICAO, PREDICTION_AIRPORT_ICAO)
PREDICTION_HORIZON_DAYS = 90
MIN_DATA_POINTS_FOR_PREDICTION = 365 * 2 # min 2 Jahre für sinnvolle Saisonalitätsschätzung

# Sicherstellen, dass die notwenigen Columns für die Prognose vorhanden sind
if not df_final.empty and 'firstseen' in df_final.columns and \
   pd.api.types.is_datetime64_any_dtype(df_final['firstseen']) and \
   'query_airport' in df_final.columns:

    logging.info(f"\n--- Beginn Prädiktive Analyse (KAQ6) für {PREDICTION_AIRPORT_NAME} ({PREDICTION_AIRPORT_ICAO}) ---")

    if PREDICTION_AIRPORT_ICAO not in df_final['query_airport'].unique():
        logging.warning(f"Ausgewählter Flughafen {PREDICTION_AIRPORT_NAME} ({PREDICTION_AIRPORT_ICAO}) nicht in den Daten gefunden. Überspringe Prognose.")
    else:
        # --- Datenvorbereitung für Zeitreihenprognose ---
        # Filtere Daten für den gewählten Flughafen und aggregiere auf täglicher Basis
        df_predict_source = df_final[df_final['query_airport'] == PREDICTION_AIRPORT_ICAO].copy()

        # Stelle sicher, dass 'firstseen' ein DatetimeIndex für resample ist
        if not pd.api.types.is_datetime64_any_dtype(df_predict_source['firstseen']):
             df_predict_source['firstseen'] = pd.to_datetime(df_predict_source['firstseen'], errors='coerce', utc=True)
        df_predict_source.set_index('firstseen', inplace=True)

        # Tägliche Flugzahlen
        daily_counts_ts = df_predict_source.resample('D').size().reset_index() # ('D' für Tag)
        daily_counts_ts.columns = ['ds', 'y'] # Prophet: 'ds' (Datum) und 'y' (Zielvariable)

        logging.info(f"Tägliche Flugzahlen für {PREDICTION_AIRPORT_NAME} vorbereitet. Zeitraum: {daily_counts_ts['ds'].min().date()} bis {daily_counts_ts['ds'].max().date()}. Anzahl Tage: {len(daily_counts_ts)}")

        if len(daily_counts_ts) < MIN_DATA_POINTS_FOR_PREDICTION:
            logging.warning(f"Weniger als {MIN_DATA_POINTS_FOR_PREDICTION} tägliche Datenpunkte ({len(daily_counts_ts)}) für {PREDICTION_AIRPORT_NAME}. Prognosequalität stark eingeschränkt oder nicht zuverlässig möglich.")
            print(f"Nicht genügend Datenpunkte ({len(daily_counts_ts)}) für eine robuste Prognose für {PREDICTION_AIRPORT_NAME}. Minimum: {MIN_DATA_POINTS_FOR_PREDICTION}.")
        else:
            # --- Methode 1: Prophet ---
            if PROPHET_AVAILABLE:
                logging.info("\n--- Prognose mit Prophet ---")
                try:
                    prophet_data_train = daily_counts_ts.copy()
                    # Prophet erwartet 'ds' ohne Zeitzone oder UTC
                    if prophet_data_train['ds'].dt.tz is not None:
                        prophet_data_train['ds'] = prophet_data_train['ds'].dt.tz_localize(None)

                    logging.info(f"Trainiere Prophet Modell mit Daten bis {prophet_data_train['ds'].max().date()}...")
                    # Modell initialisieren
                    model_prophet = Prophet(
                        yearly_seasonality=True,
                        weekly_seasonality=True,
                        daily_seasonality=False, # TODO Tägliche Saisonalität oft nicht sinnvoll für tägliche Flugzahlen
                        changepoint_prior_scale=0.05 # Standard, kann optimiert werden
                    )
                    # Schweizer Feiertage könnten hier hinzugefügt werden
                    # model_prophet.add_country_holidays(country_name='CH')

                    model_prophet.fit(prophet_data_train)

                    # DataFrame für zukünftige Datenpunkte
                    future_dates = model_prophet.make_future_dataframe(periods=PREDICTION_HORIZON_DAYS, freq='D')
                    logging.info(f"Erstelle Vorhersage für die nächsten {PREDICTION_HORIZON_DAYS} Tage bis {future_dates['ds'].max().date()}.")
                    forecast_prophet = model_prophet.predict(future_dates)

                    logging.info("Visualisiere Prophet Vorhersage...")
                    fig_prophet_fc = model_prophet.plot(forecast_prophet, figsize=(12, 6))
                    ax_prophet = fig_prophet_fc.gca()
                    ax_prophet.set_title(f'Prophet: Tägliche Flugaufkommen Vorhersage für {PREDICTION_AIRPORT_NAME}', fontsize=12, loc='left', fontweight='bold')
                    ax_prophet.set_xlabel('Datum', fontsize=10)
                    ax_prophet.set_ylabel('Prognostizierte Flüge (yhat)', fontsize=10)
                    last_actual_date = prophet_data_train['ds'].max()
                    ax_prophet.axvline(last_actual_date, color=IBCS_DUNKELGRAU, linestyle=':', lw=1,
                                       label=f'Ende Ist-Daten ({last_actual_date.date()})')

                    # Prophet zeichnet die Linien und Punkte intern. Nachträglich modifizieren für bessere IBCS-Standard
                    # Prognoselinie = 'fcst_line'; 'history_dots' sind die Ist-Punkte
                    for line in ax_prophet.get_lines():
                        if line.get_label() == 'yhat':
                            line.set_color(IBCS_MITTELGRAU)
                            line.set_linestyle('--')
                        elif line.get_label() == 'Actual':
                            pass

                    # Heutiges Datum als vertikale Linie hinzufügen (falls im Prognosezeitraum)
                    today_marker = pd.to_datetime('today').normalize()
                    if today_marker >= forecast_prophet['ds'].min() and today_marker <= forecast_prophet['ds'].max():
                        ax_prophet.axvline(today_marker, color=IBCS_ROT, linestyle='--', lw=1.5, label=f"Heute ({today_marker.date()})")
                    ax_prophet.legend(loc='upper left', frameon=False)
                    plt.show()

                    logging.info("Visualisiere Prophet Komponenten (Trend, Saisonalität)...")
                    fig_prophet_comp = model_prophet.plot_components(forecast_prophet, figsize=(12, 8))
                    plt.show()

                    print("\nLetzte 5 Tage der Prophet Vorhersage:")
                    display(forecast_prophet[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail().style.format({'ds': '{:%Y-%m-%d}', 'yhat': '{:.0f}', 'yhat_lower': '{:.0f}', 'yhat_upper': '{:.0f}'}))

                    # Beobachtung für Management Summary
                    last_hist_val = prophet_data_train['y'].iloc[-1] # Letzter bekannter Wert
                    # Nimm einen Punkt in der Mitte des Prognosehorizonts für Trendaussage
                    mid_forecast_idx = len(prophet_data_train) + PREDICTION_HORIZON_DAYS // 2 -1
                    if mid_forecast_idx < len(forecast_prophet):
                        mid_forecast_val = forecast_prophet['yhat'].iloc[mid_forecast_idx]
                        trend_direction_prophet = "steigende" if mid_forecast_val > last_hist_val else "fallende" if mid_forecast_val < last_hist_val else "stabile"
                        beobachtung_kaq6_prophet_text = f"Prophet-Modell für {PREDICTION_AIRPORT_NAME} prognostiziert tendenziell {trend_direction_prophet} tägliche Flugzahlen für die nächsten ca. {PREDICTION_HORIZON_DAYS} Tage (basierend auf yhat Mitte Prognose vs. letzter Wert)."
                        print(f"Beobachtung KAQ6 (Prophet, {PREDICTION_AIRPORT_NAME}): {beobachtung_kaq6_prophet_text}")
                        beobachtungen_dict[f'KAQ6_Prophet_{PREDICTION_AIRPORT_ICAO}'] = beobachtung_kaq6_prophet_text
                    else:
                        logging.warning("Konnte keinen mittleren Prognosewert für Trendaussage ermitteln.")

                except Exception as e_prophet:
                    logging.error(f"Fehler bei der Prophet Prognose für {PREDICTION_AIRPORT_NAME}: {e_prophet}")
            else:
                print("Prophet Bibliothek nicht verfügbar, überspringe Prophet-Prognose.")

            # --- Methode 2: Lineare Regression mit Zeit-Features (exemplarische Evaluation auf Test-Set) ---
            if SKLEARN_AVAILABLE:
                logging.info("\n--- Prognose mit Linearer Regression (Test-Set Evaluation) ---")
                try:
                    lr_data = daily_counts_ts.copy()
                    # Feature Engineering für lineare Regression
                    lr_data['jahr'] = lr_data['ds'].dt.year
                    lr_data['monat'] = lr_data['ds'].dt.month
                    # lr_data['tag_im_monat'] = lr_data['ds'].dt.day # Tag im Monat eher nicht interessant
                    lr_data['tag_in_woche'] = lr_data['ds'].dt.dayofweek # Wochentag
                    lr_data['tag_im_jahr'] = lr_data['ds'].dt.dayofyear # Jahresverlauf
                    lr_data['woche_im_jahr'] = lr_data['ds'].dt.isocalendar().week.astype(int) # Kalenderwoche
                    lr_data['zeit_schritt'] = np.arange(len(lr_data)) # Einfacher linearer Trend

                    features_lr = ['jahr', 'monat', 'tag_in_woche', 'tag_im_jahr', 'woche_im_jahr', 'zeit_schritt']
                    X_lr = lr_data[features_lr]
                    y_lr = lr_data['y']

                    # Train/Test Split: Teste auf den letzten PREDICTION_HORIZON_DAYS Tagen
                    # Dies ist ein einfacher Split, keine Kreuzvalidierung
                    if len(X_lr) > PREDICTION_HORIZON_DAYS:
                        X_train_lr, X_test_lr = X_lr.iloc[:-PREDICTION_HORIZON_DAYS], X_lr.iloc[-PREDICTION_HORIZON_DAYS:]
                        y_train_lr, y_test_lr = y_lr.iloc[:-PREDICTION_HORIZON_DAYS], y_lr.iloc[-PREDICTION_HORIZON_DAYS:]
                        dates_test_lr = lr_data['ds'].iloc[-PREDICTION_HORIZON_DAYS:]

                        if not X_train_lr.empty and not X_test_lr.empty:
                            logging.info(f"Lineare Regression: Training auf {len(X_train_lr)} Tagen, Test auf {len(X_test_lr)} Tagen.")
                            model_lr = LinearRegression()
                            model_lr.fit(X_train_lr, y_train_lr)
                            y_pred_lr = model_lr.predict(X_test_lr)

                            mse_lr = mean_squared_error(y_test_lr, y_pred_lr)
                            rmse_lr = np.sqrt(mse_lr)
                            mae_lr = mean_absolute_error(y_test_lr, y_pred_lr)
                            logging.info(f"Lineare Regression - Evaluation auf Test-Set ({PREDICTION_HORIZON_DAYS} Tage):")
                            logging.info(f"  RMSE: {rmse_lr:.2f}")
                            logging.info(f"  MAE:  {mae_lr:.2f} (Durchschnittlicher absoluter Fehler pro Tag)")
                            logging.info(f"  Zum Vergleich: Durchschnittliche Flugzahl im Testset: {y_test_lr.mean():.2f}")

                            plt.figure(figsize=(12, 6))
                            plt.plot(dates_test_lr, y_test_lr.values, label='Tatsächlich', marker='.', linestyle='-', color=IBCS_DUNKELGRAU, alpha=0.7)
                            plt.plot(dates_test_lr, y_pred_lr, label='Prognose (Lineare Regression)', marker=None, linestyle='--', color=IBCS_ROT)
                            plt.title(f'Lineare Regression: Vorhersage vs. Realität für {PREDICTION_AIRPORT_NAME} (Test-Set)', fontsize=12, loc='left', fontweight='bold')
                            plt.xlabel('Datum', fontsize=10); plt.ylabel('Anzahl Flüge', fontsize=10); plt.legend(frameon=False); plt.grid(True, linestyle=':', alpha=0.5)
                            plt.show()

                            beobachtung_kaq6_lr_text = f"Lineare Regression für {PREDICTION_AIRPORT_NAME} zeigte einen MAE von {mae_lr:.2f} auf einem Test-Set von {PREDICTION_HORIZON_DAYS} Tagen."
                            print(f"Beobachtung KAQ6 (LinReg, {PREDICTION_AIRPORT_NAME}): {beobachtung_kaq6_lr_text}")
                            beobachtungen_dict[f'KAQ6_LinReg_{PREDICTION_AIRPORT_ICAO}'] = beobachtung_kaq6_lr_text
                        else:
                            logging.warning("Nicht genügend Daten für Train/Test Split der Linearen Regression nach Aufteilung.")
                    else:
                        logging.warning(f"Nicht genügend Daten ({len(X_lr)}) für einen sinnvollen Train/Test Split (Horizont: {PREDICTION_HORIZON_DAYS} Tage) bei der Linearen Regression.")

                except Exception as e_lr:
                    logging.error(f"Fehler bei der Linearen Regressions-Prognose für {PREDICTION_AIRPORT_NAME}: {e_lr}")
            else:
                print("Scikit-learn Bibliothek nicht verfügbar, überspringe Lineare Regressions-Prognose.")
else:
    logging.warning("Prädiktive Analyse (KAQ6): Datenanforderungen nicht erfüllt.")
    print("Prädiktive Analyse (KAQ6) übersprungen: Datenanforderungen nicht erfüllt.")
# -

# ## 4. Schritt: Präsentation der Informationen (Present Information)
#
# **Ziel:** Effektive Kommunikation der in Schritt 3 gewonnenen Beobachtungen, Kennzahlen und Prognosebeispiele (Marr, 2020).
#
# Die Visualisierungen für KAQ 1-5 sind bereits in den jeweiligen Unterabschnitten von Schritt 3 integriert. Die Prognosevisualisierungen (KAQ 6) wurden in Abschnitt 3.7 erstellt.

# ### 4.1 Zusammenfassung der gesammelten Beobachtungen
# Die Beobachtungen aus den vorangehenden Abschnitten wird hier nochmals zusammengefasst:

if 'beobachtungen_dict' in locals() and beobachtungen_dict:
    print("--- Gesammelte Kernbeobachtungen aus der Analyse ---")
    for key, value in beobachtungen_dict.items():
        print(f"- {key.replace('_', ' ')}: {value}")
else:
    print("Keine Beobachtungen im 'beobachtungen_dict' gesammelt.")
# ```

# ### 4.2 Visualisierung: Jährlicher Trend am Flughafen Zürich (KAQ 1)
# Die Visualisierung für KAQ 1 wurden bereits in **Abschnitt 3.2** erzeugt und angezeigt.
# Die Darstellung zeigt die Entwicklung der Flugzahlen pro Jahr für den verkehrsreichsten Flughafen, inklusive prozentualer Vorjahresveränderung.

# ### 4.3 Visualisierung: Top Fluggesellschaften (Gesamt und Flughafen Zürich) (KAQ 2)
# Diese Tabellen zur Visualisierung der Top Fluggesellschaften wurde bereits in **Abschnitt 3.3** integriert.
# Sie listen die aktivsten Airline-Codes im analysierten Schweizer Luftraum und spezifisch für den Flughafen Zürich auf.

# ### 4.4 Visualisierung: Top Routen pro Flughafen (KAQ 3)
# Diese Tabellen wurden bereits in **Abschnitt 3.4** aufbereitet.
# Für jeden analysierten Flughafen werden die Top 10 Herkunfts- und Zielflughäfen (ICAO-Codes) mit der jeweiligen Anzahl an Flügen dargestellt.

# ### 4.5 Visualisierung: Fluglokalität (Gesamt und pro Flughafen) (KAQ 4)
# Diese Tabellen wurden bereits in **Abschnitt 3.5** erzeugt und angezeigt.
# Es wird die Verteilung des Flugverkehrs auf nationale, internationale und andere Segmente gezeigt, sowohl gesamt für alle Schweizer Flüge als auch detailliert pro Flughafen.

# ### 4.6 Visualisierung: Netzwerksichtbarkeitsdauer (KAQ 5)
# Deskriptive Statistiken (Tabellen) zur Netzwerksichtbarkeitsdauer wurden in **Abschnitt 3.6** dargestellt.
# Dies umfasst Statistiken für alle gültigen Flüge, für einen gefilterten, plausiblen Dauerbereich und einen Vergleich der Durchschnitts- und Mediandauer pro Flughafen.

# ### 4.7 Visualisierung: Prognose Flugaufkommen (Beispielhafter Flughafen) (KAQ 6)
# Die Diagramme zur Prognose des täglichen Flugaufkommens mittels Prophet (Vorhersageplot und Komponentenplot) sowie der Vergleich der Linearen Regression mit tatsächlichen Werten auf einem Test-Set wurden in **Abschnitt 3.7** erzeugt und angezeigt.
#

# ## 5. Schritt: Datengestützte Entscheidungen und Empfehlungen (Make Data-Driven Decisions)
#
# **Ziel:** Das Ziel dieses Schrittes ist di Überführung der gewonnenen Informationen in Insights und potenzielle Handlungsempfehlungen (Marr, 2020).
#
# ### 5.1 Synthese der Kern-Insights
#
# Die Analyse der Schweizer Flugdaten (2016-2024) lieferte folgende zentrale Erkenntnisse:
#
# * **Insight 1 (Marktdynamik & Konzentration):** Das Verkehrsaufkommen zeigte deutliche Schwankungen über die Jahre, insbesondere einem starken Rückgang während der COVID-19-Pandemie und eine Erholung danach. Der Flughafen Zürich (LSZH) blieb der verkehrsreichste Flughafen (1.39 Mio Flüge), gefolgt von Genf (KAQ 1). Swiss (SWR) war die dominante Airline in Zürich mit einem Anteil von 51,8% an allen identifizierten Flügen. Die wichtigste Route war Zürich–London Heathrow (EGLL). *Dies unterstreicht die Notwendigkeit agiler Anpassungen und Risikomanagement bezüglich Abhängigkeiten.*
# * **Insight 2 (Internationale Ausrichtung & Stabilität):** Der internationale Flugverkehr dominierte mit ca. 93.5% aller Flüge durchgehend (KAQ 4). Die nationalen Flüge machten nur 6.5% aus. *Die internationale Verflechtung ist sehr relevant für die wirtschaftliche Rolle der Luftfahrt und macht die Branche anfällig für geopolitische und globale Krisen.*
# * **Insight 3 (Prognostizierte Entwicklung):** Für den Flughafen Zürich prognostiziert das Prophet-Modell einen leicht steigenden Trend beim täglichen Flugaufkommen in den nächsten 90 Tagen (KAQ 6). *Die Prognose liefert eine Orientierung für operative Planung (z. B. Personal oder Slots), sollte jedoch aufgrund vereinfachter Annahmen (keine externen Schocks, aggregierte Daten) mit Vorsicht interpretiert werden.*
# * **Insight 4 (Operative Charakteristika):** Die Netzwerksichtbarkeitsdauer (Zeit, in der ein Flug im OpenSky-Netz sichtbar war) (KAQ 5) variiert deutlich zwischen den Flughäfen, von 52,6 Minuten (Bern-Belp) bis 126,1 Minuten (Zürich). *Dies könnte auf Unterschiede in Flugzeugtypen, Kontrollabdeckung oder Flughafengrösse hindeuten.*
#
# ### 5.2 Potenzielle Implikationen und Entscheidungsfelder für Stakeholder
#
# Basierend auf diesen Insights ergeben sich folgende potenzielle Überlegungen:
#
# * **Für Flughafenbetreiber:**
#     * **Strategische Kapazitätsplanung:** Langfristige Trends (KAQ1) und Prognosen (KAQ6) sollten als Basis für Investitionsentscheidungen in Infrastruktur dienen.
#     * **Operative Ressourcenplanung:** Prognosen (KAQ6) und saisonale Muster (aus Prophet) können helfen, Personal und Gates effizienter zu planen.
# * **Für Fluggesellschaften:**
#     * **Netzwerk- und Flottenplanung:** Analyse historischer Routenperformance (KAQ3) und Nachfrageprognosen (KAQ6) können Entscheidungen über Frequenzen, Kapazitäten und neue Routen unterstützen.
# * **Für Flugsicherung/Regulierung:**
#     * **Luftraummanagement:** Langfristige Verkehrsentwicklung (KAQ1, KAQ6) und Daten zur Flugdauer (KAQ5) können bei der Planung von Luftraumkapazitäten und Effizienzsteigerungen helfen.
#
# **Wichtiger Hinweis:** Diese Implikationen sind basierend auf einer ersten Analyse im Rahmen dieser Arbeit. Entgültige Entscheidungen benötigen zusätzliche Daten und Expertenwissen.
#
# ### 5.3 Limitationen der Analyse und Feedback Loop / Nächste Schritte
# Die folgenden Limitationen sollten bei der Interpretation der Resultate berücksichtigt werden:
# * **Datenqualität**: Im Kapitel 2.2 wurden bereits die Mängel zur Datenqualität aufgezeigt.
# * **Modellvereinfachungen:** Die Prognosemodelle sind grundlegend und berücksichtigen keine externen Schocks oder detaillierte ökonomische Variablen. Dadurch ist die Genauigkeit begrenzt.
#
# **Feedback Loop / Nächste Schritte für verbesserte Entscheidungsfindung:**
#
# 1.  **Verfeinerung der Prognosemodelle:** Einbeziehung externer Variablen (z.B. BIP, Ölpreis, spezielle Events, Pandemie-Indikatoren), Hyperparameter-Optimierung, Vergleich mit weiteren Modellen (z.B. ARIMA, LSTM), robustere Validierungsstrategien (z.B. rollierende Kreuzvalidierung).
# 2.  **Kausalanalyse:** Untersuchung der Ursachen für beobachtete Trendbrüche oder starke Schwankungen (z.B. detaillierter Einfluss von COVID-19, Wirtschaftskrisen, Airline-Pleiten).
# 3.  **Szenarioanalyse:** Entwicklung von Prognosen unter verschiedenen Annahmen (z.B. optimistisches, pessimistisches, Basis-Szenario für externe Faktoren).
# (Weitere Punkte wie Datenanreicherung, detailliertere Segmentierung, Validierung der Approximationen, qualitative Ergänzung aus der vorherigen Version bleiben relevant.)
#
#
# ---

# ## 6. Literaturverzeichnis
#
# * Marr, B. (2020). *From data to decisions: A five-step approach to data-driven decision-making*. CPA Canada. https://www.cpacanada.ca/MAGs
# * OpenSky Network. (o. J.). *Trino – SQL-based access to the OpenSky historical database*.
#   Abgerufen am 2. Mai 2025, von https://opensky-network.org/data/trino
# * swissinfo.ch. (2024, Februar 14). *Passagierzahlen an Schweizer Flughäfen steigen*.
#   Abgerufen am 10. Mai 2025, von https://www.swissinfo.ch/ger/passagierzahlen-an-schweizer-flugh%C3%A4fen-steigen/72926380
#
# ---

# ## 7. Verwendete Hilfsmittel
#
# Neben dem Literaturverzeichnis und den Unteralgen im Unterricht, kamen für die Erstellung dieser Arbeit folgende Hilfsmittel zum Einsatz:
#
# * **PyCharm** sowie **Google Colab** zur Entwicklung, Ausführung und Validierung des Codes.
# * **GitHub Copilot** als KI-gestützter Programmierassistent zur Code-Vervollständigung und Syntaxunterstützung in PyCharm.
# * **ChatGPT** zur sprachlichen Überprüfung (Rechtschreibung, Stil, Einheitlichkeit) sowie zur Verbesserung von Code-Abschnitten.
#
# ---

# ## 8. Anhang
#
# ### 8.1 Daten-Glossar / Metadaten
#
# * **icao24:** Eindeutiger 24-bit Transpondercode des Flugzeugs.
# * **firstseen:** Zeitstempel der ersten Sichtung im Netzwerk (UTC).
# * **lastseen:** Zeitstempel der letzten Sichtung im Netzwerk (UTC).
# * **query_airport:** ICAO-Code des Flughafens, für den die Daten primär abgefragt wurden.
# * **flight_type:** 'ARRIVAL' oder 'DEPARTURE' bezogen auf den `query_airport`.
# * **callsign:** Rufzeichen des Fluges.
# * **departure_airport:** ICAO-Code des Abflughafens (wenn bekannt).
# * **arrival_airport:** ICAO-Code des Zielflughafens (wenn bekannt).
# * **network_duration_minutes:** Berechnete Dauer zwischen firstseen und lastseen in Minuten (Approximation).
# * **airline_code:** Aus den ersten 3 Buchstaben des Callsigns extrahierter Code (Approximation).
# * **locality:** Berechnete Kategorie (National, International, etc.).
# * **jahr:** Jahr des `firstseen` Zeitstempels.
# * **monat_nr:** Monat (numerisch, 1-12) des `firstseen` Zeitstempels.
# * **monat_name:** Monatsname des `firstseen` Zeitstempels.
# * **wochentag_nr:** Wochentag (numerisch, 0=Montag bis 6=Sonntag) des `firstseen` Zeitstempels.
# * **wochentag_name:** Name des Wochentags des `firstseen` Zeitstempels.
#
# **Mapping ICAO zu Flughafenname:**

FLUGHAFEN_MAP = {
    'LSZH': 'Zürich', 'LSGG': 'Genève', 'LSZB': 'Bern-Belp',
    'LSZA': 'Lugano-Agno', 'LSZR': 'St. Gallen-Altenrhein',
    'LFSB': 'Basel-Mulhouse (EuroAirport)'
}
print(FLUGHAFEN_MAP)

# ### 8.2 Detailierte Datenübersichten
#

# **Bereinigte Daten Übersicht (`df_cleaned.info()`):**

df_cleaned.info()

#
# **Bereinigte Daten Deskriptive Statistik (`df_cleaned.describe(include=np.number)`):**

display(bereinigt_describe)

# **Finale Daten Übersicht (`df_final.info()`):**

df_final.info()

# **Finale Daten Deskriptive Statistik (`df_final.describe(include='all')`):**

display(df_final.describe(include='all'))

# ---
# Ende des Notebooks
# ---
# %%
