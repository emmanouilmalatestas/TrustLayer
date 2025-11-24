import psycopg2

def test_gdp_data_count():
    conn = psycopg2.connect(
        dbname="trustlayer_test",
        user="postgres",
        password="2511ma!",   # 🔑 πρόσθεσε εδώ τον κωδικό
        host="127.0.0.1",
        port="5432"
    )
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM gdp_data;")
    count = cur.fetchone()[0]
    conn.close()

    assert count > 0, "Η βάση trustlayer_test δεν έχει δεδομένα!"