from views import *
from model import *
from trip import *
import sys
from app_ui import *
from painting_dial import *



class TripController( Ui_Dialog):
    def __init__(self, MainWindow,db):
        super().__init__(MainWindow)
        self.db = db
        self.columns = ' '
        self.pushButton.clicked.connect(self.get_values_call)
    
    def get_values_call(self):
        self.db.getValues(self)

class Controller(Ui_Database):
    
    def gen_values_call(self):
        self.db.gen_values(self)
            

    def __init__(self, MainWindow):
        self.ui = Ui_Database(MainWindow)
        self.db = Database()
        super().__init__(MainWindow)

        self.pushButton.clicked.connect(self.saveInfo)
        
        self.comboTable = None
        self.comboAction = None
        self.textAction = None
        self.columns = ' '
        self.full_text = ''
        self.full_search_table = ''
        self.Flag = True
        self.window = QtWidgets.QDialog(MainWindow)
        self.ui = TripController(self.window, self.db)

    def saveInfo(self):
        self.comboAction = self.action.currentText()
        self.comboTable = self.table.currentText()
        self.textAction = self.textEdit.toPlainText()
        self.db.requestFormat(self.comboTable, self.comboAction, self.textAction, self)
        if not self.Flag:
            self.error_dialog = QtWidgets.QErrorMessage()
            self.error_dialog.showMessage('Unable to perceive the request')
    def showDialog(self):
        self.window.show()


    def full_str_call(self):
        self.db.full_string(self)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    MainWindow.show()
    cntr = Controller(MainWindow)

    sys.exit(app.exec_())


