# Form implementation generated from reading ui file './ui/new_page1.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1059, 533)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(parent=Form)
        self.widget.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_2 = QtWidgets.QWidget(parent=self.widget)
        self.widget_2.setMinimumSize(QtCore.QSize(600, 0))
        self.widget_2.setStyleSheet("background-color: rgb(68, 68, 68);\n"
"border-radius:20px;")
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setContentsMargins(-1, 30, -1, 30)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_2 = QtWidgets.QFrame(parent=self.widget_2)
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
        self.verticalLayout_2.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(parent=self.widget_2)
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_3 = QtWidgets.QLabel(parent=self.frame_3)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3)
        self.input_description = QtWidgets.QTextEdit(parent=self.frame_3)
        self.input_description.setMinimumSize(QtCore.QSize(0, 100))
        self.input_description.setStyleSheet("QTextEdit {\n"
"            background-color: #f0f0f0;\n"
"            border: 2px solid #ccc;\n"
"            border-radius: 5px;\n"
"            font-family: Arial, sans-serif;\n"
"            font-size: 14px;\n"
"            padding: 10px;\n"
"        }\n"
"        \n"
"        QTextEdit::hover {\n"
"            background-color: #e0e0e0;\n"
"        }\n"
"        \n"
"        QTextEdit::focus {\n"
"            border-color: #4CAF50;\n"
"        }")
        self.input_description.setObjectName("input_description")
        self.verticalLayout_4.addWidget(self.input_description)
        self.verticalLayout_2.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(parent=self.widget_2)
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_5.setContentsMargins(-1, 20, -1, -1)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_4 = QtWidgets.QLabel(parent=self.frame_4)
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 80))
        self.label_4.setObjectName("label_4")
        self.verticalLayout_5.addWidget(self.label_4)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.textClassification = QtWidgets.QPushButton(parent=self.frame_4)
        self.textClassification.setMinimumSize(QtCore.QSize(0, 60))
        self.textClassification.setStyleSheet("QPushButton {\n"
"                background-color: #dc3545; /* Red color */\n"
"                color: #fff;\n"
"                border: 2px solid #dc3545; /* Matching border color */\n"
"                border-radius: 5px;\n"
"                padding: 7px 10px;\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #c82333; /* Darker shade of red on hover */\n"
"                border: 2px solid #c82333;\n"
"            }\n"
"QPushButton:checked  {\n"
"                background-color: #c82333; /* Darker shade of red on hover */\n"
"                border: 2px solid rgb(255, 255, 255);\n"
"            }")
        self.textClassification.setCheckable(True)
        self.textClassification.setObjectName("textClassification")
        self.gridLayout.addWidget(self.textClassification, 0, 0, 1, 1)
        self.voiceClassification = QtWidgets.QPushButton(parent=self.frame_4)
        self.voiceClassification.setMinimumSize(QtCore.QSize(0, 60))
        self.voiceClassification.setStyleSheet("QPushButton {\n"
"                background-color: #dc3545; /* Red color */\n"
"                color: #fff;\n"
"                border: 2px solid #dc3545; /* Matching border color */\n"
"                border-radius: 5px;\n"
"                padding: 7px 10px;\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #c82333; /* Darker shade of red on hover */\n"
"                border: 2px solid #c82333;\n"
"            }\n"
"QPushButton:checked  {\n"
"                background-color: #c82333; /* Darker shade of red on hover */\n"
"                border: 2px solid rgb(255, 255, 255);\n"
"            }")
        self.voiceClassification.setCheckable(True)
        self.voiceClassification.setObjectName("voiceClassification")
        self.gridLayout.addWidget(self.voiceClassification, 1, 0, 1, 1)
        self.imageClassification = QtWidgets.QPushButton(parent=self.frame_4)
        self.imageClassification.setMinimumSize(QtCore.QSize(0, 60))
        self.imageClassification.setStyleSheet("QPushButton {\n"
"                background-color: #dc3545; /* Red color */\n"
"                color: #fff;\n"
"                border: 2px solid #dc3545; /* Matching border color */\n"
"                border-radius: 5px;\n"
"                padding: 7px 10px;\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #c82333; /* Darker shade of red on hover */\n"
"                border: 2px solid #c82333;\n"
"            }\n"
"QPushButton:checked  {\n"
"                background-color: #c82333; /* Darker shade of red on hover */\n"
"                border: 2px solid rgb(255, 255, 255);\n"
"            }")
        self.imageClassification.setCheckable(True)
        self.imageClassification.setObjectName("imageClassification")
        self.gridLayout.addWidget(self.imageClassification, 0, 1, 1, 1)
        self.faceClassification = QtWidgets.QPushButton(parent=self.frame_4)
        self.faceClassification.setMinimumSize(QtCore.QSize(0, 60))
        self.faceClassification.setStyleSheet("QPushButton {\n"
"                background-color: #dc3545; /* Red color */\n"
"                color: #fff;\n"
"                border: 2px solid #dc3545; /* Matching border color */\n"
"                border-radius: 5px;\n"
"                padding: 7px 10px;\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #c82333; /* Darker shade of red on hover */\n"
"                border: 2px solid #c82333;\n"
"            }\n"
"QPushButton:checked  {\n"
"                background-color: #c82333; /* Darker shade of red on hover */\n"
"                border: 2px solid rgb(255, 255, 255);\n"
"            }")
        self.faceClassification.setCheckable(True)
        self.faceClassification.setObjectName("faceClassification")
        self.gridLayout.addWidget(self.faceClassification, 1, 1, 1, 1)
        self.verticalLayout_5.addLayout(self.gridLayout)
        self.widget_3 = QtWidgets.QWidget(parent=self.frame_4)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.next_button = QtWidgets.QPushButton(parent=self.widget_3)
        self.next_button.setMinimumSize(QtCore.QSize(150, 30))
        self.next_button.setMaximumSize(QtCore.QSize(150, 16777215))
        self.next_button.setStyleSheet("QPushButton {\n"
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
        self.next_button.setObjectName("next_button")
        self.horizontalLayout_2.addWidget(self.next_button)
        self.delete_button = QtWidgets.QPushButton(parent=self.widget_3)
        self.delete_button.setMinimumSize(QtCore.QSize(150, 30))
        self.delete_button.setMaximumSize(QtCore.QSize(150, 16777215))
        self.delete_button.setStyleSheet("QPushButton {\n"
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
        self.delete_button.setObjectName("delete_button")
        self.horizontalLayout_2.addWidget(self.delete_button)
        self.verticalLayout_5.addWidget(self.widget_3, 0, QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.verticalLayout_2.addWidget(self.frame_4)
        self.verticalLayout.addWidget(self.widget_2, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.horizontalLayout.addWidget(self.widget)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p><span style=\" color:#ffffff;\">MODEL NAME</span></p></body></html>"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p><span style=\" color:#ffffff;\">DESCRIPTION</span></p></body></html>"))
        self.label_4.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#ffffff;\">MODEL TYPE</span></p></body></html>"))
        self.textClassification.setText(_translate("Form", "TEXT CLASSIFICATION"))
        self.voiceClassification.setText(_translate("Form", "TEXT EXTRACTOR"))
        self.imageClassification.setText(_translate("Form", "IMAGE CLASSIFICATION"))
        self.faceClassification.setText(_translate("Form", "FACE CLASSIFICATION"))
        self.next_button.setText(_translate("Form", "NEXT"))
        self.delete_button.setText(_translate("Form", "DELETE"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
