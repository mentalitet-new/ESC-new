import sys

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QStyleFactory, QSizeGrip

from ui_main import Ui_MainWindow


class MainFrame(QMainWindow):
    def __init__(self):
        super(MainFrame, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        applicationName = "App Name"
        self.ui.label_top.setText(applicationName)

        self.setWindowFlags(Qt.FramelessWindowHint)
        # self.setAttribute(Qt.WA_TranslucentBackground)
        self.ui.pushButton_info.clicked.connect(lambda: self.swap_menu(1, True))
        self.ui.pushButton_find_camera.clicked.connect(lambda: self.swap_menu(2, True))
        self.dragPos = self.pos()

        def moveWindow(event):
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        self.ui.verticalFrame_top.mouseMoveEvent = moveWindow

        self.row_counter = 0
        self.print_test_text()
        self.init_columns_table()
        self.sizegrip = QSizeGrip(self.ui.lable_resize)

    def swap_menu(self, number_stack_wdgt, clicked):
        if clicked:
            if number_stack_wdgt == 2:
                self.ui.stackedWidget.setCurrentWidget(self.ui.page_table)
            elif number_stack_wdgt == 1:
                self.ui.stackedWidget.setCurrentWidget(self.ui.page_info)

    def init_columns_table(self):
        """
        Ресайз колонок
        """
        self.ui.tableWidget_search_camera.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.ui.tableWidget_search_camera.verticalHeader().setDefaultSectionSize(25)
        self.ui.tableWidget_search_camera.horizontalHeader().setDefaultSectionSize(130)
        self.ui.tableWidget_search_camera.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Fixed)
        self.ui.tableWidget_search_camera.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.ui.tableWidget_search_camera.horizontalHeader().setDefaultSectionSize(120)
        self.ui.tableWidget_search_camera.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Fixed)
        self.ui.tableWidget_search_camera.horizontalHeader().setDefaultSectionSize(120)
        self.ui.tableWidget_search_camera.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.Fixed)
        self.ui.tableWidget_search_camera.horizontalHeader().setDefaultSectionSize(120)
        self.ui.tableWidget_search_camera.horizontalHeader().setSectionResizeMode(3, QtWidgets.QHeaderView.Fixed)
        self.ui.tableWidget_search_camera.horizontalHeader().setDefaultSectionSize(140)
        self.ui.tableWidget_search_camera.horizontalHeader().setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch)

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainFrame()
    window.show()
    sys.exit(app.exec_())
