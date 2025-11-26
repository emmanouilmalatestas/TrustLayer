CREATE TABLE IF NOT EXISTS gdp_data (
    country TEXT,
    year INT,
    gdp NUMERIC
);

-- Προαιρετικά: εισαγωγή δεδομένων
INSERT INTO gdp_data (country, year, gdp)
VALUES ('Cyprus', 2022, 27.5), ('Greece', 2022, 219.5);