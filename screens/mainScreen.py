from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QLabel,
    QStackedWidget,
    QTabWidget, QSizePolicy
)
from PySide6.QtCore import Qt
from tools.database import Database
from tabs.variantTab import VariantTab
from tools.state import State


class MainScreen(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.varData = {}

        self.state = State()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(20)

        # Вкладки
        self.tabs = QTabWidget()
        self.tabs.addTab(VariantTab(self.state), "Выбор варианта")



        layout.addWidget(self.tabs)

        layout.addLayout(self.getToolBar())

        self.setLayout(layout)

        # Подключение кнопки Назад


    def getToolBar(self):
        # Нижние кнопки
        btn_layout = QHBoxLayout()
        btn_layout.setSpacing(20)
        btn_back = QPushButton("Назад")
        btn_save = QPushButton("Сохранить")
        btn_next = QPushButton("Далее")

        btn_layout.addStretch(1)
        btn_layout.addWidget(btn_back)
        btn_layout.addWidget(btn_save)
        btn_layout.addWidget(btn_next)
        btn_layout.addStretch(1)

        btn_save.clicked.connect(self.onSaveClicked)
        btn_next.clicked.connect(self.onNextClicked)
        btn_back.clicked.connect(self.parent().show_welcome)

        return btn_layout

    #TODO Пока что заглушка
    def onNextClicked(self):
        print(self.state.var_number)

    #TODO Пока что заглушка
    def onSaveClicked(self):
        print("Save Clicked")