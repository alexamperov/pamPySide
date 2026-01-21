from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel, QLineEdit, QWidget, QVBoxLayout, QHBoxLayout


class LabeledInput(QWidget):
    def __init__(self, isVertical = True, text = "",  fieldWidth = 200, width = 500):
        super().__init__()
        self.text = text
        self.isVertical = isVertical
        self.fieldWidth = fieldWidth
        self.setFixedWidth(width)
        self.margins = (0,0,0,0)
        self.init_ui()

    def init_ui(self):
        if self.isVertical:
            layout = QVBoxLayout()
        else:
            layout = QHBoxLayout()

        layout.setContentsMargins(0,0,0,0)
        # TODO
        #   Добавить поверх QHBoxLayout если isVertical == True
        #   и выранивать его по центру по высоте относительно поля

        # FIXME Слишком большие отступы между LabeledInput, сделать их настраиваемыми

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
        label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.input.setFixedWidth(self.fieldWidth)
        self.input.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.setLayout(layout)

    def getText(self):
        return self.input.text()
