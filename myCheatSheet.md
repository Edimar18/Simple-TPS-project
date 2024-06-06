# PyQt5 and SQLite Cheat Sheet

This cheat sheet provides a brief overview of commonly used PyQt5 and SQLite functionalities. It's designed to help you quickly reference and implement these features in your Python application.

## PyQt5

### Importing PyQt5 Modules

```python
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QPushButton, QLineEdit, QTextEdit, QInputDialog, QMessageBox, QStackedWidget
from PyQt5.QtCore import QResource, QSize
from PyQt5.QtGui import QPixmap
```

### Loading UI Files

```python
import uic
uic.loadUi("mainUI.ui", self)  # Load UI file into a widget
```

### Setting Widget Properties

```python
self.setWindowTitle("My App")  # Set window title
self.label.setText("Hello, PyQt5!")  # Set label text
self.pushButton.clicked.connect(self.my_function)  # Connect button click event to a function
self.textEdit.textChanged.connect(self.my_function)  # Connect text edit change event to a function
```

### Creating Dialogs

```python
result = QInputDialog.getText(self, "Input Dialog", "Enter your name:")  # Get text input from user
QMessageBox.information(self, "Information", "This is an information message.")  # Show information message
```

### Working with Stacked Widgets

```python
self.stackedWidget.setCurrentIndex(1)  # Switch to the second widget in the stack
```

## SQLite

### Importing SQLite Module

```python
import sqlite3
```

### Connecting to a Database

```python
database = sqlite3.connect("my_database.db")  # Connect to a SQLite database
cursor = database.cursor()  # Create a cursor object
```

### Creating a Table

```python
create_table_query = """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL
);
"""
cursor.execute(create_table_query)  # Execute the query
```

### Inserting Data

```python
insert_query = "INSERT INTO users (name, email) VALUES (?,?)"
cursor.execute(insert_query, ("John Doe", "johndoe@example.com"))  # Execute the query with parameters
database.commit()  # Commit the changes
```

### Updating Data

```python
update_query = "UPDATE users SET email =? WHERE id =?"
cursor.execute(update_query, ("newemail@example.com", 1))  # Execute the query with parameters
database.commit()  # Commit the changes
```

### Deleting Data

```python
delete_query = "DELETE FROM users WHERE id =?"
cursor.execute(delete_query, (1,))  # Execute the query with parameters
database.commit()  # Commit the changes
```

### Selecting Data

```python
select_query = "SELECT * FROM users WHERE name =?"
cursor.execute(select_query, ("John Doe",))  # Execute the query with parameters
rows = cursor.fetchall()  # Fetch all rows
for row in rows:
    print(row)
```

### Closing the Database Connection

```python
database.close()  # Close the database connection
```

I hope this cheat sheet helps you in your PyQt5 and SQLite presentation! Let me know if you have any further questions.