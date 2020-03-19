from views.gui_timetable import *
from views.gui_dialog_update import *
from views.gui_dialog_add import *
import sys


class MainForm(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)  # Это нужно для инициализации дизайна
        self.ui.add_button.clicked.connect(self.open_dialog_add)
        self.ui.update_button.clicked.connect(self.open_dialog_update)
        # очистка содержимого таблицы при клике на кнопку.
        self.ui.clear_button.clicked.connect(self.clear)
        # добавление столбцов
        self.ui.tableWidget.setColumnCount(6)
        self.ui.tableWidget.setRowCount(3)
        # заголовки для столбцов.
        self.ui.tableWidget.setHorizontalHeaderLabels(
            ('День недели', 'Номер урока', 'Дисциплина', 'Класс', 'Кабинет', 'Учитель')
        )

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
