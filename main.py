from components.views.mainScreen import MainScreen
from components.views.welcomeScreen import WelcomeScreen
from PySide6.QtWidgets import (QApplication,QMainWindow,QStackedWidget)
from PySide6.QtGui import QPalette, QColor
from PySide6.QtCore import Qt
class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Проектирование автомата Мура (реверсивный счетчик)")
        self.resize(1200, 700)

        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)

        self.welcome = WelcomeScreen(self)
        self.create_project = MainScreen(self)

        self.stack.addWidget(self.welcome)
        self.stack.addWidget(self.create_project)

        self.stack.setCurrentWidget(self.welcome)

    def show_create_project(self):
        self.stack.setCurrentWidget(self.create_project)

    def show_welcome(self):
        self.stack.setCurrentWidget(self.welcome)

def apply_light_palette(app: QApplication):
    """
    Применяет светлую тему, аналогичную твоему C++ коду
    """
    palette = QPalette()

    # Основные цвета окна и фона
    palette.setColor(QPalette.Window, QColor(240, 240, 240))
    palette.setColor(QPalette.WindowText, Qt.black)

    # Фон для редактируемых областей (QLineEdit, QTextEdit и т.д.)
    palette.setColor(QPalette.Base, QColor(255, 255, 255))
    palette.setColor(QPalette.AlternateBase, QColor(233, 231, 227))

    # Подсказки (tooltips)
    palette.setColor(QPalette.ToolTipBase, Qt.white)
    palette.setColor(QPalette.ToolTipText, Qt.black)

    # Текст в полях ввода
    palette.setColor(QPalette.Text, Qt.black)

    # Кнопки
    palette.setColor(QPalette.Button, QColor(240, 240, 240))
    palette.setColor(QPalette.ButtonText, Qt.black)

    # Яркий текст (обычно для акцентов/ошибок)
    palette.setColor(QPalette.BrightText, Qt.red)

    # Ссылки
    palette.setColor(QPalette.Link, QColor(0, 0, 255))

    # Выделение (selection)
    palette.setColor(QPalette.Highlight, QColor(0, 120, 215))
    palette.setColor(QPalette.HighlightedText, Qt.white)

    # Применяем палитру ко всему приложению
    app.setPalette(palette)


if __name__ == "__main__":
    app = QApplication([])
    apply_light_palette(app)
    app.setStyle('Fusion')
    window = MainWindow()
    window.show()
    app.exec()