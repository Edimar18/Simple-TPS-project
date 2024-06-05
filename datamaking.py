import sqlite3

## DATABASE CONNECTION
database = sqlite3.connect("peanutflixx_usrs.db")
cursor = database.cursor()

## CREATE TABLE

create = "CREATE TABLE IF NOT EXISTS users(unique_id TEXT, name TEXT, last_name TEXT, email TEXT, address TEXT, subscription_left TEXT)"
create_atm_data = "CREATE TABLE IF NOT EXISTS atm(name TEXT,last_name TEXT ,card_number TEXT, card_pin TEXT, balance TEXT)"
def create_table():
    cursor.execute(create)
    cursor.execute(create_atm_data)

def put_info():
    cursor.execute("INSERT INTO users VALUES('127987', 'Edimar', 'Mosquida', 'edimarmosquia@gmail.com', 'Lapasan', '10') ")
    cursor.execute("INSERT INTO users VALUES('123456', 'Kurt', 'Buan', 'Kurtbuan@gmail.com', 'Macasandig', '1') ")
    cursor.execute("INSERT INTO atm VALUES('Edimar', 'Mosquida', '129009', '1234', '120000') ")
    cursor.execute("INSERT INTO atm VALUES('Kurt', 'Buan', '111111', '4321', '1203')  ")
create_table()
put_info()
database.commit()