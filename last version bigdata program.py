#!/usr/bin/env python
# coding: utf-8

# In[1]:


from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit,     QPushButton, QTextEdit, QComboBox
from pymongo import MongoClient
from pymongo import ASCENDING, DESCENDING
from tkinter import *

root = Tk()
background = "#132E3C"
root.geometry("1250x700+210+100")
root.config(bg=background)


root.config(bg=background)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Breast Cancer Database GUI")
        self.setGeometry(100, 100, 800, 600)
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.setStyleSheet("background-color: #FADBD8;")
        # Connect to the MongoDB database

        # Create the UI elements

        # self.titleLabel = QLabel("MongoDB GUI", self.centralWidget)
        # self.titleLabel.move(10, 10)
        # self.titleLabel.setFixedWidth(150)
        # self.titleLabel.setFixedHeight(30)

        self.collectionLabel = QLabel("Collection:", self.centralWidget)
        self.collectionLabel.move(100, 50)
        self.collectionLabel.setFixedWidth(150)
        self.collectionLabel.setFixedHeight(30)

        self.collectionLineEdit = QLineEdit(self.centralWidget)
        self.collectionLineEdit.move(170, 50)
        self.collectionLineEdit.setFixedWidth(500)
        self.collectionLineEdit.setFixedHeight(30)
        self.collectionLineEdit.setStyleSheet("background-color: #F7FFF7;")
            
            
        self.queryLabel = QLabel("Query:", self.centralWidget)
        self.queryLabel.move(110, 90)
        self.queryLabel.setFixedWidth(150)
        self.queryLabel.setFixedHeight(30)

        self.queryLineEdit = QLineEdit(self.centralWidget)
        self.queryLineEdit.move(170, 90)
        self.queryLineEdit.setFixedWidth(500)
        self.queryLineEdit.setFixedHeight(30)
        self.queryLineEdit.setStyleSheet("background-color: #F7FFF7;")
        
        
        self.queryButton = QPushButton("Search", self.centralWidget)
        self.queryButton.move(680, 90)
        self.queryButton.setFixedWidth(100)
        self.queryButton.setFixedHeight(30)
        self.queryButton.clicked.connect(self.queryDatabase)
        self.queryButton.setStyleSheet("background-color: #C1BBDD;") 
            
            
        self.insertLabel = QLabel("Insert:", self.centralWidget)
        self.insertLabel.move(110, 130)
        self.insertLabel.setFixedWidth(150)
        self.insertLabel.setFixedHeight(50)

        self.insertTextEdit = QTextEdit(self.centralWidget)
        self.insertTextEdit.move(170, 130)
        self.insertTextEdit.setFixedWidth(500)
        self.insertTextEdit.setFixedHeight(100)
        self.insertTextEdit.setStyleSheet("background-color: #F7FFF7;")

        self.insertButton = QPushButton("Insert", self.centralWidget)
        self.insertButton.move(680, 150)
        self.insertButton.setFixedWidth(100)
        self.insertButton.setFixedHeight(50)
        self.insertButton.clicked.connect(self.insertDocument)
        self.insertButton.setStyleSheet("background-color: #C1BBDD;")

        self.updateLabel = QLabel("Update:", self.centralWidget)
        self.updateLabel.move(110, 240)
        self.updateLabel.setFixedWidth(150)
        self.updateLabel.setFixedHeight(30)

        self.updateQueryTextEdit = QTextEdit(self.centralWidget)
        self.updateQueryTextEdit.move(170, 240)
        self.updateQueryTextEdit.setFixedWidth(500)
        self.updateQueryTextEdit.setFixedHeight(100)
        self.updateQueryTextEdit.setStyleSheet("background-color: #F7FFF7;")

        self.updateTextEdit = QTextEdit(self.centralWidget)
        self.updateTextEdit.move(170, 360)
        self.updateTextEdit.setFixedWidth(500)
        self.updateTextEdit.setFixedHeight(30)
        self.updateTextEdit.setStyleSheet("background-color: #F7FFF7;")
        

        self.updateButton = QPushButton("Update", self.centralWidget)
        self.updateButton.move(680, 260)
        self.updateButton.setFixedWidth(100)
        self.updateButton.setFixedHeight(50)
        self.updateButton.clicked.connect(self.updateDocument)
        self.updateButton.setStyleSheet("background-color: #C1BBDD;")

        self.deleteLabel = QLabel("Delete:", self.centralWidget)
        self.deleteLabel.move(120, 520)
        self.deleteLabel.setFixedWidth(150)
        self.deleteLabel.setFixedHeight(30)

        self.deleteQueryTextEdit = QTextEdit(self.centralWidget)
        self.deleteQueryTextEdit.move(170, 490)
        self.deleteQueryTextEdit.setFixedWidth(500)
        self.deleteQueryTextEdit.setFixedHeight(100)
        self.deleteQueryTextEdit.setStyleSheet("background-color: #F7FFF7;")

        self.deleteButton = QPushButton("Delete", self.centralWidget)
        self.deleteButton.move(680, 510)
        self.deleteButton.setFixedWidth(100)
        self.deleteButton.setFixedHeight(50)
        self.deleteButton.clicked.connect(self.deleteDocument)
        self.deleteButton.setStyleSheet("background-color: #C1BBDD;")

        self.resultTextEdit = QTextEdit(self.centralWidget)
        self.resultTextEdit.move(10, 590)
        self.resultTextEdit.setFixedWidth(770)
        self.resultTextEdit.setFixedHeight(100)
        self.resultTextEdit.setStyleSheet("background-color: #F7FFF7;")

        self.aggregateButton = QPushButton("Aggregate", self.centralWidget)
        self.aggregateButton.move(680, 340)
        self.aggregateButton.setFixedWidth(100)
        self.aggregateButton.setFixedHeight(30)
        self.aggregateButton.clicked.connect(self.aggregateDatabase)
        self.aggregateButton.setStyleSheet("background-color: #C1BBDD;")
        
        

        self.fieldLabel = QLabel("Field:", self.centralWidget)
        self.fieldLabel.move(120, 400)
        self.fieldLabel.setFixedWidth(150)
        self.fieldLabel.setFixedHeight(30)

        self.fieldLineEdit = QLineEdit(self.centralWidget)
        self.fieldLineEdit.move(170, 400)
        self.fieldLineEdit.setFixedWidth(500)
        self.fieldLineEdit.setFixedHeight(30)
        self.fieldLineEdit.setStyleSheet("background-color: #F7FFF7;")
        

        self.orderLabel = QLabel("Order:", self.centralWidget)
        self.orderLabel.move(120, 440)
        self.orderLabel.setFixedWidth(150)
        self.orderLabel.setFixedHeight(30)

        self.orderComboBox = QComboBox(self.centralWidget)
        self.orderComboBox.move(170, 440)
        self.orderComboBox.setFixedWidth(500)
        self.orderComboBox.setFixedHeight(30)
        self.orderComboBox.addItem("Ascending")
        self.orderComboBox.addItem("Descending")
        self.orderComboBox.setStyleSheet("background-color: #F7FFF7;")

        self.indexButton = QPushButton("Index", self.centralWidget)
        self.indexButton.move(680, 400)
        self.indexButton.setFixedWidth(100)
        self.indexButton.setFixedHeight(30)
        self.indexButton.clicked.connect(self.indexDatabase)
        self.indexButton.setStyleSheet("background-color: #C1BBDD;")

        self.aggregateButton = QPushButton("Map reduce", self.centralWidget)
        self.aggregateButton.move(680, 50)
        self.aggregateButton.setFixedWidth(100)
        self.aggregateButton.setFixedHeight(30)
        self.aggregateButton.clicked.connect(self.aggregateDatabase)
        self.aggregateButton.setStyleSheet("background-color: #C1BBDD;")
        
        

    def queryDatabase(self):
        # Retrieve the collection name and query from the line edits
        collection_name = self.collectionLineEdit.text()
        query = self.queryLineEdit.text()

        # Query the MongoDB database
        collection = self.db[collection_name]
        results = collection.find(eval(query))

        # Display the results in the QTextEdit
        self.resultTextEdit.clear()
        for result in results:
            self.resultTextEdit.append(str(result))

    def insertDocument(self):
        # Retrieve the collection name and document from the line edits
        collection_name = self.collectionLineEdit.text()
        doc = eval(self.insertTextEdit.toPlainText())

        # Insert the document into the MongoDB database
        collection = self.db[collection_name]
        result = collection.insert_one(doc)

        # Display the result in the QTextEdit
        self.resultTextEdit.clear()
        self.resultTextEdit.append(f"Inserted document with ID: {result.inserted_id}")

    def updateDocument(self):
        # Retrieve the collection name and query from the line edits
        collection_name = self.collectionLineEdit.text()
        query = self.updateQueryTextEdit.toPlainText()

        # Retrieve the update document from the text edit
        update_doc = eval(self.updateTextEdit.toPlainText())

        # Update the document in the MongoDB database
        collection = self.db[collection_name]
        result = collection.update_one(eval(query), {"$set": update_doc})

        # Display the result in the QTextEdit
        self.resultTextEdit.clear()
        self.resultTextEdit.append(
            f"Matched {result.matched_count} documents and modified {result.modified_count} documents.")

    def deleteDocument(self):
        # Retrieve the collection name and query from the line edits
        collection_name = self.collectionLineEdit.text()
        query = self.deleteQueryTextEdit.toPlainText()

        # Delete the document(s) in the MongoDB database
        collection = self.db[collection_name]
        result = collection.delete_many(eval(query))

        # Display the result in the QTextEdit
        self.resultTextEdit.clear()
        self.resultTextEdit.append(f"Deleted {result.deleted_count} documents.")

    def aggregateDatabase(self):
        # Retrieve the collection name from the line edit
        collection_name = self.collectionLineEdit.text()

        # Aggregate the MongoDB database
        collection = self.db[collection_name]
        pipeline = [
            {"$match": {"view": "CC"}},
            {"$group": {"_id": "$patient_id", "count": {"$sum": 1}}}
        ]
        results = collection.aggregate(pipeline)

        # Display the results in the QTextEdit
        self.resultTextEdit.clear()
        
        for result in results:
            self.resultTextEdit.append(f"{result['_id']}: {result['count']} views")

    def indexDatabase(self):
        # Retrieve the collection name, field, and order from the UI elements
        collection_name = self.collectionLineEdit.text()
        field = self.fieldLineEdit.text()
        order = self.orderComboBox.currentText()

        # Map the order string to the corresponding pymongo constant
        if order == "Ascending":
            order = ASCENDING
        else:
            order = DESCENDING

        # Create the index on the specified field in the specified collection
        collection = self.db[collection_name]
        result = collection.create_index([(field, order)])

        # Display the result in the QTextEdit
        self.resultTextEdit.clear()
        self.resultTextEdit.append(f"Created index: {result}")

    def aggregateDatabase(self):
        # Retrieve the collection name from the line edit
        collection_name = self.collectionLineEdit.text()

        # Aggregate the MongoDB database
        collection = self.db[collection_name]
        pipeline = [
            {"$match": {"view": "CC"}},
            {"$group": {"_id": "$patient_id", "count": {"$sum": 1}}}
        ]
        results = collection.aggregate(pipeline)

        # Display the results in the QTextEdit
        self.resultTextEdit.clear()
        for result in results:
            self.resultTextEdit.append(f"{result['_id']}: {result['count']} views")


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()


# In[ ]:





# In[ ]:




