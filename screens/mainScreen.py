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


class MainScreen(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.varData = {}
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(20)

        # Вкладки
        self.tabs = QTabWidget()
        self.tabs.addTab(VariantTab(), "Выбор варианта")

        tab2 = QWidget()
        tab2_layout = QVBoxLayout()
        tab2_layout.addWidget(QLabel("Кодировка состояний\n(пока пусто)", alignment=Qt.AlignCenter))
        tab2.setLayout(tab2_layout)
        self.tabs.addTab(tab2, "Кодировка состояний")

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

        layout.addWidget(self.tabs)

        layout.addLayout(btn_layout)

        self.setLayout(layout)

        # Подключение кнопки Назад
        btn_back.clicked.connect(self.parent().show_welcome)