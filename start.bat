@echo off

:: Set the IP address of the database server.
:: !!! IMPORTANT: Replace 192.168.1.100 with your actual server IP address.
set DB_SERVER=192.168.153.9
set DB_USER=knitex
set DB_PASSWORD=eb564ff0

:: Set the database credentials. You can also set these here if they are not in a .env file.
:: set DB_USER=your_db_user
:: set DB_PASSWORD=your_db_password

:: Start the application.
echo Starting WorkSalary...
start "" "WorkSalary.exe"

exit