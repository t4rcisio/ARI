# Form implementation generated from reading ui file './ui/new_page2.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(904, 545)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(parent=Form)
        self.widget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget_2 = QtWidgets.QWidget(parent=self.widget)
        self.widget_2.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout.setContentsMargins(-1, -1, -1, 30)
        self.verticalLayout.setSpacing(11)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(parent=self.widget_2)
        self.label.setMaximumSize(QtCore.QSize(16777215, 40))
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.frame = QtWidgets.QFrame(parent=self.widget_2)
        self.frame.setMinimumSize(QtCore.QSize(800, 0))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.widget_5 = QtWidgets.QWidget(parent=self.frame)
        self.widget_5.setStyleSheet("background-color: rgb(68, 68, 68);\n"
"border-radius:20px;")
        self.widget_5.setObjectName("widget_5")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.widget_5)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.frame_2 = QtWidgets.QFrame(parent=self.widget_5)
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 80))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(parent=self.frame_2)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.input_name = QtWidgets.QLineEdit(parent=self.frame_2)
        self.input_name.setMinimumSize(QtCore.QSize(0, 30))
        self.input_name.setStyleSheet("QLineEdit {\n"
"                background-color: #333;\n"
"                color: #fff;\n"
"                border: 2px solid #555;\n"
"                border-radius: 5px;\n"
"                padding: 5px;\n"
"            }")
        self.input_name.setObjectName("input_name")
        self.verticalLayout_3.addWidget(self.input_name)
        self.verticalLayout_8.addWidget(self.frame_2)
        self.widget_3 = QtWidgets.QWidget(parent=self.widget_5)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_7 = QtWidgets.QLabel(parent=self.widget_3)
        self.label_7.setMaximumSize(QtCore.QSize(16777215, 40))
        self.label_7.setObjectName("label_7")
        self.verticalLayout_9.addWidget(self.label_7)
        self.frame_6 = QtWidgets.QFrame(parent=self.widget_3)
        self.frame_6.setMaximumSize(QtCore.QSize(16777215, 100))
        self.frame_6.setStyleSheet("border-radius:0px;")
        self.frame_6.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_6 = QtWidgets.QLabel(parent=self.frame_6)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_7.addWidget(self.label_6)
        self.comboBox = QtWidgets.QComboBox(parent=self.frame_6)
        self.comboBox.setMinimumSize(QtCore.QSize(0, 30))
        self.comboBox.setStyleSheet("QComboBox {\n"
"    background-color: #000;\n"
"    color: #fff;\n"
"    border: 2px solid #555;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    color: #fff;\n"
"    border-radius: 0px; /* Set border radius to 0px */\n"
"}\n"
"")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayout_7.addWidget(self.comboBox)
        self.verticalLayout_9.addWidget(self.frame_6)
        self.verticalLayout_8.addWidget(self.widget_3, 0, QtCore.Qt.AlignmentFlag.AlignTop)
        self.widget_8 = QtWidgets.QWidget(parent=self.widget_5)
        self.widget_8.setObjectName("widget_8")
        self.verticalLayout_8.addWidget(self.widget_8)
        self.widget_7 = QtWidgets.QWidget(parent=self.widget_5)
        self.widget_7.setObjectName("widget_7")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_7)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.save_button = QtWidgets.QPushButton(parent=self.widget_7)
        self.save_button.setMinimumSize(QtCore.QSize(0, 30))
        self.save_button.setStyleSheet("QPushButton {\n"
"                background-color: #007bff;\n"
"                color: #fff;\n"
"                border: 2px solid #007bff;\n"
"                border-radius: 5px;\n"
"                padding: 7px 10px;\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #0056b3;\n"
"                border: 2px solid #0056b3;\n"
"            }")
        self.save_button.setObjectName("save_button")
        self.horizontalLayout_5.addWidget(self.save_button)
        self.cancel_button = QtWidgets.QPushButton(parent=self.widget_7)
        self.cancel_button.setMinimumSize(QtCore.QSize(0, 30))
        self.cancel_button.setStyleSheet("QPushButton {\n"
"                background-color: #007bff;\n"
"                color: #fff;\n"
"                border: 2px solid #007bff;\n"
"                border-radius: 5px;\n"
"                padding: 7px 10px;\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #0056b3;\n"
"                border: 2px solid #0056b3;\n"
"            }")
        self.cancel_button.setObjectName("cancel_button")
        self.horizontalLayout_5.addWidget(self.cancel_button)
        self.verticalLayout_8.addWidget(self.widget_7, 0, QtCore.Qt.AlignmentFlag.AlignBottom)
        self.horizontalLayout_3.addWidget(self.widget_5)
        self.widget_4 = QtWidgets.QWidget(parent=self.frame)
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_4)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_8 = QtWidgets.QLabel(parent=self.widget_4)
        self.label_8.setMaximumSize(QtCore.QSize(16777215, 40))
        self.label_8.setObjectName("label_8")
        self.verticalLayout_2.addWidget(self.label_8)
        self.scrollArea = QtWidgets.QScrollArea(parent=self.widget_4)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 367, 329))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.scrollArea)
        self.horizontalLayout_3.addWidget(self.widget_4)
        self.verticalLayout.addWidget(self.frame, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.widget_6 = QtWidgets.QWidget(parent=self.widget_2)
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_6)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 20)
        self.horizontalLayout_4.setSpacing(9)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.back_button = QtWidgets.QPushButton(parent=self.widget_6)
        self.back_button.setMinimumSize(QtCore.QSize(150, 30))
        self.back_button.setMaximumSize(QtCore.QSize(150, 16777215))
        self.back_button.setStyleSheet("QPushButton {\n"
"                background-color: #007bff;\n"
"                color: #fff;\n"
"                border: 2px solid #007bff;\n"
"                border-radius: 5px;\n"
"                padding: 7px 10px;\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #0056b3;\n"
"                border: 2px solid #0056b3;\n"
"            }")
        self.back_button.setObjectName("back_button")
        self.horizontalLayout_4.addWidget(self.back_button)
        self.finish_button = QtWidgets.QPushButton(parent=self.widget_6)
        self.finish_button.setMinimumSize(QtCore.QSize(150, 30))
        self.finish_button.setMaximumSize(QtCore.QSize(150, 16777215))
        self.finish_button.setStyleSheet("QPushButton {\n"
"                background-color: #007bff;\n"
"                color: #fff;\n"
"                border: 2px solid #007bff;\n"
"                border-radius: 5px;\n"
"                padding: 7px 10px;\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #0056b3;\n"
"                border: 2px solid #0056b3;\n"
"            }")
        self.finish_button.setObjectName("finish_button")
        self.horizontalLayout_4.addWidget(self.finish_button)
        self.verticalLayout.addWidget(self.widget_6, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.horizontalLayout_2.addWidget(self.widget_2)
        self.horizontalLayout.addWidget(self.widget)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt;\"># MODEL CLASSES</span></p></body></html>"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p><span style=\" color:#ffffff;\">CLASS NAME</span></p></body></html>"))
        self.label_7.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt; color:#ffffff;\">SOURCE</span></p></body></html>"))
        self.label_6.setText(_translate("Form", "<html><head/><body><p><span style=\" color:#ffffff;\">SOURCE TYPE</span></p></body></html>"))
        self.comboBox.setItemText(0, _translate("Form", "SELECT"))
        self.comboBox.setItemText(1, _translate("Form", "DIRECTORY"))
        self.comboBox.setItemText(2, _translate("Form", "WEB IMAGES"))
        self.save_button.setText(_translate("Form", "INCLUDE"))
        self.cancel_button.setText(_translate("Form", "DISCARD"))
        self.label_8.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt; color:#ffffff;\">SOURCES</span></p></body></html>"))
        self.back_button.setText(_translate("Form", "BACK"))
        self.finish_button.setText(_translate("Form", "FINISH"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
