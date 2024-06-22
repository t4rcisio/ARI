

import os
from pages import train_page
from utils import storeManager,tools
from PyQt6 import QtWidgets, QtCore
from threads import threads
from PyQt6.QtGui import QMovie, QIcon



class Train:


    def build(self):
        
        self.storeManager = storeManager.StoreManager()
        self.classList = None
        self.tools = tools.Tools()

        self.trainWidget = QtWidgets.QWidget()
        self.trainIaPage = train_page.Ui_Form()
        self.trainIaPage.setupUi(self.trainWidget)

        self.__initLabels()

        return self.trainWidget

    def __initLabels(self):

        self.trainIaPage.comboBox_3.clear()
        itens = self.storeManager.modelParams()

        if itens != None:

            itens = ["SELECT"] + list(itens.keys())
        else:
            itens = ["SELECT"]

        self.trainIaPage.comboBox_3.addItems(itens)
        self.trainIaPage.comboBox_3.currentIndexChanged.connect(self.__updateData)

        self.scrollArea = QtWidgets.QScrollArea()
        self.textLog = QtWidgets.QTextEdit()

        self.scrollArea.setWidgetResizable(True)
        self.trainIaPage.tabWidget.clear()

        self.trainIaPage.tabWidget.addTab(self.textLog, "CONSOLE")
        self.__downloadPage()
        #self.trainIaPage.tabWidget.addTab(self.scrollArea, "CLASSES")

        self.trainIaPage.input_epoch.setEnabled(False)
        self.trainIaPage.input_split.setEnabled(False)
        self.trainIaPage.opmodetg.setEnabled(False)
        self.trainIaPage.opmodetg.setChecked(False)
        self.trainIaPage.genDataset_info.setVisible(False)

        #self.trainIaPage.input_model_type_2.mousePressEvent = lambda state, w=self.trainIaPage.input_model_type_2: self._getFilePath(w, 'Pickle Files (*.pkl)')
        self.trainIaPage.datasetname_input.setEnabled(False)
        self.trainIaPage.input_model_type.setReadOnly(True)

        self.trainIaPage.genDataset_button.clicked.connect(lambda state: self.__generateDataset())

        #self.trainIaPage.save_button.clicked.connect(lambda state: self.)

        self.queueDownload = {}

    def __trainData(self):

        if len(self.queueDownload) == 0:
            self.__msgBox("SELET CLASSES TO TRAIN")
            return

        epochs = self.trainIaPage.input_epoch.text()
        split_rate = self.trainIaPage.input_split.text()

        try:      
            epochs = int(float(epochs))
            if epochs <= 0:
                self.__msgBox("EPOCHS PARAM MUST BE GREATER THAN 0")
                return
        except:
            self.__msgBox("EPOCHS PARAM MUST BE INTERGER")
            return
    
        try:      
            epochs = float(split_rate)
            if epochs < 0.01 or epochs > 0.99:
                self.__msgBox("SPLIT RATE PARAM MUST BE  0.1 > X < 0.99")
                return
        except:
            self.__msgBox("SPLIT RATE PARAM MUST BE FLOAT")
            return



    def __generateDataset(self):

        if len(self.queueDownload) == 0:
            self.__msgBox("SELET CLASSES TO TRAIN")
            return

        datasetName = self.trainIaPage.datasetname_input.text()

        if not self.tools.is_valid_filename(datasetName):
            self.__msgBox("SET A VALID FILE NAME")
            return
        
        if self.trainIaPage.comboBox_4.currentText() == "NEW":
            opMode = "NEW"
        else:
            if self.trainIaPage.opmodetg.isChecked():
                opMode = "APPEND"


        paths = []
        classes = []
        for item in self.queueDownload:
            paths.append(self.queueDownload[item]["ARGS"]["FOLDER_INPUT"])
            classes.append(self.queueDownload[item]["C_NAME"])

        payload = {
                "OP": "GENERATE DATASET",
                "ARGS":{
                    "PATHS": paths,
                    "CLASS": classes,
                    "DATASETNAME": datasetName,
                    "MODE": opMode
                }
            }

        self.storeManager.args(payload)

        self.th = threads.ThreadService()
        self.th.run(self.__beginDataset, self.__endDataset, progress=self.__progress_dataset)

    def __beginDataset(self):

        print("START")
        self.trainIaPage.genDataset_info.setVisible(True)

    def __endDataset(self):

        print("END")
        self.trainIaPage.genDataset_info.setVisible(False)
    
    def __progress_dataset(self):
        
        text = self.storeManager.msgBroadcast()

        if text != False and text != None:
            self.trainIaPage.genDataset_info.setText('<html><head/><body><p align="center"><span style=" color:#ffffff;">'+text+'</span></p></body></html>')


    def __downloadPage(self):

        lWidget = QtWidgets.QWidget()
        lLayout = QtWidgets.QVBoxLayout(lWidget)

        self.vSelect = QtWidgets.QCheckBox()
        self.vSelect.setText("SELECT ALL")
        self.vSelect.setStyleSheet('color:#ffffff;')
        self.vSelect.stateChanged.connect(lambda state,: self.__selectAllControl(state))

        self.downloadButton = QtWidgets.QPushButton()

        self.downloadButton.setText("DOWNLOAD SELECTED")
        self.downloadButton.clicked.connect(lambda state: self.__downloadSelected())
        self.downloadButton.setStyleSheet('''QPushButton {
                background-color: #007bff;
                color: #fff;
                border: 2px solid #007bff;
                border-radius: 5px;
                padding: 7px 10px;
            }
            QPushButton:hover {
                background-color: #0056b3;
                border: 2px solid #0056b3;
            }''')
        
        self.downloadButton.clicked.connect(lambda state: self.__downloadData())


        self.pWidgetDw = QtWidgets.QWidget()
        pLayout = QtWidgets.QHBoxLayout(self.pWidgetDw )
        pLayout.setContentsMargins(0,0,0,0)

        self.movieGif_dw = QMovie("./images/loading_dw.gif")
        self.movieGif_dw.setScaledSize(QtCore.QSize(60, 60))
        self.pLabel2Gif_dw = QtWidgets.QLabel()
        self.pLabel2Gif_dw.setMovie(self.movieGif_dw)
        self.pLabel2Gif_dw.setFixedSize(60,60)
        self.movieGif_dw.start()

        self.textThDw = QtWidgets.QLabel()
        self.textThDw.setText('<html><head/><body><p><span style=" color:#ffffff;">DOWNLOADING DOG | 50/5000</span></p></body></html>')

        pLayout.addWidget(self.pLabel2Gif_dw)
        pLayout.addWidget(self.textThDw)


        lLayout.addWidget(self.vSelect)
        lLayout.addWidget(self.downloadButton)
        lLayout.addWidget(self.pWidgetDw)
        lLayout.addWidget(self.scrollArea)

        self.pWidgetDw.setVisible(False)
        self.trainIaPage.tabWidget.addTab(lWidget, "CLASSES")

    def __downloadSelected(self):

        print("OKOK")

    def __updateData(self, index):

        if index == 0:
            self.__clearLabels()
            return

        currentText = self.trainIaPage.comboBox_3.currentText()

        data = self.storeManager.modelParams()[currentText]

        self.trainIaPage.comboBox_4.clear()
        self.trainIaPage.comboBox_4.addItems(["SELECT"] + data["TRAIN_VERSIONS"] + ["NEW"])
        self.trainIaPage.comboBox_4.currentIndexChanged.connect(self.__updateClassesView)
        self.queueDownload = {}
        self.__showClass()

        currentText = self.trainIaPage.comboBox_3.currentText()
        data = self.storeManager.modelParams()[currentText]

        self.trainIaPage.textEdit.setText(data["MODEL_DESC"])
        self.trainIaPage.textEdit.setReadOnly(True)
        self.trainIaPage.input_model_type.setText(data["MODEL_TYPE"])
        self.trainIaPage.textEdit.setReadOnly(True)
        

    def __updateClassesView(self, index):

        if index <= 0:
            self.trainIaPage.input_epoch.setEnabled(False)
            self.trainIaPage.input_split.setEnabled(False)
            self.trainIaPage.opmodetg.setEnabled(False)
            self.trainIaPage.opmodetg.setChecked(False)
            self.__clearSub()
            return
        if self.trainIaPage.comboBox_4.currentText() == "NEW":
            self.trainIaPage.input_epoch.setEnabled(True)
            self.trainIaPage.input_split.setEnabled(True)
            self.trainIaPage.opmodetg.setEnabled(False)
            self.trainIaPage.opmodetg.setChecked(False)


        currentText = self.trainIaPage.comboBox_3.currentText()
        data = self.storeManager.modelParams()[currentText]
        version = self.trainIaPage.comboBox_4.currentText()
        self.trainIaPage.datasetname_input.setEnabled(True)

        if version != "NEW":
            self.trainIaPage.opmodetg.setEnabled(True)
            self.trainIaPage.input_epoch.setEnabled(False)
            self.trainIaPage.input_split.setEnabled(False)
            self.trainIaPage.input_epoch.setText(data["TRAIN_VERSIONS"][version]["EPOCH"])
            self.trainIaPage.input_split.setText(data["TRAIN_VERSIONS"][version]["EPOCH"])
            self.textLog.setText(data["TRAIN_VERSIONS"][version]["LOG"])
             

    def __updateLogView(self):

        pass

    def __clearLabels(self):

         self.trainIaPage.textEdit.setText("")
         self.trainIaPage.input_model_type.setText('')
         self.__clearLayout(self.classList)
         self.scrollArea.setWidget(QtWidgets.QWidget())
         self.trainIaPage.comboBox_4.setCurrentIndex(0)
         self.__clearSub()

    def __clearSub(self):
        
        self.trainIaPage.input_epoch.setText("")
        self.trainIaPage.input_split.setText("")
        self.textLog.setText("")


    def __showClass(self):
        
        currentText = self.trainIaPage.comboBox_3.currentText()
        storage = self.storeManager.modelParams()[currentText]

        rClass = QtWidgets.QWidget()
        self.classList = QtWidgets.QVBoxLayout(rClass)
        self.classList.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
        self.classList.setContentsMargins(3,9,3,9)
        self.classList.setSpacing(12)

        self.__clearLayout(self.classList)
        self.qselectItemList = []

        index = 0        
        for item in storage["CLASSES"]:

            qWidget = QtWidgets.QWidget()
            qWidget.setStyleSheet("background-color: rgb(68, 68, 68);border-radius:10px;")
            qLayout = QtWidgets.QVBoxLayout(qWidget)
            qLayout.setAlignment(QtCore.Qt.AlignmentFlag.AlignVCenter)
            qLayout.setContentsMargins(9,3,9,9)
            qLayout.setSpacing(0)
            

            self.qselectItemList.append(QtWidgets.QCheckBox())
            self.qselectItemList[-1].stateChanged.connect(lambda state, item=item, i=index: self.__selectionControl(state, item,i))

            qCname = QtWidgets.QLabel()
            qCname.setWordWrap(True)
            rCname = '<html><head/><body><p><span style=" font-size:8pt; color:#ffffff;">CLASS NAME: '+str(item["C_NAME"])+'</span></p></body></html>'
            qCname.setText(rCname)
            qCname.setMinimumHeight(20)

            qCtype = QtWidgets.QLabel()
            qCtype.setWordWrap(True)
            rCtype = '<html><head/><body><p><span style=" font-size:8pt; color:#ffffff;">CLASS TYPE: '+str(item["TYPE"])+'</span></p></body></html>'
            qCtype.setText(rCtype)
            qCtype.setMinimumHeight(20)


            if os.path.exists(item['ARGS']["FOLDER_INPUT"]):
                content = len(os.listdir(item['ARGS']["FOLDER_INPUT"]))
            else:
                content = "Empty"


            qContent = QtWidgets.QLabel()
            qContent.setWordWrap(True)
            rContent = '<html><head/><body><p><span style=" font-size:8pt; color:#ffffff;">FOLDER CONTENT: '+str(content)+'</span></p></body></html>'
            qContent.setText(rContent)
            qContent.setMinimumHeight(20)

            qLayout.addWidget(self.qselectItemList[-1])
            qLayout.addWidget(qCname)
            qLayout.addWidget(qCtype)
            qLayout.addWidget(qContent)

            wList = []
            for arg in item['ARGS']:

                wList.append(QtWidgets.QLabel())
                wList[-1].setWordWrap(True)
                rCtype = '<html><head/><body><p><span style=" font-size:8pt; color:#ffffff;">'+str(arg)+': '+str(item["ARGS"][arg])+'</span></p></body></html>'
                wList[-1].setText(rCtype)
                wList[-1].setMinimumHeight(20)
                qLayout.addWidget(wList[-1])


            sWidget = QtWidgets.QWidget()
            sLayout = QtWidgets.QHBoxLayout(sWidget)
            sLayout.setContentsMargins(0,9,0,0)
            sLayout.setSpacing(12)

            if item["TYPE"] == "WEB IMAGES":

                delButton = QtWidgets.QPushButton()
                delButton.setStyleSheet("background-color: #ff4b3e;border-radius:5px;")
                delButton.setMinimumHeight(20)
                delButton.setText("CLEAR FOLDER")
                delButton.clicked.connect(lambda state, x=item["ARGS"]["FOLDER_INPUT"]: self.__clearFolder(x))

                editButton = QtWidgets.QPushButton()
                editButton.setStyleSheet("background-color: #ffde23;border-radius:5px;")
                editButton.setText("OPEN FOLDER")
                editButton.setMinimumHeight(20)
                editButton.clicked.connect(lambda state, x=item["ARGS"]["FOLDER_INPUT"]: self.__openFolder(x))

                sLayout.addWidget(delButton)
                sLayout.addWidget(editButton)

            qLayout.addWidget(sWidget)

            self.classList.addWidget(qWidget)
            index+=1

        self.scrollArea.setWidget(rClass)

    def __clearFolder(self, path):


        if self.confirmation_popup(str(path)+"\n\nDo you really want delete all data in this folder? ") == True:

            payload = {
                "OP": "CLEAR FOLDER",
                "ARGS": path,
            }

            self.storeManager.args(payload)

            self.th = threads.ThreadService()
            self.th.run(self.__begin, self.__end, progress=self.__progress_downloadingData)


    def __openFolder(self, path):


        try:
            os.startfile(path)
        except Exception as e:
            print(e)
            self.__msgBox("THIS FOLDER DOES'T EXIST OR IS INACCESIBLE")


    
    def confirmation_popup(self, message):
        msg_box = QtWidgets.QMessageBox()
        msg_box.setWindowTitle("ARI - Confirmation")
        msg_box.setText(message)
        msg_box.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No)
        msg_box.setIcon(QtWidgets.QMessageBox.Icon.Question)

        result = msg_box.exec()

        return result == QtWidgets.QMessageBox.StandardButton.Yes 
    
    def __selectionControl(self, state, item, index):
        
        if state == 2:
            self.queueDownload[index] = item
        else:
            del self.queueDownload[index]

    def __selectAllControl(self, state):

            if state == 2:
                for item in self.qselectItemList:
                    item.setChecked(True)
            else:
                for item in self.qselectItemList:
                    item.setChecked(False)

    def _getFilePath(self, element, type):
        
        file_dialog = QtWidgets.QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self.trainWidget, 'Open File', '', type)

        if file_path != "":
            element.setText(file_path)




    def __downloadData(self):
        
        payload = {
            "OP": "IMAGE DOWNLOADER",
            "ARGS": self.queueDownload,
        }

        self.storeManager.args(payload)

        self.th = threads.ThreadService()
        self.th.run(self.__begin, self.__end, progress=self.__progress_downloadingData)


    def __begin(self):
        self.downloadButton.setText("STOP DOWNLOADING")
        self.pWidgetDw.setVisible(True)

    def __end(self):
        self.downloadButton.setText("DOWNLOAD SELECTED")
        self.__showClass()
        self.pWidgetDw.setVisible(False)
        self.__msgBox("DOWNLOAD COMPLETED!")

    def __progress_downloadingData(self):
        
        text = self.storeManager.msgBroadcast()

        if text != False and text != None:

            self.textThDw.setText('<html><head/><body><p><span style=" color:#ffffff;">'+str(text)+'</span></p></body></html>')
        
        

    def __clearLayout(self, layoutElement):
         
        try:
            while layoutElement.count() > 0:
                item = layoutElement.takeAt(0)
                if item.widget():
                    item.widget().deleteLater
        except:
            pass
    
    def __msgBox(self, message, title="ARI"):
        messageBox = QtWidgets.QMessageBox()
        messageBox.setWindowTitle(title)
        messageBox.setText(message)
        icon = QIcon('.\\ui\\../images/logo.png')
        messageBox.setWindowIcon(icon)
        messageBox.exec()