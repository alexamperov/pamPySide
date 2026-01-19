from PySide6.QtWidgets import (
    QApplication,QMainWindow,QWidget,
    QVBoxLayout,QHBoxLayout,QPushButton,
    QLabel,QStackedWidget,QTabWidget
)
from PySide6.QtCore import Qt


class WelcomeScreen(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)
        layout.setSpacing(40)


        subtitle = QLabel("Выберите действие для начала работы")
        subtitle.setAlignment(Qt.AlignCenter)
        subtitle.setStyleSheet("font-size: 16px; color: #666;")

        btn_layout = QHBoxLayout()
        btn_create = QPushButton("Создать проект")
        btn_create.setFixedSize(200, 40)
        btn_open = QPushButton("Открыть проект")
        btn_open.setFixedSize(200, 40)
        btn_open.setEnabled(False)  # пока неактивна, как просил

        layout.addStretch(1)
        layout.addWidget(subtitle)
        layout.addSpacing(40)
        btn_layout.addWidget(btn_create, alignment=Qt.AlignCenter)
        btn_layout.addWidget(btn_open, alignment=Qt.AlignCenter)
        layout.addLayout(btn_layout)
        layout.addStretch(1)

        self.setLayout(layout)

        # Сигнал
        btn_create.clicked.connect(self.parent().show_create_project)