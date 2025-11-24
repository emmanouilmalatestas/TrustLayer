import pandas as pd
import requests
import hashlib
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

# Φόρτωσε .env
load_dotenv()

PG_USER = os.getenv("PG_USER")
PG_PASSWORD = os.getenv("PG_PASSWORD")
PG_HOST = os.getenv("PG_HOST")
PG_PORT = os.getenv("PG_PORT")
PG_DB = os.getenv("PG_DB")

engine = create_engine(f"postgresql+psycopg2://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{PG_DB}")

# Κατέβασε δεδομένα GDP από World Bank JSON API
url = "http://api.worldbank.org/v2/country/all/indicator/NY.GDP.MKTP.CD?format=json&per_page=20000"
response = requests.get(url)
data = response.json()

# Τα δεδομένα είναι στη δεύτερη λίστα (index 1)
records = data[1]

# Φτιάξε DataFrame
df = pd.DataFrame(records)

# Κράτα μόνο τα πεδία που μας ενδιαφέρουν
df_clean = df[["country", "date", "value"]].dropna(subset=["value"])

# Μετατροπή country σε string (κρατάμε το όνομα)
df_clean["country"] = df_clean["country"].apply(lambda x: x["value"] if isinstance(x, dict) else x)
df_clean["date"] = df_clean["date"].astype(str)

# Υπολογισμός hash
hash_value = hashlib.sha256(pd.util.hash_pandas_object(df_clean, index=False).values).hexdigest()
print(f"Dataset hash: {hash_value}")

# Αποθήκευση στη βάση
df_clean.to_sql("gdp_data", engine, if_exists="replace", index=False)

print("✅ Δεδομένα GDP φορτώθηκαν επιτυχώς")