from rich.console import Console
from rich.table import Table
import sqlite3
import random
import os
import time
## CONNECT TA SA DATABASE
database = sqlite3.connect("peanutflixx_usrs.db")
cursor = database.cursor()

## TODO
## ADMIN THAT CAN ADD, UPDATE, AND REMOVE DATA/USER 10pts


def printTable(title, columns, rows):
    table = Table(title=title)
    for column in columns:
        table.add_column(column)

    for row in rows:
        table.add_row(*row, style='bright_green')

    console = Console()
    console.print(table)
    

def viewusers():
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    columns = ["ID NUMBER", "F.Name", "L.Name", "Email", "Address", "S.left"]
    printTable("Users", columns, rows)
def genIdNumber():
    number = random.randint(120000, 999999)
    return number
def addUser(name, lname, email, address):
    cursor.execute("SELECT unique_id FROM users")
    idNumbers = [row[0] for row in cursor.fetchall()]
    idNumber = genIdNumber()
    print(idNumber)
    if idNumbers in idNumbers:
        print("Id number already in the database\nGenerating another one\n")
        addUser()
    else:
        print("Unique id number generated!!!\nProceeding to add in the database")
        cursor.execute(f"INSERT INTO users VALUES ('{idNumber}','{name}','{lname}','{email}','{address}','0')")
        print("User added successfully\nShowing updated users list")
        time.sleep(1)
        database.commit()
def update_user(idnumber):
    cursor.execute(f"SELECT * FROM users WHERE unique_id = '{idnumber}'")
    rows = cursor.fetchall()
    columns = ["ID NUMBER", "F.Name", "L.Name", "Email", "Address", "S.left"]
    printTable("Users", columns, rows)
    choice = input("What do you want to update?\n[1]Name\n[2]Last Name\n[3]Email\n[4]Address\n[5]Subscription Left\n>>> ")
    if choice == "1":
        new_name = input("Enter new name: ")
        cursor.execute(f"UPDATE users SET name = '{new_name}' WHERE unique_id = '{idnumber}'")
        database.commit()
        print("Name updated successfully\nShowing updated users list")
        time.sleep(1)
        main()
    elif choice == "2":
        new_lname = input("Enter new last name: ")
        cursor.execute(f"UPDATE users SET last_name = '{new_lname}' WHERE unique_id = '{idnumber}'")
        database.commit()
        print("Last name updated successfully\nShowing updated users list")
        time.sleep(1)
        main()
    elif choice == "3":
        new_email = input("Enter new email: ")
        cursor.execute(f"UPDATE users SET email = '{new_email}' WHERE unique_id = '{idnumber}'")
        database.commit()
        print("Email updated successfully\nShowing updated users list")
        time.sleep(1)
        main()
    elif choice == "4":
        new_address = input("Enter new address: ")
        cursor.execute(f"UPDATE users SET address = '{new_address}' WHERE unique_id = '{idnumber}'")
        database.commit()
        print("Address updated successfully\nShowing updated users list")
        time.sleep(1)
        main()
    elif choice == "5":
        new_dayL = input("Enter new subscription left: ")
        cursor.execute(f"UPDATE users SET subscription_left = '{new_dayL}' WHERE unique_id = '{idnumber}'")
        database.commit()
        print("Subscription left updated successfully\nShowing updated users list")
        time.sleep(1)
        main()
    else:
        print("Invalid choice")
        main()
def remove_user(idnumber):
    cursor.execute(f"DELETE FROM users WHERE unique_id = '{idnumber}'")
    database.commit()
    print("User removed successfully\nShowing updated users list")
    time.sleep(1)
    main()
def sort_by_subscriptionleft():
    #sort using bubble sort
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    columns = ["ID NUMBER", "F.Name", "L.Name", "Email", "Address", "S.left"]
    printTable("Users", columns, rows)
    print("\n\t\tSorting by subscription left\n")
    time.sleep(1)
    for i in range(len(rows)):
        for j in range(len(rows)-1):
            if int(rows[j][5]) > int(rows[j+1][5]):
                temp = rows[j]
                rows[j] = rows[j+1]
                rows[j+1] = temp
    printTable("Users", columns, rows)
    input("Press enter to continue...")
    main()
def sort_by_subscrionleft_ascending():
    #sort using bubble sort
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    columns = ["ID NUMBER", "F.Name", "L.Name", "Email", "Address", "S.left"]
    printTable("Users", columns, rows)
    print("\n\t\tSorting by subscription left\n")
    time.sleep(1)
    for i in range(len(rows)):
        for j in range(len(rows)-1):
            if int(rows[j][5]) < int(rows[j+1][5]):
                temp = rows[j]
                rows[j] = rows[j+1]
                rows[j+1] = temp
    printTable("Users", columns, rows)
    time.sleep(1)
    input("Press enter to continue...")
    main()
def main():
    os.system("cls")
    print("\n\t\tWelcome to admin panel\n")
    viewusers()
    print("[1]Add user\n[2]Update user\n[3]Remove user\n[4]Sort by Subscription Left(descending)\n[5]Sort by Subscription Right(ascending)")
    choice = input(">>> ")
    if choice == "1":
        name = input("Enter first name: ")
        lname = input("Enter last name: ")
        email = input("Enter email: ")
        address = input("Enter address: ")
        addUser(name, lname, email, address)
        main()
    elif choice == "2":
        idnumber = input("Enter id number: ")
        cursor.execute("SELECT unique_id FROM users")
        idNumbers = [row[0] for row in cursor.fetchall()]
        if idnumber in idNumbers:
            update_user(idnumber)
        else:
            print("Id number not found")
            time.sleep(1)
            main()
    elif choice == "3":
        idnumber = input("Enter id number: ")
        cursor.execute("SELECT unique_id FROM users")
        idNumbers = [row[0] for row in cursor.fetchall()]
        if idnumber in idNumbers:
            remove_user(idnumber)
        else:
            print("Id number not found")
            time.sleep(1)
            main()
    elif choice == "4":
        sort_by_subscriptionleft()
    elif choice == "5":
        sort_by_subscrionleft_ascending()
    
    
main()