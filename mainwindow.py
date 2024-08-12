import sys
from PySide6.QtCore import QProcess, Signal, Slot, QDir
from PySide6.QtWidgets import QApplication, QMainWindow, QHeaderView, QAbstractItemView
from PySide6.QtSql import QSqlTableModel
from sqlConnection import Data
from ui_mainwindow import Ui_MainWindow

#     pyside6-uic mainwindow.ui -o ui_mainwindow.py

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # A list of selected row ID's from the tableview -> used for delete function
        self.idlist = []

        self.process = QProcess(self)
        self.process.readyReadStandardOutput.connect(self.handle_stdout)
        self.process.readyReadStandardError.connect(self.handle_stderr)
        self.process.finished.connect(self.process_finished)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn_exit.clicked.connect(self.close)
        self.ui.btn_scrape.clicked.connect(self.start_scrapy)
        self.ui.btn_delete.clicked.connect(self.delete_btn)

        self.conn = Data()
        # self.conn.mySignal.connect(self.update_messages)
        self.call_table()

        self.ui.comboBox.currentTextChanged.connect(self.on_combobox_changed)
        self.ui.comboBox.addItem("https://books.toscrape.com/catalogue/category/books/travel_2/")
        self.ui.comboBox.addItem("https://books.toscrape.com/catalogue/category/books/mystery_3/")
        self.ui.comboBox.addItem("https://books.toscrape.com/catalogue/category/books/historical-fiction_4/")
        self.ui.comboBox.addItem("https://books.toscrape.com/catalogue/category/books/sequential-art_5/")
        self.ui.comboBox.addItem("https://books.toscrape.com/catalogue/category/books/classics_6/")
        self.ui.comboBox.addItem("https://books.toscrape.com/catalogue/category/books/philosophy_7/")
        self.ui.comboBox.addItem("https://books.toscrape.com/catalogue/category/books/romance_8/")
        self.ui.comboBox.addItem("https://books.toscrape.com/catalogue/category/books/womens-fiction_9/")
        self.ui.comboBox.addItem("https://books.toscrape.com/catalogue/category/books/fiction_10/")
        self.ui.comboBox.addItem("https://books.toscrape.com/catalogue/category/books/childrens_11/")
        self.ui.comboBox.addItem("https://books.toscrape.com/catalogue/category/books/religion_12/")
        self.ui.comboBox.addItem("https://books.toscrape.com/catalogue/category/books/classics_6/")
        self.ui.comboBox.addItem("https://books.toscrape.com/catalogue/category/books/nonfiction_13/")

    def call_table(self):
        self.model = QSqlTableModel(self)
        self.model.setTable('booksdb')
        self.model.select()
        self.ui.tableView.setModel(self.model)
        # Auto stretch columns
        self.ui.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tableView.horizontalHeader().setMinimumSectionSize(10)
        # Adjust column widths to their content
        self.ui.tableView.resizeColumnsToContents()
        self.ui.tableView.setFocus()

        self.ui.tableView.setSelectionMode(QAbstractItemView.SelectionMode.MultiSelection)
        self.ui.tableView.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        # self.ui.tableView.selectRow(0)
        # self.selectedid(idindex=0)

        # Get Row selection
        # selection = self.ui.tableView.qi
        # selection.selectionChanged.connect(self.selectedid)

        selection_model = self.ui.tableView.selectionModel()
        selection_model.selectionChanged.connect(self.on_selectionChanged)

        self.ui.statusbar.showMessage("Ready")
        # selectedIndexes

        # NO EDIT TRIGGERS on tableview

    def selectedidvalue(self, idlist):
        idlist = ", ".join(str(x) for x in idlist)
        self.ui.statusbar.showMessage("Selected values: " + idlist)

    @Slot()
    def on_selectionChanged(self):
        # Collects a list of ID for deletion
        rows = self.ui.tableView.selectionModel().selectedRows()
        myidlist = []
        for item in rows:
            myidlist.append(item.data())

        myidlist.sort()
        self.idlist = myidlist

        s = ', '.join(str(x) for x in myidlist)
        self.ui.statusbar.showMessage(f"Selected values: {s}")

    def on_combobox_changed(self):
        print("URL SELECTION on_combobox_changed CHANGED")
        self.ui.statusbar.showMessage("URL to scrape: " + self.ui.comboBox.currentText())

    def redraw(self):
        print("REDRAW")
        self.call_table()

    def delete_btn(self, idlist):
        print(type(self.idlist))
        print(f"I am Delete selected id {self.idlist}")
        self.conn.delete_selectedids(self.idlist)
        if (self.conn.delete_selectedids):
            print("Return is TRUE")
            self.call_table()

    @Slot()
    def start_scrapy(self):
        # CHECK DATABASE IS NOT LOCKED.

        # CLOSE CONNECTION TO DATABASE SO NO CONFLICTS
        # self.conn.db.close()
        self.ui.statusbar.showMessage("RUNNING START_SCRAPY")

        print("CLOSED DATABASE CONNECTION")
        print("RUNNING START_SCRAPY")
        self.ui.textEdit.clear()
        project_dir = QDir.currentPath()
        # print(f"{project_dir}")
        self.process.setWorkingDirectory(project_dir)
        script_path = "run_spider.py"
        urlselected = str(self.ui.comboBox.currentText())
        spinboxvalue = str(self.ui.spinBox.value())
        args = [script_path, urlselected, spinboxvalue]
        self.process.start("python", args)

    @Slot()
    def handle_stdout(self):
        data = self.process.readAllStandardOutput().data().decode()
        self.ui.textEdit.append(data)
        self.ui.statusbar.showMessage(f"RUNNING: {data}")

    @Slot()
    def handle_stderr(self):
        data = self.process.readAllStandardError().data().decode()
        self.ui.textEdit.append(data)
        self.ui.statusbar.showMessage(f"RUNNING: {data}")

    @Slot()
    def process_finished(self, exit_code, exit_status):
        self.ui.textEdit.append(f"Process finished with exit code {exit_code} and exit status {exit_status}")
        self.ui.statusbar.showMessage(f"Process finished with exit code {exit_code} and exit status {exit_status}")

        if self.conn.db:
            print("CLOSING DB CONNECTION (main.process_finished)")
            self.conn.db.close()

        print("CALLING TO REDRAW")
        self.redraw()
        self.ui.statusbar.showMessage("RUNNING START_SCRAPY FINISHED")
