from PySide6.QtGui import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QLabel, QSpacerItem, QSizePolicy


class StateEncodingTab(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.countStates = QLineEdit()
        self.countStates.setStyleSheet("""
                            QLineEdit {
                                border: 1px solid #ccc;
                                border-radius: 4px;
                                padding: 5px;
                                background: white;
                                width: 200px;
                                font-family: 'Segoe UI', Arial, sans-serif;
                            }
                        """)
        self.countTriggers = QLineEdit()
        self.countTriggers.setStyleSheet("""
                                    QLineEdit {
                                        border: 1px solid #ccc;
                                        border-radius: 4px;
                                        padding: 5px;
                                        background: white;
                                        width: 200px;
                                        font-family: 'Segoe UI', Arial, sans-serif;
                                    }
                                """)
        layout.addWidget(QLabel("естик"))
        layout.addWidget(self.countStates, Qt.AlignRight)
        layout.addWidget(self.countTriggers, Qt.AlignRight)

        spacer = QSpacerItem(40,20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        layout.addSpacerItem(spacer)
        self.setLayout(layout)