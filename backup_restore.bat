@echo off
REM === Ρυθμίσεις ===
set PGPASSWORD=TrustLayer2025!
set PG_BIN="C:\Program Files\PostgreSQL\16\bin"
set BACKUP_DIR=C:\TrustLayer\backups
set BACKUP_FILE=%BACKUP_DIR%\trustlayer_auto.dump

REM === Βήμα 1: Backup της βάσης trustlayer ===
echo Δημιουργία backup...
%PG_BIN%\pg_dump.exe -U postgres -h 127.0.0.1 -p 5432 -F c -d trustlayer -f "%BACKUP_FILE%"

REM === Βήμα 2: Δημιουργία test βάσης αν δεν υπάρχει ===
echo Έλεγχος για test βάση...
%PG_BIN%\psql.exe -U postgres -h 127.0.0.1 -p 5432 -tc "SELECT 1 FROM pg_database WHERE datname='trustlayer_test';" | findstr /C:"1" >nul
if errorlevel 1 (
    echo Δημιουργία βάσης trustlayer_test...
    %PG_BIN%\psql.exe -U postgres -h 127.0.0.1 -p 5432 -c "CREATE DATABASE trustlayer_test;"
)

REM === Βήμα 3: Restore στη test βάση ===
echo Επαναφορά στη βάση trustlayer_test...
%PG_BIN%\pg_restore.exe -U postgres -h 127.0.0.1 -p 5432 -d trustlayer_test "%BACKUP_FILE%"

echo Ολοκληρώθηκε!
pause