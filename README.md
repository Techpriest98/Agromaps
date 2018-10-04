# Agro maps

Students project

## Install

Install base packages:

```bash
sudo apt install python3.7 python3-pip mysqlclient mysql-server
```
Setup virtual environment:
```bash
python3.7 -m pip install virtualenv
virtualenv venv
source ./venv/bin/activate
```
Install dependencies:
```bash
pip install Django mysqlclient
```
Create mysql database:
```bash
mysql -u root -p -e "CREATE DATABASE agromaps CHARACTER SET utf8 COLLATE utf8_general_ci;"
```
Set mysql parameters at settings.py

Setup project. Use admin:admin login:password for super-admin
```bash
python manage.py migrate
python manage.py createsuperuser
```
Run server:
```bash
python manage.py runserver
```
