# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'layout_doc_search_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(839, 832)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.gridLayout_2.addWidget(self.comboBox, 0, 1, 1, 1)
        self.lineEdit_Search = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_Search.setObjectName("lineEdit_Search")
        self.gridLayout_2.addWidget(self.lineEdit_Search, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.pushButton_Search = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_Search.sizePolicy().hasHeightForWidth())
        self.pushButton_Search.setSizePolicy(sizePolicy)
        self.pushButton_Search.setObjectName("pushButton_Search")
        self.gridLayout_2.addWidget(self.pushButton_Search, 0, 2, 2, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.label_TotalResults = QtWidgets.QLabel(Dialog)
        self.label_TotalResults.setObjectName("label_TotalResults")
        self.verticalLayout.addWidget(self.label_TotalResults)
        self.label_ResultsShowing = QtWidgets.QLabel(Dialog)
        self.label_ResultsShowing.setObjectName("label_ResultsShowing")
        self.verticalLayout.addWidget(self.label_ResultsShowing)
        self.horizontalLayout_PageButtons = QtWidgets.QHBoxLayout()
        self.horizontalLayout_PageButtons.setObjectName("horizontalLayout_PageButtons")
        self.pushButton_PageBack = QtWidgets.QPushButton(Dialog)
        self.pushButton_PageBack.setEnabled(False)
        self.pushButton_PageBack.setObjectName("pushButton_PageBack")
        self.horizontalLayout_PageButtons.addWidget(self.pushButton_PageBack)
        self.pushButton_PageForward = QtWidgets.QPushButton(Dialog)
        self.pushButton_PageForward.setObjectName("pushButton_PageForward")
        self.horizontalLayout_PageButtons.addWidget(self.pushButton_PageForward)
        self.verticalLayout.addLayout(self.horizontalLayout_PageButtons)
        self.scrollArea = QtWidgets.QScrollArea(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 819, 642))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName("gridLayout")
        self.tableWidget_SearchResults = QtWidgets.QTableWidget(self.scrollAreaWidgetContents)
        self.tableWidget_SearchResults.setObjectName("tableWidget_SearchResults")
        self.tableWidget_SearchResults.setColumnCount(0)
        self.tableWidget_SearchResults.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget_SearchResults, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_Merge = QtWidgets.QPushButton(Dialog)
        self.pushButton_Merge.setObjectName("pushButton_Merge")
        self.horizontalLayout.addWidget(self.pushButton_Merge)
        self.pushButton_Compare = QtWidgets.QPushButton(Dialog)
        self.pushButton_Compare.setObjectName("pushButton_Compare")
        self.horizontalLayout.addWidget(self.pushButton_Compare)
        self.pushButton_Cancel = QtWidgets.QPushButton(Dialog)
        self.pushButton_Cancel.setObjectName("pushButton_Cancel")
        self.horizontalLayout.addWidget(self.pushButton_Cancel)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Crossref Query"))
        self.label.setText(_translate("Dialog", "Search Field:"))
        self.comboBox.setItemText(0, _translate("Dialog", "All fields"))
        self.label_2.setText(_translate("Dialog", "Search Value:"))
        self.pushButton_Search.setText(_translate("Dialog", "Search"))
        self.label_TotalResults.setText(_translate("Dialog", "TextLabel"))
        self.label_ResultsShowing.setText(_translate("Dialog", "TextLabel"))
        self.pushButton_PageBack.setText(_translate("Dialog", "<- Page Backward"))
        self.pushButton_PageForward.setText(_translate("Dialog", "Page Forward ->"))
        self.pushButton_Merge.setText(_translate("Dialog", "Overwrite Existing"))
        self.pushButton_Compare.setText(_translate("Dialog", "Compare and Merge"))
        self.pushButton_Cancel.setText(_translate("Dialog", "Cancel"))
