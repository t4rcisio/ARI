
from PyQt6 import QtWidgets, QtCore
from pages import main_page, home, newIA, edit, train, alert
import sys
from utils import storeManager
from PyQt6.QtCore import QTimer

class Main_Page:


    def show(self):

        app = QtWidgets.QApplication(sys.argv)
        self.mainWidget = QtWidgets.QWidget()
        self.main_page = main_page.Ui_Form()
        self.main_page.setupUi(self.mainWidget)

        self.store = storeManager.StoreManager()
        self.__configPages()
        self.__connections()
        self.main_page.stackedWidget.setCurrentIndex(0)

        self.mainWidget.show()
        sys.exit(app.exec())

    def __configPages(self):
        
        # HOME
        self.homeWidget = QtWidgets.QWidget()
        self.homePage = home.Ui_Form()
        self.homePage.setupUi(self.homeWidget)
        self.main_page.stackedWidget.insertWidget(0, self.homeWidget)

    def __pageGen(self, index):
        
        if index == 1:

            # NEW MODEL
            self.newWidget = QtWidgets.QWidget()
            self.newIaPage = newIA.Ui_Form()
            self.newIaPage.setupUi(self.newWidget)
            self.main_page.stackedWidget.insertWidget(1, self.newWidget)

        elif index == 2:

            # EDIT MODEL
            self.editWidget = QtWidgets.QWidget()
            self.editIaPage = edit.Ui_Form()
            self.editIaPage.setupUi(self.editWidget)
            self.main_page.stackedWidget.insertWidget(2, self.editWidget)


        elif index == 3:

            # EDIT MODEL
            self.train = train.Train()
            self.trainWidget = self.train.build()
            
            self.main_page.stackedWidget.insertWidget(3, self.trainWidget)
    


    def __connections(self):

        self.store.alertTrigger(None)
        
        self.main_page.pushButton.clicked.connect(lambda state: self.__clearPage(0))

        self.homePage.pushButton.clicked.connect(lambda state: self.__switchPage(0)) # CONSOLE
        self.homePage.pushButton_2.clicked.connect(lambda state: self.__switchPage(1)) # NEW MODEL
        self.homePage.pushButton_3.clicked.connect(lambda state: self.__switchPage(3)) # MODEL TRAIN
        self.homePage.pushButton_4.clicked.connect(lambda state: self.__switchPage(2)) # MODEL EDITOR

        self.timer = QTimer()
        self.timer.timeout.connect(self.__alertEvent)
        self.timer.start(1000)  # Trigger event every 1000 ms (1 second)


    def __clearPage(self, index):
        self.store.tempConfig(None)
        self.__switchPage(index)

    def __switchPage(self, index):
        
        self.__pageGen(index)
        self.main_page.stackedWidget.setCurrentIndex(index)
        print(index)


    def __alertEvent(self):

        data = self.store.alertTrigger()
        if data != None:

            message = data["MESSAGE"]
            if message != None:
                self.__alertPopup(message)
            
            operation = data["OP"]
            if operation == "GO HOME":
                self.__clearPage(0)

            self.store.alertTrigger(None)


    def __alertPopup(self, message):

        self.alertPopup = QtWidgets.QWidget()
        self.alertPage = alert.Ui_Form()
        self.alertPage.setupUi(self.alertPopup)
        self.alertPage.label.setText(message["MESSAGE"])
        self.alertPopup.setWindowTitle(message["TITLE"])
        self.alertPopup.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)
        self.alertPopup.show()


if __name__ == "__main__":

    page = Main_Page()
    page.show()