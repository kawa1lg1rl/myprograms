from PyQt5.QtCore import *
from PyQt5.QtWidgets import*
from PyQt5.uic import *

class Form(QWidget):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.loginUi()
        
        # test event
        self.login.loginButton.clicked.connect(self.freePass)
        
    def loginUi(self):
        self.login = loadUi("login.ui")
        self.login.show()


    def freePass(self):
        QMessageBox.information(self, "test", "free pass")
        
        self.login.destroy()
        

if __name__ == "__main__":  
    import sys
    
    app = QApplication(sys.argv)
    s = Form()
    
    sys.exit(app.exec_())
    


#pyuic4.exe input.ui -o output.py
