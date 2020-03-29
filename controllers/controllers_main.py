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
        # добавление столбцов
        self.ui.tableWidget.setColumnCount(6)
        self.ui.tableWidget.setRowCount(3)
        # заголовки для столбцов.
        self.ui.tableWidget.setHorizontalHeaderLabels(
            ('День недели', 'Номер урока', 'Дисциплина', 'Класс', 'Кабинет', 'Учитель')
        )
        with db_session:
            self.ui.comboBox_3.addItems(select(d.name for d in Discipline))
            self.ui.comboBox.addItems(select(dw.name for dw in DayWeek))
            self.ui.comboBox_4.addItems(select(c.full_class for c in Class))
            self.ui.comboBox_5.addItems(select(c.number+" корпус "+c.housing.name for c in Cabinet))
            self.ui.comboBox_2.addItems(select(str(l.number) for l in LessonNumber))
            self.ui.comboBox_6.addItems(select(t.full_name for t in Teacher))

    def open_dialog_add(self):
        dialog = QtWidgets.QDialog()
        dialog.ui = Ui_Dialog_Add()
        dialog.ui.setupUi(dialog)
        dialog.exec_()
        dialog.show()

    def open_dialog_update(self):
        dialog = QtWidgets.QDialog()
        dialog.ui = Ui_Dialog_Update()
        dialog.ui.setupUi(dialog)
        dialog.exec_()
        dialog.show()

    def clear_tableWidget(self):
        self.ui.tableWidget.clearContents()


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = MainForm()  # Создаём объект класса MainForm()
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


if __name__ == "__main__":
    main()
