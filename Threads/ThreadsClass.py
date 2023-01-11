from PyQt5 import QtCore
from PyQt5.QtCore import QThread
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from functools import wraps
from timeit import default_timer as timer
from starter import Searcher


def measure_time(func):
    @wraps(func)
    def handler(*args, **kwargs):
        print(f"Start {func.__name__}")
        start = timer()
        func(*args, **kwargs)
        stop = timer()
        print(f"Stop after {func.__name__} {stop - start} sec")
    return handler

class Sqlite3Handler:

    def write_db(self, columns):
        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('cameras.db')
        if not db.open():
            raise NotImplementedError('db not available!')

        query = QSqlQuery()
        query.exec_("DELETE FROM camera")

        for column in columns:
            query.exec_(f"INSERT INTO camera (model, mac, ip, mask, version, manufactured) VALUES('{column[0]}', "
                        f"'{column[1]}', '{column[2]}', '{column[3]}', '{column[4]}', '{column[5]}');")
        query.clear()
        db.close()

    def read_db(self):
        rows = []
        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('cameras.db')
        if not db.open():
            raise NotImplementedError('db not available!')

        query = QSqlQuery()
        query.exec_('select * from camera')
        while query.next():
            rows.append([query.value("model"), query.value("mac"), query.value("ip"),
                         query.value("mask"),
                         query.value("version")])
        query.clear()
        db.close()
        return rows

    def sort_db(self):
        rows = []
        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('cameras.db')
        if not db.open():
            raise NotImplementedError('db not available!')

        query = QSqlQuery()
        query.exec_('select * from camera ORDER BY ip asc')
        while query.next():
            rows.append([query.value("model"), query.value("mac"), query.value("ip"),
                         query.value("mask"),
                         query.value("version")])
        query.clear()
        db.close()
        return rows

class ThStarter(QThread):
    thread_signal = QtCore.pyqtSignal(list)
    s = Searcher()

    def run(self):
        try:
            sql = Sqlite3Handler()
            cams = self.s.search()
            sql.write_db(cams)
            self.thread_signal.emit(sql.read_db())
        except Exception as error:
            print(error)

class ThSort(QThread):
    thread_signal = QtCore.pyqtSignal(list)

    def run(self):
        try:
            sort = Sqlite3Handler()
            self.thread_signal.emit(sort.sort_db())
        except Exception as error:
            print(error)

class ThLastRecord(QThread):
    thread_signal = QtCore.pyqtSignal(list)

    def run(self):
        try:
            rec = Sqlite3Handler()
            self.thread_signal.emit(rec.read_db())
        except Exception as error:
            print(error)