# Form implementation generated from reading ui file './ui/edit.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from utils import storeManager
from pages import newIA_st1, newIA_st2, alert
from utils import storeManager
import datetime

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1092, 675)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(parent=Form)
        self.frame.setStyleSheet("background-color: rgb(0, 0, 0)")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget = QtWidgets.QWidget(parent=self.frame)
        self.widget.setMaximumSize(QtCore.QSize(16777215, 50))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget_3 = QtWidgets.QWidget(parent=self.widget)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(parent=self.widget_3)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.horizontalLayout.addWidget(self.widget_3)
        self.widget_4 = QtWidgets.QWidget(parent=self.widget)
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_4)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.comboBox = QtWidgets.QComboBox(parent=self.widget_4)
        self.comboBox.setStyleSheet("QComboBox {\n"
"    background-color:rgb(68, 68, 68) ;\n"
"    color: rgb(255, 255, 255);\n"
"    border: 2px solid #555;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 0px;\n"
"}\n"
"QListView\n"
"{\n"
"background-color : rgb(68, 68, 68);;\n"
"}\n"
"")
        self.comboBox.setObjectName("comboBox")
        self.verticalLayout_3.addWidget(self.comboBox)
        self.horizontalLayout.addWidget(self.widget_4)
        self.verticalLayout_2.addWidget(self.widget)
        self.stackedWidget = QtWidgets.QStackedWidget(parent=self.frame)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget.addWidget(self.page_2)
        self.verticalLayout_2.addWidget(self.stackedWidget)
        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.__loadModels()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:18pt; color:#ffffff;\">EDIT IA MODEL</span></p></body></html>"))



    def __loadModels(self):

        self.store = storeManager.StoreManager()
        storage = self.store.tempConfig(None)

        pmodel = self.store.modelParams()

        if pmodel != None:
            models = pmodel
            self.__nonePage("./images/ia_folder.png", "SELECT A MODEL TO EDIT")
            self.comboBox.currentIndexChanged.connect(self.__chageEdit)
        else:
            models = {}


        if len(models) > 0:

            itens = ["SELECT"]+list(models.keys())
            self.comboBox.addItems(itens)
        else:
            self.__nonePage("./images/no-search-found.png", "NO MODELS FOUND")

    def __chageEdit(self, index):
        
        target = self.comboBox.currentText()

        if index == 0:
            self.__nonePage("./images/ia_folder.png", "SELECT A MODEL TO EDIT")
            self.label.setText('<html><head/><body><p><span style=" font-size:18pt; color:#ffffff;">EDIT IA MODEL</span></p></body></html>')
        else:
            self.__loadPages(target)
            self.label.setText("<html><head/><body><p><span style=\" font-size:18pt; color:#ffffff;\">EDIT IA MODEL  | "+str(target)+"</span></p></body></html>")
    
    def __nonePage(self, image_path, text):

        rPage = QtWidgets.QWidget()
        rLayout = QtWidgets.QVBoxLayout(rPage)
        rLayout.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)
        rLayout.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        image_label = QtWidgets.QLabel()
        pixmap = QtGui.QPixmap(image_path)
        pixmap = pixmap.scaled(300, 300)
        image_label.setPixmap(pixmap)

        rlabel = QtWidgets.QLabel()
        rlabel.setText('<html><head/><body><p align="center"><span style=" font-size:18pt;color:#9a9da0;">'+text+'</span></p></body></html>')

        rLayout.addWidget(image_label)
        rLayout.addWidget(rlabel)

        self.stackedWidget.insertWidget(0, rPage)
        self.stackedWidget.setCurrentIndex(0)


    def __loadPages(self, taget):

        self.page_step1 = QtWidgets.QWidget()
        self.newIA_st1 = newIA_st1.Ui_Form()
        self.newIA_st1.setupUi(self.page_step1)
        self.store.tempConfig(None)
        self.currentTextButton = ""

        self.currentModel = self.store.modelParams()[taget]
        self.store.tempConfig(self.currentModel)
        
        self.page_step2 = QtWidgets.QWidget()
        self.newIA_st2 = newIA_st2.Ui_Form()
        self.newIA_st2.setupUi(self.page_step2)

        self.stackedWidget.insertWidget(0, self.page_step1)
        self.stackedWidget.insertWidget(1, self.page_step2)

        self.stackedWidget.setCurrentIndex(0)

        self.__loadScrollArea()

        comboItens = list(self.cTypes.keys())
        self.newIA_st2.comboBox.clear()
        self.newIA_st2.comboBox.addItems(comboItens)
        self.newIA_st2.comboBox.setCurrentIndex(0)
        self.__classTypes(comboItens[0])

        self.alert = QtWidgets.QWidget()
        self.alertWidget = alert.Ui_Form()
        self.alertWidget.setupUi(self.alert)
        self.alert.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)


        self.newIA_st2.scrollArea.setWidgetResizable(True)
        self.__setConnections()
       
    def __setConnections(self):

        self.editId = None

        self.newIA_st1.next_button.clicked.connect(lambda state: self.__checkParamsPage1())
        self.newIA_st2.back_button.clicked.connect(lambda state: self.__previusPage())
        self.newIA_st1.delete_button.clicked.connect(lambda state: self.__deleteButton())

        self.grid = [self.newIA_st1.textClassification, self.newIA_st1.faceClassification, self.newIA_st1.imageClassification, self.newIA_st1.voiceClassification]

        self.newIA_st1.textClassification.clicked.connect(lambda state: self.__modelgrid(0))
        self.newIA_st1.faceClassification.clicked.connect(lambda state: self.__modelgrid(1))
        self.newIA_st1.imageClassification.clicked.connect(lambda state: self.__modelgrid(2))
        self.newIA_st1.voiceClassification.clicked.connect(lambda state: self.__modelgrid(3))

        self.newIA_st2.comboBox.currentIndexChanged.connect(self.__sourceTypeControl)
        self.newIA_st2.save_button.clicked.connect(lambda statte: self.__saveButton())
        self.newIA_st2.cancel_button.clicked.connect(lambda state: self.__clearInputs())
        self.newIA_st2.finish_button.clicked.connect(lambda state: self.__saveModel())

        self.__fillFirstPage()

    def __fillFirstPage(self):

        self.newIA_st1.input_name.setText(self.currentModel['MODEL_NAME'])
        self.newIA_st1.input_description.setPlainText(self.currentModel["MODEL_DESC"])

        for index in range(0, len(self.grid)):
            if self.grid[index].text() == self.currentModel["MODEL_TYPE"]:
                self.grid[index].setChecked(True)
                self.__modelgrid(index)


    def confirmation_popup(self, message):
        msg_box = QtWidgets.QMessageBox()
        msg_box.setWindowTitle("Confirmation")
        msg_box.setText(message)
        msg_box.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No)
        msg_box.setIcon(QtWidgets.QMessageBox.Icon.Question)

        result = msg_box.exec()

        return result == QtWidgets.QMessageBox.StandardButton.Yes 


    def __deleteButton(self):


        if self.confirmation_popup("Do you really want delete this model? ") == True:
        
            models = self.store.modelParams()
            currentModel = self.newIA_st1.input_name.text()


            if models != None:
                if  currentModel in models:
                    del models[currentModel]
                    self.store.modelParams(models)
                    self.store.alertTrigger({
                    "MESSAGE": {
                        "MESSAGE": "MODEL DELETED!",
                        "TITLE": "EDIT MODEL",
                        "IMG": "./images/ia_saved.png"}, 
                    "OP": "GO HOME"})

            

    def __saveModel(self):


        storage = self.store.tempConfig()

        if len(storage["CLASSES"]) >=1:

            models = self.store.modelParams()
            if models  == None:
                models = {}

            storage["MODIFIED_AT"] = str(datetime.datetime.now())
            models[storage["MODEL_NAME"]] = storage

            self.store.modelParams(models)
            self.store.tempConfig(None)
            self.__clearInputs()
            self.store.alertTrigger({
                "MESSAGE": {
                    "MESSAGE": "THE MODEL WAS SAVED!",
                    "TITLE": "EDIT MODEL",
                    "IMG": "./images/ia_saved.png"}, 
                "OP": None})

        else:
            self.store.alertTrigger({
                "MESSAGE": {
                    "MESSAGE": "THE MODEL MUST HAVE AT LEAST ONE CLASS!",
                    "TITLE": "EDIT MODEL",
                    "IMG": "./images/alert-icon.png"}, 
                "OP": None})

            

    def __modelgrid(self, target):

        targetStatus = self.grid[target].isChecked()
        self.currentTextButton = self.grid[target].text()

        if targetStatus == True:

            for index in range(0, len(self.grid)):

                if self.grid[index].isChecked() and index != target:
                    self.grid[index].setChecked(False)


    def __checkParamsPage1(self):

        modelName = str(self.newIA_st1.input_name.text()).strip()
        modelDesc = str(self.newIA_st1.input_description.toPlainText()).strip()
        status = True
        alertMsg = '<span style=" color:#ff0000;"> * Required</span>'


        if modelName == "":
            self.newIA_st1.label_2.setText('<html><head/><body><p><span style=" color:#ffffff;">MODEL NAME</span>'+alertMsg+'</p></body></html>')
            status = False
        else:
            self.newIA_st1.label_2.setText('<html><head/><body><p><span style=" color:#ffffff;">MODEL NAME</span></p></body></html>')

        if modelDesc == "":
            self.newIA_st1.label_3.setText('<html><head/><body><p><span style=" color:#ffffff;">DESCRIPTION </span>'+alertMsg+'</p></body></html>')
            status = False
        else:
            self.newIA_st1.label_3.setText('<html><head/><body><p><span style=" color:#ffffff;">DESCRIPTION </span></p></body></html>')

        res = any(item.isChecked() == True for item in self.grid)
        
        if not res:
            self.newIA_st1.label_4.setText('<html><head/><body><p align="center"><span style=" font-size:18pt; color:#ffffff;">MODEL TYPE</span>'+alertMsg+'</p></body></html>')
        else:
            self.newIA_st1.label_4.setText('<html><head/><body><p align="center"><span style=" font-size:18pt; color:#ffffff;">MODEL TYPE</span></p></body></html>')

        
        if  res and status:
            self.label.setText("<html><head/><body><p><span style=\" font-size:18pt; color:#ffffff;\">EDIT IA MODEL  | "+str(modelName)+"</span></p></body></html>")

            storage = self.store.tempConfig()
            if storage == None:
                storage = {

                    "MODEL_NAME": "",
                    "MODEL_DESC": "", 
                    "MODEL_TYPE": "",
                    "CLASSES":[]
                }
                
            storage["MODEL_NAME"] = modelName
            storage["MODEL_DESC"] = modelDesc
            storage["MODEL_TYPE"] = self.currentTextButton

            self.store.tempConfig(storage)

            self.__nextpage()
            self.__includeClass()


    def __sourceTypeControl(self, index):

        self.__clearLayout(self.qLayout)

        selected_text = self.newIA_st2.comboBox.currentText()
        self.__classTypes(selected_text)

    def __saveButton(self):

        alertMsg = '<span style=" color:#ff0000;"> * Required</span>'
        invalid = False

        storage = self.store.tempConfig()


        if len(storage["CLASSES"]) == 0:
            rId = 0
        else:
            rId = storage["CLASSES"][-1]["ID"] + 1 

        payload = {
            "ID": rId,
            "C_NAME": self.newIA_st2.input_name.text(),
            "TYPE": self.newIA_st2.comboBox.currentText(),
            "ARGS": {}
        }

        rdata = {}
        for item in self.inputList:

            rdata[item.objectName()]  = item.text()

            if str(item.text()).replace(" ", "") == "":
                invalid = True


        if payload["C_NAME"] == "" or invalid:
            self.newIA_st2.label_2.setText('<html><head/><body><p><span style=" color:#ffffff;">CLASS NAME</span>'+alertMsg+'</p></body></html>')
        else:
            self.newIA_st2.label_2.setText('<html><head/><body><p><span style=" color:#ffffff;">CLASS NAME</span></p></body></html>')
            payload["ARGS"] = rdata

            if self.editId == None:
                storage["CLASSES"].append(payload)
            else:
                storage["CLASSES"][self.__searchClassID(self.editId)] = payload

            self.store.tempConfig(storage)
            self.__includeClass()
            self.__clearInputs()


    def __clearInputs(self):

        self.newIA_st2.save_button.setText("INCLUDE")
        self.editId = None
        self.__classTypes(self.newIA_st2.comboBox.currentText())
        self.newIA_st2.input_name.setText("")
        self.newIA_st2.comboBox.setCurrentIndex(0)



    def __includeClass(self):
        
        storage = self.store.tempConfig()

        rClass = QtWidgets.QWidget()
        self.classList = QtWidgets.QVBoxLayout(rClass)
        self.classList.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
        self.classList.setContentsMargins(3,9,3,9)
        self.classList.setSpacing(12)

        self.__clearLayout(self.classList)

        index = 0        
        for item in storage["CLASSES"]:

            qWidget = QtWidgets.QWidget()
            qWidget.setStyleSheet("background-color: rgb(68, 68, 68);border-radius:10px;")
            qLayout = QtWidgets.QVBoxLayout(qWidget)
            qLayout.setAlignment(QtCore.Qt.AlignmentFlag.AlignVCenter)
            qLayout.setContentsMargins(9,3,9,9)
            qLayout.setSpacing(0)


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

            qLayout.addWidget(qCname)
            qLayout.addWidget(qCtype)

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


            delButton = QtWidgets.QPushButton()
            delButton.setStyleSheet("background-color: #ff4b3e;border-radius:5px;")
            delButton.setMinimumHeight(20)
            delButton.setText("DELETE")
            delButton.clicked.connect(lambda state, x=item["ID"]: self.__removeClass(x))

            editButton = QtWidgets.QPushButton()
            editButton.setStyleSheet("background-color: #ffde23;border-radius:5px;")
            editButton.setText("EDIT")
            editButton.setMinimumHeight(20)
            editButton.clicked.connect(lambda state, x=item["ID"]: self.__editClass(x))

            sLayout.addWidget(delButton)
            sLayout.addWidget(editButton)

            qLayout.addWidget(sWidget)

            self.classList.addWidget(qWidget)
            index+=1

        self.newIA_st2.scrollArea.setWidget(rClass)

    def __removeClass(self, id):

        if self.editId == id:
            self.__clearInputs()
        
        storage = self.store.tempConfig()

        index = self.__searchClassID(id)
        storage["CLASSES"].pop(index)

        self.store.tempConfig(storage)

        self.__includeClass()

    def __editClass(self, id):

        self.newIA_st2.save_button.setText("UPDATE")
        item = self.__searchClass(id)
        self.newIA_st2.input_name.setText(item["C_NAME"])
        self.newIA_st2.comboBox.setCurrentText(item["TYPE"])
        
        self.__classTypes(item["TYPE"], item["ARGS"])

        self.editId = id


    def __searchClass(self, id):

        storage = self.store.tempConfig()
        for index in range(0,len(storage["CLASSES"])):

            item = storage["CLASSES"][index]

            if item["ID"] == id:
                return item
            
    def __searchClassID(self, id):

        storage = self.store.tempConfig()
        for index in range(0,len(storage["CLASSES"])):

            item = storage["CLASSES"][index]

            if item["ID"] == id:
                return index


    def __loadScrollArea(self):
        
        self.wLayout  = QtWidgets.QHBoxLayout(self.newIA_st2.widget_8)
        self.wLayout.setSpacing(0)
        self.scrollArea = QtWidgets.QScrollArea()
        self.wLayout.addWidget(self.scrollArea)
        self.scrollArea.setWidgetResizable(True)
        

        self.__classTypes(None)


    def __classTypes(self, target=None, data=None):


        self.cTypes ={

            "WEB IMAGES" :{
                "PARAMS" : {
                    0:{
                        "URL_INPUT_LABEL" : {"TEXT": "TERMS OR URL", "TYPE": "LABEL", "FX": None},
                        "WEB_INPUT" : {"TEXT": "Url", "TYPE": "LINE EDIT", "FX": None},
                    },

                    1: {
                        "URL_MAXD_LABEL" : {"TEXT": "MAX DOWNLOAD", "TYPE": "LABEL", "FX": None},
                        "WEB_MAXD" : {"TEXT": "Max download", "TYPE": "LINE EDIT", "FX": None},
                    },

                    2:{
                        "URL_FOLDER_OUTPUT_LABEL" : {"TEXT": "FOLDER", "TYPE": "LABEL", "FX": None},
                        "FOLDER_INPUT" : {"TEXT": "Output Directory", "TYPE": "LINE EDIT", "FX": "SET FOLDER"},
                    }
                }
                  
            },

            "DIRECTORY" :{

                "PARAMS" : {
                    0:{
                        "FOLDER_INPUT_LABEL" : {"TEXT": "FOLDER", "TYPE": "LABEL", "FX": None},
                        "FOLDER_INPUT" : {"TEXT": "Source directory", "TYPE": "LINE EDIT", "FX": "SET FOLDER"},
                    }
                }
            },
        }

        qWidget = False

        for key in self.cTypes:

            if key == target:
                
                self.inputList = []
                qWidget = QtWidgets.QWidget()
                self.qLayout = QtWidgets.QVBoxLayout(qWidget)
                self.qLayout.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                #self.qLayout.setContentsMargins(0,0,0,0)

                for param in self.cTypes[key]["PARAMS"]:

                    for element in self.cTypes[key]["PARAMS"][param]:
                        
                        eType = self.cTypes[key]["PARAMS"][param][element]["TYPE"]

                        if eType == "LABEL":

                            eItem = QtWidgets.QLabel()
                            rtext = '<html><head/><body><p><span style=" font-size:12pt; color:#ffffff;">'+str(self.cTypes[key]["PARAMS"][param][element]["TEXT"])+'</span></p></body></html>'
                            eItem.setText(rtext)
                            eItem.setObjectName(element)

                        if eType == "LINE EDIT":

                            eItem = QtWidgets.QLineEdit()
                            eItem.setStyleSheet('''QLineEdit {
                                background-color: #333;
                                color: #fff;
                                border: 2px solid #555;
                                border-radius: 5px;
                                padding: 5px;
                            }''')
                            eItem.setPlaceholderText(self.cTypes[key]["PARAMS"][param][element]["TEXT"])
                            eItem.setObjectName(element)

                            if data != None:
                                if element in data:
                                    eItem.setText(data[element])


                            self.inputList.append(eItem)
                            
                            if self.cTypes[key]["PARAMS"][param][element]["FX"] != None:
                                
                                if self.cTypes[key]["PARAMS"][param][element]["FX"] == "SET FOLDER":
                                    eItem.mousePressEvent = lambda event, el = eItem: self.__selectFolder(event, el)

                                if self.cTypes[key]["PARAMS"][param][element]["FX"] == "TEXT CHANGE":
                                    pass
                        
                        self.qLayout.addWidget(eItem)

        if qWidget != False:
            self.scrollArea.setWidget(qWidget)


    def __selectFolder(self, event, element):


        folder_path = QtWidgets.QFileDialog.getExistingDirectory(self.widget, "Select Folder")
        if folder_path:
            element.setText(folder_path)


    def __clearLayout(self, layoutElement):
       
         while layoutElement.count() > 0:
            item = layoutElement.takeAt(0)
            if item.widget():
                item.widget().deleteLater
                    

    def __nextpage(self):
    
        self.stackedWidget.setCurrentIndex(1)

    def __previusPage(self):

        self.stackedWidget.setCurrentIndex(0)
