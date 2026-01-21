from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel, QLineEdit, QWidget, QVBoxLayout, QHBoxLayout


class LabeledInput(QWidget):
    def __init__(self, isVertical = True, text = "",
                 fieldWidth = 200, width = 480,
                 hMargin = 0, vMargin = 0):
        super().__init__()
        self.text = text
        self.isVertical = isVertical
        self.fieldWidth = fieldWidth
        self.setFixedWidth(width)
        self.margins = (hMargin, vMargin, hMargin, vMargin)

        self.init_ui()

    def init_ui(self):

        if self.isVertical:
            layout = QVBoxLayout()
        else:
            layout = QHBoxLayout()

        layout.setContentsMargins(*self.margins)

        # Adding label
        label = QLabel(self.text)
        label.setStyleSheet("""
            QLabel {
            font-family: 'Segoe UI', Arial, sans-serif;
            font-size: 12px;
            margin: 0;
            }
            """)
        layout.addWidget(label)

        self.input = QLineEdit()
        self.input.setStyleSheet("""
                            QLineEdit {
                                border: 1px solid #ccc;
                                border-radius: 4px;
                                padding: 3px;
                                background: white;
                                margin: 0;
                                font-family: 'Segoe UI', Arial, sans-serif;
                            }
                        """)

        layout.addWidget(self.input)

        label.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)

        self.input.setFixedWidth(self.fieldWidth)
        self.input.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.setLayout(layout)

    def getText(self):
        return self.input.text()

    def setText(self, text = ""):
        return self.input.setText(text)
