# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'layout_main.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1141, 1034)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.gridLayoutWidget = QtWidgets.QWidget(self.splitter)
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.comboBox_Filter_Project = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox_Filter_Project.setObjectName("comboBox_Filter_Project")
        self.gridLayout_2.addWidget(self.comboBox_Filter_Project, 0, 3, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 0, 2, 1, 1)
        self.comboBox_Filter = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox_Filter.setObjectName("comboBox_Filter")
        self.gridLayout_2.addWidget(self.comboBox_Filter, 0, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 1, 2, 1, 1)
        self.comboBox_Search_Column = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox_Search_Column.setObjectName("comboBox_Search_Column")
        self.gridLayout_2.addWidget(self.comboBox_Search_Column, 1, 3, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 1, 0, 1, 1)
        self.lineEdit_Search = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_Search.setObjectName("lineEdit_Search")
        self.gridLayout_2.addWidget(self.lineEdit_Search, 1, 1, 1, 1)
        self.tableView_Docs = QtWidgets.QTableView(self.gridLayoutWidget)
        self.tableView_Docs.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.tableView_Docs.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableView_Docs.setObjectName("tableView_Docs")
        self.gridLayout_2.addWidget(self.tableView_Docs, 2, 0, 1, 4)
        self.tabSidePanel = QtWidgets.QTabWidget(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabSidePanel.sizePolicy().hasHeightForWidth())
        self.tabSidePanel.setSizePolicy(sizePolicy)
        self.tabSidePanel.setMinimumSize(QtCore.QSize(250, 0))
        self.tabSidePanel.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tabSidePanel.setObjectName("tabSidePanel")
        self.tabSidePanelPage1_2 = QtWidgets.QWidget()
        self.tabSidePanelPage1_2.setObjectName("tabSidePanelPage1_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tabSidePanelPage1_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.tabSidePanelPage1_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.comboBox_DocType = QtWidgets.QComboBox(self.tabSidePanelPage1_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_DocType.sizePolicy().hasHeightForWidth())
        self.comboBox_DocType.setSizePolicy(sizePolicy)
        self.comboBox_DocType.setObjectName("comboBox_DocType")
        self.comboBox_DocType.addItem("")
        self.comboBox_DocType.addItem("")
        self.comboBox_DocType.addItem("")
        self.comboBox_DocType.addItem("")
        self.comboBox_DocType.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox_DocType)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.textEdit_Title = QtWidgets.QTextEdit(self.tabSidePanelPage1_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.textEdit_Title.sizePolicy().hasHeightForWidth())
        self.textEdit_Title.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.textEdit_Title.setFont(font)
        self.textEdit_Title.setAcceptDrops(False)
        self.textEdit_Title.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.textEdit_Title.setLineWidth(0)
        self.textEdit_Title.setObjectName("textEdit_Title")
        self.verticalLayout_2.addWidget(self.textEdit_Title)
        self.scrollArea = QtWidgets.QScrollArea(self.tabSidePanelPage1_2)
        self.scrollArea.setAutoFillBackground(False)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setFrameShadow(QtWidgets.QFrame.Plain)
        self.scrollArea.setLineWidth(0)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 451, 600))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents_2.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents_2.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout.setVerticalSpacing(8)
        self.formLayout.setObjectName("formLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.formLayout.setLayout(1, QtWidgets.QFormLayout.LabelRole, self.verticalLayout)
        self.textEdit_Authors = QtWidgets.QTextEdit(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.textEdit_Authors.sizePolicy().hasHeightForWidth())
        self.textEdit_Authors.setSizePolicy(sizePolicy)
        self.textEdit_Authors.setAcceptDrops(False)
        self.textEdit_Authors.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.textEdit_Authors.setLineWidth(0)
        self.textEdit_Authors.setObjectName("textEdit_Authors")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.textEdit_Authors)
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lineEdit_Journal = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_Journal.setAcceptDrops(False)
        self.lineEdit_Journal.setFrame(False)
        self.lineEdit_Journal.setObjectName("lineEdit_Journal")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_Journal)
        self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.lineEdit_Year = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_Year.setAcceptDrops(False)
        self.lineEdit_Year.setFrame(False)
        self.lineEdit_Year.setObjectName("lineEdit_Year")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_Year)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_10 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_3.addWidget(self.label_10)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.formLayout.setLayout(5, QtWidgets.QFormLayout.LabelRole, self.verticalLayout_3)
        self.verticalLayout_MetaFiles = QtWidgets.QVBoxLayout()
        self.verticalLayout_MetaFiles.setSpacing(4)
        self.verticalLayout_MetaFiles.setObjectName("verticalLayout_MetaFiles")
        self.label_meta_path_1 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_meta_path_1.setObjectName("label_meta_path_1")
        self.verticalLayout_MetaFiles.addWidget(self.label_meta_path_1)
        self.label_meta_path_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_meta_path_2.setObjectName("label_meta_path_2")
        self.verticalLayout_MetaFiles.addWidget(self.label_meta_path_2)
        self.label_meta_path_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_meta_path_3.setObjectName("label_meta_path_3")
        self.verticalLayout_MetaFiles.addWidget(self.label_meta_path_3)
        self.label_meta_path_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_meta_path_4.setObjectName("label_meta_path_4")
        self.verticalLayout_MetaFiles.addWidget(self.label_meta_path_4)
        self.label_meta_path_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_meta_path_5.setObjectName("label_meta_path_5")
        self.verticalLayout_MetaFiles.addWidget(self.label_meta_path_5)
        self.pushButton_AddFile = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton_AddFile.setMaximumSize(QtCore.QSize(16777215, 30))
        self.pushButton_AddFile.setFlat(False)
        self.pushButton_AddFile.setObjectName("pushButton_AddFile")
        self.verticalLayout_MetaFiles.addWidget(self.pushButton_AddFile)
        spacerItem2 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_MetaFiles.addItem(spacerItem2)
        self.formLayout.setLayout(5, QtWidgets.QFormLayout.FieldRole, self.verticalLayout_MetaFiles)
        self.label_11 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_11.setObjectName("label_11")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.label_12 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_12.setObjectName("label_12")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.label_12)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(11, QtWidgets.QFormLayout.LabelRole, spacerItem3)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(11, QtWidgets.QFormLayout.FieldRole, spacerItem4)
        self.lineEdit_Pages = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_Pages.sizePolicy().hasHeightForWidth())
        self.lineEdit_Pages.setSizePolicy(sizePolicy)
        self.lineEdit_Pages.setAcceptDrops(False)
        self.lineEdit_Pages.setFrame(False)
        self.lineEdit_Pages.setObjectName("lineEdit_Pages")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.lineEdit_Pages)
        self.lineEdit_Editors = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_Editors.setAcceptDrops(False)
        self.lineEdit_Editors.setFrame(False)
        self.lineEdit_Editors.setObjectName("lineEdit_Editors")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.lineEdit_Editors)
        self.lineEdit_URL = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_URL.setAcceptDrops(False)
        self.lineEdit_URL.setFrame(False)
        self.lineEdit_URL.setObjectName("lineEdit_URL")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.lineEdit_URL)
        self.label_13 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_13.setObjectName("label_13")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.label_14 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_14.setObjectName("label_14")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.label_14)
        self.lineEdit_Volume = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_Volume.setAcceptDrops(False)
        self.lineEdit_Volume.setFrame(False)
        self.lineEdit_Volume.setObjectName("lineEdit_Volume")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.lineEdit_Volume)
        self.label_9 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.lineEdit_Issue = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_Issue.setAcceptDrops(False)
        self.lineEdit_Issue.setFrame(False)
        self.lineEdit_Issue.setObjectName("lineEdit_Issue")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.lineEdit_Issue)
        self.verticalLayout_5.addLayout(self.formLayout)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_2.addWidget(self.scrollArea)
        self.tabSidePanel.addTab(self.tabSidePanelPage1_2, "")
        self.tabSidePanelPage2_2 = QtWidgets.QWidget()
        self.tabSidePanelPage2_2.setObjectName("tabSidePanelPage2_2")
        self.gridLayout = QtWidgets.QGridLayout(self.tabSidePanelPage2_2)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_NewProject = QtWidgets.QPushButton(self.tabSidePanelPage2_2)
        self.pushButton_NewProject.setObjectName("pushButton_NewProject")
        self.gridLayout.addWidget(self.pushButton_NewProject, 1, 0, 1, 1)
        self.treeView_Projects = QtWidgets.QTreeView(self.tabSidePanelPage2_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.treeView_Projects.sizePolicy().hasHeightForWidth())
        self.treeView_Projects.setSizePolicy(sizePolicy)
        self.treeView_Projects.setObjectName("treeView_Projects")
        self.gridLayout.addWidget(self.treeView_Projects, 0, 0, 1, 2)
        self.pushButton_OpenProjectFolder = QtWidgets.QPushButton(self.tabSidePanelPage2_2)
        self.pushButton_OpenProjectFolder.setObjectName("pushButton_OpenProjectFolder")
        self.gridLayout.addWidget(self.pushButton_OpenProjectFolder, 1, 1, 1, 1)
        self.pushButton_EditProject = QtWidgets.QPushButton(self.tabSidePanelPage2_2)
        self.pushButton_EditProject.setObjectName("pushButton_EditProject")
        self.gridLayout.addWidget(self.pushButton_EditProject, 2, 0, 1, 1)
        self.tabSidePanel.addTab(self.tabSidePanelPage2_2, "")
        self.tabSidePanelPage3_2 = QtWidgets.QWidget()
        self.tabSidePanelPage3_2.setObjectName("tabSidePanelPage3_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tabSidePanelPage3_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.checkBox_Col_1 = QtWidgets.QCheckBox(self.tabSidePanelPage3_2)
        self.checkBox_Col_1.setObjectName("checkBox_Col_1")
        self.verticalLayout_4.addWidget(self.checkBox_Col_1)
        self.checkBox_2 = QtWidgets.QCheckBox(self.tabSidePanelPage3_2)
        self.checkBox_2.setObjectName("checkBox_2")
        self.verticalLayout_4.addWidget(self.checkBox_2)
        self.checkBox_3 = QtWidgets.QCheckBox(self.tabSidePanelPage3_2)
        self.checkBox_3.setObjectName("checkBox_3")
        self.verticalLayout_4.addWidget(self.checkBox_3)
        self.checkBox_4 = QtWidgets.QCheckBox(self.tabSidePanelPage3_2)
        self.checkBox_4.setObjectName("checkBox_4")
        self.verticalLayout_4.addWidget(self.checkBox_4)
        self.checkBox_5 = QtWidgets.QCheckBox(self.tabSidePanelPage3_2)
        self.checkBox_5.setObjectName("checkBox_5")
        self.verticalLayout_4.addWidget(self.checkBox_5)
        self.checkBox_6 = QtWidgets.QCheckBox(self.tabSidePanelPage3_2)
        self.checkBox_6.setObjectName("checkBox_6")
        self.verticalLayout_4.addWidget(self.checkBox_6)
        self.checkBox_7 = QtWidgets.QCheckBox(self.tabSidePanelPage3_2)
        self.checkBox_7.setObjectName("checkBox_7")
        self.verticalLayout_4.addWidget(self.checkBox_7)
        self.checkBox_8 = QtWidgets.QCheckBox(self.tabSidePanelPage3_2)
        self.checkBox_8.setIconSize(QtCore.QSize(20, 20))
        self.checkBox_8.setObjectName("checkBox_8")
        self.verticalLayout_4.addWidget(self.checkBox_8)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem5)
        self.tabSidePanel.addTab(self.tabSidePanelPage3_2, "")
        self.horizontalLayout.addWidget(self.splitter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1141, 38))
        self.menubar.setObjectName("menubar")
        self.menu_File = QtWidgets.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")
        self.menuImport = QtWidgets.QMenu(self.menu_File)
        self.menuImport.setObjectName("menuImport")
        self.menuTools = QtWidgets.QMenu(self.menubar)
        self.menuTools.setObjectName("menuTools")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionProperties = QtWidgets.QAction(MainWindow)
        self.actionProperties.setObjectName("actionProperties")
        self.action_Exit = QtWidgets.QAction(MainWindow)
        self.action_Exit.setObjectName("action_Exit")
        self.actionCheck_for_Duplicates = QtWidgets.QAction(MainWindow)
        self.actionCheck_for_Duplicates.setObjectName("actionCheck_for_Duplicates")
        self.actionCheck_for_New_Docs = QtWidgets.QAction(MainWindow)
        self.actionCheck_for_New_Docs.setObjectName("actionCheck_for_New_Docs")
        self.actionOpen_Selected_in_Acrobat = QtWidgets.QAction(MainWindow)
        self.actionOpen_Selected_in_Acrobat.setObjectName("actionOpen_Selected_in_Acrobat")
        self.actionPDF_File = QtWidgets.QAction(MainWindow)
        self.actionPDF_File.setShortcut("")
        self.actionPDF_File.setObjectName("actionPDF_File")
        self.actionBib_File = QtWidgets.QAction(MainWindow)
        self.actionBib_File.setObjectName("actionBib_File")
        self.actionNew_Bib_DB = QtWidgets.QAction(MainWindow)
        self.actionNew_Bib_DB.setObjectName("actionNew_Bib_DB")
        self.actionOpen_Bib_DB = QtWidgets.QAction(MainWindow)
        self.actionOpen_Bib_DB.setObjectName("actionOpen_Bib_DB")
        self.action_New_Blank_Entry = QtWidgets.QAction(MainWindow)
        self.action_New_Blank_Entry.setObjectName("action_New_Blank_Entry")
        self.menuImport.addAction(self.actionPDF_File)
        self.menuImport.addAction(self.actionBib_File)
        self.menuImport.addAction(self.action_New_Blank_Entry)
        self.menu_File.addAction(self.actionNew_Bib_DB)
        self.menu_File.addAction(self.actionOpen_Bib_DB)
        self.menu_File.addAction(self.menuImport.menuAction())
        self.menu_File.addAction(self.actionProperties)
        self.menu_File.addAction(self.action_Exit)
        self.menuTools.addAction(self.actionCheck_for_New_Docs)
        self.menuTools.addAction(self.actionCheck_for_Duplicates)
        self.menuTools.addAction(self.actionOpen_Selected_in_Acrobat)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())

        self.retranslateUi(MainWindow)
        self.tabSidePanel.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ArDa"))
        self.label_6.setText(_translate("MainWindow", "from"))
        self.label_5.setText(_translate("MainWindow", "Showing"))
        self.label_8.setText(_translate("MainWindow", "in"))
        self.label_7.setText(_translate("MainWindow", "Search"))
        self.label.setText(_translate("MainWindow", "Doc Type:"))
        self.comboBox_DocType.setItemText(0, _translate("MainWindow", "Article"))
        self.comboBox_DocType.setItemText(1, _translate("MainWindow", "Book"))
        self.comboBox_DocType.setItemText(2, _translate("MainWindow", "Book Section"))
        self.comboBox_DocType.setItemText(3, _translate("MainWindow", "Working Paper"))
        self.comboBox_DocType.setItemText(4, _translate("MainWindow", "Report"))
        self.textEdit_Title.setPlaceholderText(_translate("MainWindow", "Title"))
        self.label_2.setText(_translate("MainWindow", "Authors:"))
        self.label_3.setText(_translate("MainWindow", "Journal:"))
        self.label_4.setText(_translate("MainWindow", "Year:"))
        self.label_10.setText(_translate("MainWindow", "Files:"))
        self.label_meta_path_1.setText(_translate("MainWindow", "TextLabel"))
        self.label_meta_path_2.setText(_translate("MainWindow", "TextLabel"))
        self.label_meta_path_3.setText(_translate("MainWindow", "TextLabel"))
        self.label_meta_path_4.setText(_translate("MainWindow", "TextLabel"))
        self.label_meta_path_5.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton_AddFile.setText(_translate("MainWindow", "Add File"))
        self.label_11.setText(_translate("MainWindow", "Editors:"))
        self.label_12.setText(_translate("MainWindow", "URL:"))
        self.label_13.setText(_translate("MainWindow", "Pages:"))
        self.label_14.setText(_translate("MainWindow", "Volume:"))
        self.label_9.setText(_translate("MainWindow", "Issue:"))
        self.tabSidePanel.setTabText(self.tabSidePanel.indexOf(self.tabSidePanelPage1_2), _translate("MainWindow", "Meta"))
        self.pushButton_NewProject.setText(_translate("MainWindow", "New Project"))
        self.pushButton_OpenProjectFolder.setText(_translate("MainWindow", "Open Project Folder"))
        self.pushButton_EditProject.setText(_translate("MainWindow", "Edit Project"))
        self.tabSidePanel.setTabText(self.tabSidePanel.indexOf(self.tabSidePanelPage2_2), _translate("MainWindow", "Projects"))
        self.checkBox_Col_1.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_2.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_3.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_4.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_5.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_6.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_7.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_8.setText(_translate("MainWindow", "CheckBox"))
        self.tabSidePanel.setTabText(self.tabSidePanel.indexOf(self.tabSidePanelPage3_2), _translate("MainWindow", "Columns"))
        self.menu_File.setTitle(_translate("MainWindow", "&File"))
        self.menuImport.setTitle(_translate("MainWindow", "&Import/Add"))
        self.menuTools.setTitle(_translate("MainWindow", "&Tools"))
        self.actionProperties.setText(_translate("MainWindow", "DB &Properties"))
        self.action_Exit.setText(_translate("MainWindow", "&Exit"))
        self.action_Exit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionCheck_for_Duplicates.setText(_translate("MainWindow", "Check for &Duplicates"))
        self.actionCheck_for_New_Docs.setText(_translate("MainWindow", "Check for &New Docs"))
        self.actionOpen_Selected_in_Acrobat.setText(_translate("MainWindow", "&Open in Acrobat"))
        self.actionOpen_Selected_in_Acrobat.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionPDF_File.setText(_translate("MainWindow", "&PDF File"))
        self.actionBib_File.setText(_translate("MainWindow", "&Bib File"))
        self.actionNew_Bib_DB.setText(_translate("MainWindow", "&New Bib DB"))
        self.actionOpen_Bib_DB.setText(_translate("MainWindow", "&Open Bib DB"))
        self.action_New_Blank_Entry.setText(_translate("MainWindow", "&New Blank Entry"))
        self.action_New_Blank_Entry.setShortcut(_translate("MainWindow", "+"))

