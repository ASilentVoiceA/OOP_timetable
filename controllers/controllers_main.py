from PyQt5.QtWidgets import QTableWidgetItem

from db_timetable.database import *
from views.gui_timetable import *
from views.gui_dialog_update import *
from views.gui_dialog_add import *
from pony.orm import *

import sys


class MainForm(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)  # Это нужно для инициализации дизайна
        self.ui.add_button.clicked.connect(self.open_dialog_add)
        self.ui.update_button.clicked.connect(self.open_dialog_update)
        # очистка содержимого таблицы при клике на кнопку.
        self.ui.clear_button.clicked.connect(self.clear_tableWidget)
        self.ui.find_button.clicked.connect(self.find_table)

        with db_session:
            self.ui.comboBox_3.addItems(select(d.name for d in Discipline))
            self.ui.comboBox.addItems(select(dw.name for dw in DayWeek))
            self.ui.comboBox_4.addItems(select(c.full_class for c in Class))
            self.ui.comboBox_5.addItems(select(c.number + " корпус " + c.housing.name for c in Cabinet))
            self.ui.comboBox_2.addItems(select(str(l.number) for l in LessonNumber))
            self.ui.comboBox_6.addItems(select(t.full_name for t in Teacher))

    def clear_tableWidget(self):
        self.ui.tableWidget.clearContents()

    # заполнение таблицы
    def fill_table(self):
        self.ui.tableWidget.clear()

        labels = ['День недели', 'Номер урока', 'Дисциплина', 'Класс', 'Кабинет', 'Учитель']

        self.ui.tableWidget.setColumnCount(len(labels))  # добавление столбцов таблицы
        self.ui.tableWidget.setHorizontalHeaderLabels(labels)  # заголовки для столбцов.

        with db_session:
            for day_week, num_less, klass, teacher, discipline, cabinet in select((t.day_week, t.lesson_number, t.klass,
                                                                                   t.teacher, t.discipline, t.cabinet)
                                                                                  for t in Timetable):
                row = self.ui.tableWidget.rowCount()
                self.ui.tableWidget.setRowCount(row + 1)

                self.ui.tableWidget.setItem(row, 0, QTableWidgetItem(day_week.name))
                self.ui.tableWidget.setItem(row, 1, QTableWidgetItem(str(num_less.number)))
                self.ui.tableWidget.setItem(row, 2, QTableWidgetItem(discipline.name))
                self.ui.tableWidget.setItem(row, 3, QTableWidgetItem(klass.full_class))
                self.ui.tableWidget.setItem(row, 4, QTableWidgetItem(cabinet.full_cabinet))
                self.ui.tableWidget.setItem(row, 5, QTableWidgetItem(teacher.full_name))

    def find_table(self):
        pass
        # for item in self.ui.tableWidget.selectedItems():
        #     print(item.text())

    def open_dialog_add(self):
        self.add_window = AddForm(self)
        self.add_window.show()


    def open_dialog_update(self):
        self.update_window = UpdateForm(self)
        self.update_window.show()


class AddForm(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.add_window = Ui_Dialog_Add()
        self.add_window.setupUi(self)

class UpdateForm(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.update_window = Ui_Dialog_Update()
        self.update_window.setupUi(self)
        #self.update_window.lineEdit_3.setText(Ui_MainWindow.tableWidget.selectedItems()[0].text())
        #self.update_window.lineEdit_3.setText(MainForm.fill_line_update_form)

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = MainForm()  # Создаём объект класса MainForm()
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


if __name__ == "__main__":
    main()
