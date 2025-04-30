import pandas as pd
from pyopensky.trino import Trino
from datetime import datetime, timezone
import time
import logging
import sys
import os

# --- Configuration ---
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
OUTPUT_DIR = "."
CSV_FILENAME_TEMPLATE = "swiss_flight_data_{start}_{end}.csv"

# ICAO codes for Swiss airports
SWISS_AIRPORTS = ['LSZH', 'LSGG', 'LSZB', 'LSZA', 'LSZR', 'LFSB']
AIRPORTS_TO_QUERY = ['LSZH', 'LSGG', 'LSZB', 'LSZA', 'LSZR', 'LFSB']

START_TIME = datetime(2017, 1, 1, 0, 0, 0, tzinfo=timezone.utc)
STOP_TIME = datetime(2024, 12, 31, 0, 0, 0, tzinfo=timezone.utc)
start_ts = int(START_TIME.timestamp())
stop_ts = int(STOP_TIME.timestamp())

# --- Functions ---
def safe_timestamp(ts_input):
    """Convert input to UTC-aware datetime"""
    if pd.isna(ts_input):
        return None
    try:
        if isinstance(ts_input, (int, float)):
            if ts_input > 1e10:
                ts_input /= 1000
            return datetime.fromtimestamp(int(ts_input), timezone.utc)
        elif isinstance(ts_input, pd.Timestamp):
            return ts_input.tz_localize(timezone.utc) if ts_input.tzinfo is None else ts_input.tz_convert(timezone.utc).to_pydatetime()
        elif isinstance(ts_input, datetime):
            return ts_input.replace(tzinfo=timezone.utc) if ts_input.tzinfo is None else ts_input.astimezone(timezone.utc)
        else:
            logging.warning(f"Unexpected type for timestamp: {type(ts_input)}")
            return None
    except (ValueError, TypeError, OverflowError) as e:
        logging.warning(f"Timestamp conversion failed: {e}")
        return None

def fetch_flight_data(trino_conn, airport_icao, start_timestamp, stop_timestamp) -> pd.DataFrame:
    logging.info(f"Fetching data for {airport_icao} from {datetime.fromtimestamp(start_timestamp, timezone.utc)} to {datetime.fromtimestamp(stop_timestamp, timezone.utc)}")
    max_retries = 3
    retry_delay = 5
    for attempt in range(max_retries):
        try:
            results = trino_conn.flightlist(start_timestamp, stop_timestamp, airport=airport_icao)

            if results is None:
                logging.warning(f"API returned None for {airport_icao}. Attempt {attempt + 1}/{max_retries}")
                return pd.DataFrame()

            if isinstance(results, pd.DataFrame):
                if not results.empty:
                    logging.info(f"Fetched {len(results)} records for {airport_icao}")
                    rename_map = {'departure': 'estdepartureairport', 'arrival': 'estarrivalairport'}
                    results.rename(columns=rename_map, inplace=True, errors='ignore')
                return results
            else:
                logging.error(f"Unexpected result type: {type(results)} for {airport_icao}")
                return pd.DataFrame()

        except Exception as e:
            logging.error(f"Error fetching data for {airport_icao}: {e}. Attempt {attempt + 1}/{max_retries}")
            if attempt < max_retries - 1:
                time.sleep(retry_delay)
            else:
                return pd.DataFrame()

def process_raw_data(input_df: pd.DataFrame, query_airport_icao: str) -> list:
    if not isinstance(input_df, pd.DataFrame) or input_df.empty:
        return []

    required_cols = ['icao24', 'firstseen', 'estdepartureairport', 'lastseen', 'estarrivalairport', 'callsign']
    missing = [col for col in required_cols if col not in input_df.columns]
    if missing:
        logging.warning(f"Missing columns for {query_airport_icao}: {missing}")

    processed_data = []
    for row in input_df.itertuples(index=False, name='FlightData'):
        try:
            dep_airport = getattr(row, 'estdepartureairport', None)
            arr_airport = getattr(row, 'estarrivalairport', None)
            callsign = getattr(row, 'callsign', None)

            data_entry = {
                'icao24': getattr(row, 'icao24', None),
                'firstseen': safe_timestamp(getattr(row, 'firstseen', None)),
                'lastseen': safe_timestamp(getattr(row, 'lastseen', None)),
                'departure_airport': dep_airport.strip() if isinstance(dep_airport, str) else None,
                'arrival_airport': arr_airport.strip() if isinstance(arr_airport, str) else None,
                'callsign': callsign.strip() if isinstance(callsign, str) else None,
                'query_airport': query_airport_icao,
                'flight_type': 'Arrival' if arr_airport == query_airport_icao else 'Departure' if dep_airport == query_airport_icao else 'Unknown'
            }

            if all([data_entry['icao24'], data_entry['firstseen'], data_entry['lastseen']]) and data_entry['flight_type'] != 'Unknown':
                processed_data.append(data_entry)
        except Exception as e:
            logging.warning(f"Error processing row: {e}")

    return processed_data

