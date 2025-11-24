import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()
PG_USER = os.getenv("PG_USER")
PG_PASSWORD = os.getenv("PG_PASSWORD")
PG_HOST = os.getenv("PG_HOST")
PG_PORT = os.getenv("PG_PORT")
PG_DB = os.getenv("PG_DB")

conn_str = f"postgresql://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{PG_DB}"
engine = create_engine(conn_str)

try:
    with engine.connect() as conn:
        print("✅ Σύνδεση επιτυχής στη βάση:", PG_DB)
except Exception as e:
    print("❌ Σφάλμα σύνδεσης:", e)

