import sqlite3
## DATABASE CONNECTION
database = sqlite3.connect("peanutflixx_usrs.db")
cursor = database.cursor()

cursor.execute("SELECT balance FROM atm WHERE card_number = 129009")
result = cursor.fetchone()[0]
print (result)
