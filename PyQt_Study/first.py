# -*- coding: utf8 -*-
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class Form(QWidget):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        nameLabel = QLabel("Name : ")
        
        self.nameLine = QLineEdit()
        self.nameLine.setMinimumSize(200,150)
        self.submitButton = QPushButton("Show Text")
        self.showResult = QTextEdit()
        self.showResult.setReadOnly(True)
        self.showResult.resize(100,100)

        buttonLayout1 = QVBoxLayout()
        buttonLayout1.addWidget(nameLabel)
        buttonLayout1.addWidget(self.nameLine)
        buttonLayout1.addWidget(self.submitButton)
        self.setFixedSize(300,500)
        layout1 = QVBoxLayout()

        layout1.addWidget(self.showResult)
        
        self.submitButton.clicked.connect(self.submitContact)

        mainLayout = QVBoxLayout()
        # mainLayout.addWidget(nameLabel, 0, 0)
        mainLayout.addLayout(buttonLayout1)
        mainLayout.addLayout(layout1)
        self.setLayout(mainLayout)
        self.setWindowTitle("Hello Qt")

    def submitContact(self):
        name = self.nameLine.text()

        if name == "":
            QMessageBox.information(self, "Empty Field", "Please enter a name and address.")
            return
        else:
            temp = " ============== "
            temp += " Result "
            temp += " ============== \n"
            temp += self.nameLine.text()
            self.showResult.setText(temp)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)

    screen = Form()
    screen.show()

    sys.exit(app.exec_())

