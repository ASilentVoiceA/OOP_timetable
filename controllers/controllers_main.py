from views.gui_timetable import *
from views.gui_dialog_update import *
from views.gui_dialog_add import *
import sys


class MainForm(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = UiMainWindow()
        self.ui.setupUi(self)  # Это нужно для инициализации дизайна
        self.ui.add_button.clicked.connect(self.open_dialog_add)
        self.ui.update_button.clicked.connect(self.open_dialog_update)

    def open_dialog_add(self):
        print("add")

    def open_dialog_update(self):
        print("update")


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = MainForm()  # Создаём объект класса MyWin
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


if __name__ == "__main__":
    main()
