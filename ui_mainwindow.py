# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QGridLayout,
    QGroupBox, QHBoxLayout, QHeaderView, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QStatusBar, QTabWidget, QTableView,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1026, 682)
        MainWindow.setStyleSheet(u"/* Setting a style */\n"
"QWidget {\n"
"        background-color: \"powderblue\";\n"
"}\n"
"/* --------------------------------------- expand pane in qtabwidget --------------------------------------- */\n"
"QTabWidget::pane {\n"
"    border: 0 solid black;\n"
"    margin: -9px -8px -8px -9px;\n"
"}\n"
"QTabBar::tab {\n"
"    background: \"peachpuff\"; \n"
"    border: 2px solid lightgray; \n"
"    padding: 10px 20px 10px 20px;\n"
"}\n"
" QTabBar::tab:selected {\n"
"    background: \"lightgreen\";\n"
"    border: 2px solid gray;\n"
"    padding: 10px 20px 10px 20px;\n"
"    margin-bottom: -2px; \n"
" }\n"
"/* --------------------------------------- Style the BUTTONS --------------------------------------- */\n"
"QPushButton {\n"
"    color: \"black\"; /* Button Text */\n"
"    padding: 10px;\n"
"    border-radius: 5px;\n"
"    border-width: 1px;\n"
"    border-color: \"lightslategrey\";\n"
"    border-style: solid;\n"
"}\n"
"QPushButton#btn_scrape {\n"
"    background-color: \"lightgreen\";\n"
"    padding: 10"
                        "px 30px 10px 30px;\n"
"    border-color: \"olivedrap\";\n"
"}\n"
"QPushButton::hover#btn_scrape {\n"
"    color: \"white\"; /* Button Text */\n"
"    background-color: \"forestgreen\";\n"
"    font-weight:bold;\n"
"}\n"
"QPushButton#btn_delete {\n"
"    background-color: \"khaki\";\n"
"    padding: 10px 20px 10px 20px;\n"
"    border-color: \"darkgoldenrod\";\n"
"}\n"
"QPushButton::hover#btn_delete {\n"
"    color: \"white\"; /* Button Text */\n"
"    background-color: \"darkgoldenrod\";\n"
"    font-weight:bold;\n"
"}\n"
"QPushButton#btn_exit {\n"
"    color: \"black\"; /* Button Text */\n"
"    background-color: \"orange\";\n"
"    padding: 8px;\n"
"    border-radius: 5px;\n"
"    border-width: 1px;\n"
"    border-color: \"red\";\n"
"    border-style: solid;\n"
"    width:100px;\n"
"    height:10px;\n"
"}\n"
"QPushButton::hover#btn_exit {\n"
"    color: \"white\"; /* Button Text */\n"
"    background-color: \"red\";\n"
"    border-color: \"orange\";\n"
"    border-width: 0px;\n"
"    font-weight:bold;\n"
"}\n"
""
                        "/* --------------------------------------- Style the QGroupbox --------------------------------------- */\n"
"QGroupBox {\n"
"    font: bold;\n"
"    border: 1px solid silver;\n"
"    border-radius: 4px;\n"
"    margin-top: 8px;\n"
"background-color: \"lightgreen\";\n"
"}\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 7px;\n"
"    padding: 0px 5px 0px 5px;\n"
"}\n"
"/*  ---------------------------------------  Setting a style for QTableView  ---------------------------------------  */\n"
"\n"
"QTableView { gridline-color: \"orange\";\n"
"        background-color: \"khaki\";\n"
"        border-color: rgb(242, 128, 133);\n"
"        padding: 1px;\n"
"        }\n"
"QHeaderView {\n"
"    background-color: \"yellow\";\n"
"    }\n"
"QHeaderView::section {\n"
"    padding-bottom: 5px;\n"
"    padding-top: 5px;\n"
"    background-color: rgb(71, 153, 176);\n"
"    color: white;\n"
"    height: 25px;\n"
"    /* width: 150px; */\n"
"    font: 14px;\n"
"}\n"
"QTableView::item:selected {\n"
"    /*"
                        " row selected */\n"
"    background-color: \"gold\";\n"
"    color: \"black\"; \n"
"}\n"
"QTableView::item {\n"
"    /* row selected */\n"
"    padding: 5px;\n"
"}\n"
"QTableView::item:selected {\n"
"    background-color: rgb(242, 128, 133);\n"
"}\n"
"\n"
"/*  ---------------------------------------  Setting a style for QCombobox  ---------------------------------------  #aaff7f */\n"
"QComboBox { \n"
"subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    selection-background-color: #111;\n"
"    selection-color: yellow;\n"
"    color: \"black\";\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #aaff7f, stop: 0.5 #aaff7f, stop: 0.9 #aaff7f, stop: 1 #aaff7f);\n"
"    border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius: 2;\n"
"    padding: 1px 0px 1px 20px;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    border: 2px solid darkgray;\n"
"selection-background-color: lightgray;\n"
"}\n"
"QListView {\n"
"    background-co"
                        "lor: \"lightgreen\";\n"
"}\n"
"QSpinBox {\n"
"    color: white;\n"
"    selection-background-color: \"lightgreen\";\n"
"    background: #aaff7f;\n"
"    border: 1px solid \"olivedrap\";\n"
"    border-radius: 2px;\n"
"padding: 1px 10px 1px 10px;\n"
"color: \"black\";\n"
"selection-background-color: \"lightgreen\";\n"
"selection-color: \"black\";\n"
"font: bold;\n"
"}\n"
"QStatusBar {\n"
"    background: \"skyblue\";\n"
"    border-top: 2px solid \"gray\";\n"
"}\n"
"/* --------------------------------------- Status Bar  -----------------------------------*/\n"
"QSizeGrip {\n"
"    image: url(icon/size_grip.svg);\n"
"    width: 20px;\n"
"    height: 20px;\n"
"    background-color: \"skyblue\";\n"
"}\n"
"QStatusBar, QStatusBar QLabel {\n"
"        color: \"black\";\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.comboBox = QComboBox(self.groupBox)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_2.addWidget(self.comboBox)

        self.spinBox = QSpinBox(self.groupBox)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setMinimumSize(QSize(50, 30))
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(50)

        self.horizontalLayout_2.addWidget(self.spinBox)

        self.btn_scrape = QPushButton(self.groupBox)
        self.btn_scrape.setObjectName(u"btn_scrape")

        self.horizontalLayout_2.addWidget(self.btn_scrape)

        self.horizontalLayout_2.setStretch(0, 1)

        self.verticalLayout.addWidget(self.groupBox)

        self.tabs = QTabWidget(self.centralwidget)
        self.tabs.setObjectName(u"tabs")
        self.tabs.setStyleSheet(u"")
        self.tab_table = QWidget()
        self.tab_table.setObjectName(u"tab_table")
        self.gridLayout = QGridLayout(self.tab_table)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tableView = QTableView(self.tab_table)
        self.tableView.setObjectName(u"tableView")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(46)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableView.sizePolicy().hasHeightForWidth())
        self.tableView.setSizePolicy(sizePolicy)
        self.tableView.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)

        self.gridLayout.addWidget(self.tableView, 0, 0, 1, 1)

        self.tabs.addTab(self.tab_table, "")
        self.tab_output = QWidget()
        self.tab_output.setObjectName(u"tab_output")
        self.horizontalLayout_3 = QHBoxLayout(self.tab_output)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.textEdit = QTextEdit(self.tab_output)
        self.textEdit.setObjectName(u"textEdit")

        self.horizontalLayout_3.addWidget(self.textEdit)

        self.tabs.addTab(self.tab_output, "")

        self.verticalLayout.addWidget(self.tabs)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_delete = QPushButton(self.centralwidget)
        self.btn_delete.setObjectName(u"btn_delete")

        self.horizontalLayout.addWidget(self.btn_delete)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_exit = QPushButton(self.centralwidget)
        self.btn_exit.setObjectName(u"btn_exit")

        self.horizontalLayout.addWidget(self.btn_exit)


        self.verticalLayout.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1026, 18))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabs.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Scrapy Project", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Webpage selection", None))
        self.btn_scrape.setText(QCoreApplication.translate("MainWindow", u"Scrape", None))
        self.tabs.setTabText(self.tabs.indexOf(self.tab_table), QCoreApplication.translate("MainWindow", u"Table", None))
        self.tabs.setTabText(self.tabs.indexOf(self.tab_output), QCoreApplication.translate("MainWindow", u"Output", None))
        self.btn_delete.setText(QCoreApplication.translate("MainWindow", u"Delete Selected", None))
        self.btn_exit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
    # retranslateUi

