'''

A PROJECT CREATED BY:

EDIMAR S. MOSQUIDA
KURT BUAN

------------------------
DISCRIPTION:
Peanutflixx Transactional Processing System is a PyQt5-based desktop application designed for 
managing user subscriptions and purchases. It connects to a SQLite database to store user 
information and transaction details. The system allows users to verify their identities using 
unique IDs, view their subscription details, and purchase additional subscription days using a 
virtual ATM. Upon successful payment, the system updates the user's subscription status and 
generates a receipt for the transaction. The application features a user-friendly interface 
with intuitive navigation and error handling mechanisms.

'''

from PyQt5.QtWidgets import *
from PyQt5 import uic
import sqlite3
from PyQt5.QtCore import QResource
from PyQt5.QtGui import QPixmap
import datetime

## DATABASE CONNECTION
database = sqlite3.connect("peanutflixx_usrs.db")
cursor = database.cursor()

## LOG FILE
def save_ToLog(message):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("log.txt", "a") as file:
        file.write(f"\n:::{timestamp}:::\n {message}\n")



class mainWindow(QMainWindow):
    def __init__(self):
        super(mainWindow, self).__init__()
        uic.loadUi("mainUI.ui", self)
        QResource.registerResource("resources.qrc")
        logoPixMap = QPixmap("logo.jpeg")
        userPixMap = QPixmap("icons8-user-100.png")
        
        self.show()
        self.amount = 0
        self.added_days = 0
        self.name=""
        self.address = ""
        self.lname = ""
        self.id_Num=""
        self.label_3.setPixmap(logoPixMap)
        self.label_7.setPixmap(userPixMap)
        self.pushButton.clicked.connect(self.verifier)
        self.pushButton_2.clicked.connect(self.home_to_sub)
        self.pushButton_3.clicked.connect(self.sub_to_home)
        self.pushButton_4.clicked.connect(self.sub_to_con)
        self.pushButton_7.clicked.connect(self.pur_to_confirm)
        self.pushButton_8.clicked.connect(self.cancelConfirm)
        self.pushButton_6.clicked.connect(self.pur_to_info)
        self.pushButton_9.clicked.connect(self.confirm_card)
        self.pushButton_10.clicked.connect(self.go_to_receipt)
        self.textEdit_2.textChanged.connect(self.enable_purchase_button)
        self.pushButton_11.clicked.connect(self.back_to_home)
    def verifier(self):
        Id_Number = self.textEdit.toPlainText()
        self.id_Num = Id_Number
        # Check if ID number exists in the user table
        check_query = "SELECT EXISTS(SELECT 1 FROM users WHERE unique_id=? LIMIT 1)"
        cursor.execute(check_query, (str(Id_Number),))
        result = cursor.fetchone()
        if result[0] == 1:
            self.label_5.setText("STATUS: USER FOUND IN THE DATABASE")
            self.label_5.setStyleSheet("background-color: rgb(244, 238, 215, 200);font-size: 30px;padding-left: 10px; color: green;")
            get_fname = "SELECT name FROM users WHERE unique_id=?" 
            get_lname = "SELECT last_name FROM users WHERE unique_id=?"
            get_address = "SELECT address FROM users WHERE unique_id=?"
            get_dayL = "SELECT subscription_left FROM users WHERE unique_id=?"
            cursor.execute(get_fname, (str(Id_Number),))
            Fname = cursor.fetchone()[0]
            self.name = Fname
            cursor.execute(get_lname, (str(Id_Number),))
            lname = name = cursor.fetchone()[0]
            self.lname = lname
            cursor.execute(get_address, (str(Id_Number),))
            address = cursor.fetchone()[0]
            self.address = address
            cursor.execute(get_dayL, (str(Id_Number),))
            dayL = str(cursor.fetchone()[0])
            self.dayL = dayL
            save_ToLog(f"{self.name} {self.lname} WAS VERIFIED")
            self.label_8.setText("Name: "+Fname)
            self.label_9.setText("Surname: "+lname)
            self.label_10.setText("Address: "+address)
            self.label_12.setText("Subscription Days Lefts: "+dayL)
            self.label_13.setText(Id_Number)
             
            self.pushButton_2.setEnabled(True)
            
        else:
            save_ToLog(f"ID NUMBER [{Id_Number}] WAS NOT FOUND IN THE DATABSE")
            self.pushButton_2.setEnabled(False)
            self.label_5.setStyleSheet("background-color: rgb(244, 238, 215, 200);font-size: 30px;padding-left: 10px; color: red;")
            self.label_5.setText("STATUS: NOT FOUND IN THE DATABASE")
    def home_to_sub(self):
        self.stackedWidget.setCurrentIndex(1)
    def sub_to_home(self):
        self.stackedWidget.setCurrentIndex(0)
    def sub_to_con(self):
        self.stackedWidget.setCurrentIndex(2)
    def enable_purchase_button(self):
        text = self.textEdit_2.toPlainText()
        if text.isdigit():
            self.label_28.setText(str(int(self.textEdit_2.toPlainText())*100))
            self.pushButton_7.setEnabled(True)
        else:
            self.label_28.setText("ENTER VALID AMOUNT")
            self.pushButton_7.setEnabled(False)
    def cancelPurchase(self):
        self.stackedWidget.setCurrentIndex(1)
    def pur_to_confirm(self):
        self.amount = self.textEdit_2.toPlainText()
        self.stackedWidget.setCurrentIndex(3)
    def pur_to_info(self):
        self.stackedWidget.setCurrentIndex(1)
        
    def confirm_card(self):
        to_pay = int(self.amount) * 100
        card_number = self.textEdit_3.toPlainText()
        card_pin = self.textEdit_4.toPlainText()
        check_ifExist = "SELECT EXISTS(SELECT 1 FROM atm WHERE card_number=? AND card_pin=?LIMIT 1)"
        cursor.execute(check_ifExist, (str(card_number),str(card_pin),))
        result = cursor.fetchone()
        if result[0] == 1:
            getBalance = "SELECT balance FROM atm WHERE card_number=?"
            cursor.execute(getBalance, (str(card_number),))
            atmBalance = cursor.fetchone()[0]
            if int(atmBalance) > to_pay:
                getTotalDays = "SELECT subscription_left FROM users WHERE name=?"
                cursor.execute(getTotalDays, (str(self.name),))
                totalDays = cursor.fetchone()[0]
                self.added_days = self.textEdit_2.toPlainText()
                updated_days = str(int(totalDays)+int(self.added_days))
                print(updated_days)
                self.label_21.setText(str(self.added_days)+" DAYS SUCCESSFULY ADDED TO YOUR ACCOUNT")
                cursor.execute(f"UPDATE users SET subscription_left = '{updated_days}' WHERE unique_id = '{self.id_Num}'")
                new_atmBalance = str(int(atmBalance)-(int(self.added_days)*100))
                print(new_atmBalance)
                cursor.execute(f"UPDATE atm SET balance = '{new_atmBalance}' WHERE card_number = '{card_number}' AND card_pin = '{card_pin}'")
                print("success")
                database.commit()
                save_ToLog(f"PAYMENT OF {to_pay} OR EQUIVALENT TO {self.amount} DAYS WAS SUCCESSFUL")
                QApplication.processEvents()
                self.stackedWidget.setCurrentIndex(4)
            else:
                save_ToLog(f"ATM CARD NUMBER [{card_number} DOESNT HAVE ENOUGH BALANCE")
                self.no_balance.setText("YOUR CARD DOEST HAVE ENOUGH BALANCE")
                
            
        else:
            self.no_balance.setText("CARD IS NOT VALID")
    def cancelConfirm(self):
        self.stackedWidget.setCurrentIndex(2)
            
    def go_to_receipt(self):
        save_ToLog(f"GENERATED RECEIPT FOR USER: {self.name}")
        getTotalDays = "SELECT subscription_left FROM users WHERE name=?"
        cursor.execute(getTotalDays, (str(self.name),))
        totalDays = cursor.fetchone()[0]
        self.label_22.setText("NAME: " + str(self.name))
        self.label_23.setText("ADDRESS: " + str(self.address))
        self.label_24.setText("PURCHASED: " + str(int(self.amount)*100))
        self.label_25.setText("SUBSCIPTION: " + str(self.amount) +" DAYS")
        self.label_26.setText("TOTAL DAYS AVAILABLE: " + str(int(totalDays)+int(self.amount)))
        QApplication.processEvents()
        self.stackedWidget.setCurrentIndex(5)
    def back_to_home(self):
        save_ToLog(f"USER {self.name} {self.lname} LOGED OUT..")
        self.textEdit.setText("")
        self.label_5.setText("STATUS:")
        self.pushButton_2.setEnabled(False)
        self.stackedWidget.setCurrentIndex(0)
        
app = QApplication([])
window = mainWindow()
app.exec_()
