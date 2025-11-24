@echo off
set PGPASSWORD=TrustLayer2025!
"C:\Program Files\PostgreSQL\16\bin\pg_dump.exe" -U postgres -h 127.0.0.1 -p 5432 -F c -d trustlayer -f "C:\TrustLayer\backups\trustlayer_%DATE:~6,4%-%DATE:~3,2%-%DATE:~0,2%.dump"