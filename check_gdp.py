import pandas as pd
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

# Διάβασε δεδομένα
df = pd.read_sql("SELECT country, date, value FROM gdp_data ORDER BY date DESC LIMIT 20;", engine)

print("✅ Τελευταίες 20 εγγραφές GDP:")
print(df)