def get_flight_locality(row):
    dep = row['departure_airport']
    arr = row['arrival_airport']
    dep_is_swiss = dep in SWISS_AIRPORTS
    arr_is_swiss = arr in SWISS_AIRPORTS

    if dep_is_swiss and arr_is_swiss:
        return 'Domestic'
    elif (dep_is_swiss and arr and not arr_is_swiss) or (arr_is_swiss and dep and not dep_is_swiss):
        return 'International'
    elif (dep_is_swiss and not arr) or (arr_is_swiss and not dep):
        return 'International (Incomplete Data)'
    elif not dep_is_swiss and not arr_is_swiss and (dep or arr):
        logging.warning(f"Unexpected non-Swiss route: dep={dep}, arr={arr}")
        return 'Non-Swiss Transit/Overflight'
    else:
        return 'Unknown'

# --- Main ---
if __name__ == "__main__":
    try:
        trino = Trino()
        logging.info("Connected to Trino")
    except Exception as e:
        logging.error(f"Trino connection failed: {e}")
        sys.exit(1)

    all_flight_data = []
    for airport in AIRPORTS_TO_QUERY:
        raw_df = fetch_flight_data(trino, airport, start_ts, stop_ts)
        if isinstance(raw_df, pd.DataFrame) and not raw_df.empty:
            processed = process_raw_data(raw_df, airport)
            if processed:
                all_flight_data.extend(processed)
                logging.info(f"Appended {len(processed)} records for {airport}")

    if not all_flight_data:
        logging.warning("No valid data collected")
        sys.exit(0)

    df = pd.DataFrame(all_flight_data)
    df['firstseen'] = pd.to_datetime(df['firstseen'], errors='coerce', utc=True)
    df['lastseen'] = pd.to_datetime(df['lastseen'], errors='coerce', utc=True)
    df.dropna(subset=['firstseen', 'lastseen', 'icao24', 'query_airport', 'flight_type'], inplace=True)

    if df.empty:
        logging.warning("All data dropped during cleaning")
        sys.exit(0)

    df['network_duration_minutes'] = (df['lastseen'] - df['firstseen']).dt.total_seconds() / 60
    df['airline_code'] = df['callsign'].astype(str).str[:3].str.upper()
    df.loc[df['airline_code'].isin(['NON', 'NAN', '', None]), 'airline_code'] = pd.NA
    df['locality'] = df.apply(get_flight_locality, axis=1)

    subset_cols = ['icao24', 'firstseen', 'lastseen', 'query_airport', 'flight_type']
    df.drop_duplicates(subset=subset_cols, keep='first', inplace=True)

    try:
        start_str = START_TIME.strftime('%Y%m%d')
        end_str = STOP_TIME.strftime('%Y%m%d')
        csv_filename = CSV_FILENAME_TEMPLATE.format(start=start_str, end=end_str)
        full_csv_path = os.path.join(OUTPUT_DIR, csv_filename)
        os.makedirs(OUTPUT_DIR, exist_ok=True)
        df_save = df.copy()
        df_save['firstseen'] = df_save['firstseen'].dt.strftime('%Y-%m-%d %H:%M:%S%z')
        df_save['lastseen'] = df_save['lastseen'].dt.strftime('%Y-%m-%d %H:%M:%S%z')
        df_save.to_csv(full_csv_path, index=False)
        logging.info(f"Saved {len(df_save)} records to {full_csv_path}")
    except Exception as e:
        logging.error(f"CSV save failed: {e}")

    logging.info("Script complete")
