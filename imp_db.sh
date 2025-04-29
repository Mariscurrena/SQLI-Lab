#!/usr/bin/env bash

############## NOTE: This is a script that works with debian distros
### DB Credentials
DB_User="root" 
DB_Pass="admin1234"
DB_Name="Prueb1"
DB_PATH="./Prueb1.sql"

### Is MySQL Installed?
if ! command -v mysql &> /dev/null; then
    echo -e "\033[0;32mMySQL is not installed!\033[0m\n"
    echo -e "\033[0;34mScript will proceed with MySQL Intallation\033[0m\n"
    sudo apt upate
    sudo apt install -y mysql-server
    sudo systemctl start mysql
    sudo systemctl enable mysql
else
    echo -e "\033[0;32mMySQL is installed!\033[0m\n"
fi

### MySQL Init
if ! systemctl is-active --quiet mysql; then
    echo -e "\033[0;34mMySQL is not running. Initializing MySQL Service...\033[0m\n"
    sudo systemctl start mysql
fi

### DB Import
echo -e "\033[0;34m--> Proceeding with DB import!\033[0m\n"
echo -e "\033[0;34m--> Importing ${DB_Name} Database from ${DB_PATH} file\033[0m\n"

### Verifing Database Location
if [ ! -f "$DB_PATH" ]; then
    echo -e "\033[0;31m--> Database: ${DB_Name} do not exist in current directory\033[0m"
    echo -e "\033[0;31m--> Aborting Operation!\033[0m\n"
    exit 1
else
    echo -e "\033[0;32m--> Database Schema Located!\033[0m\n"
fi

### Creating DB if not exist
sudo mysql -u "$DB_User" -p"$DB_Pass" -e "CREATE DATABASE IF NOT EXISTS ${DB_Name};"
echo -e "\033[0;34m--> Adding user privileges:\033[0m"
### Importing DB
sudo mysql -u "$DB_User" -p"$DB_Pass" "$DB_Name" < "$DB_PATH"

echo -e "\033[0;32m--> DB Import Successful!\033[0m\n"
