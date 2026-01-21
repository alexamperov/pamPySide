from PySide6.QtGui import QTextOption
from PySide6.QtWidgets import QWidget, QVBoxLayout, QTextBrowser, QLabel, QLayout
from PySide6.QtCore import Qt
from shiboken6.Shiboken import Object


class LabeledText(QWidget):
    """
    Custom Component with QTextBrowser under QLabel
    """
    sizeContainer = Object
    isFilling : bool

    def __init__(self, textBrowser :QTextBrowser, text = "",
                 variant="normal", isFixed = False, scrollsHidden = True):
        """
        :param textBrowser: injected textBrowser
        :param text: text on label
        :param variant: size (200, 40) if normal
        :param isFixed: textBrowser filling width with False else used fixed size from variant type
        :param scrollsHidden: hide all scroolbars if True
        """
        super().__init__()

        self.textBrowser = textBrowser
        self.text = text

        self.scrollsHidden = scrollsHidden
        self.isFilling = not isFixed

        if variant == "normal":
            self.sizeContainer.width = 200
            self.sizeContainer.height = 40

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.textBrowser.setStyleSheet("""
                                QTextBrowser {
                                    border: 1px solid #ccc;
                                    border-radius: 4px;
                                    padding: 5px;
                                    background: white;
                                    margin-left: 10px;
                                    margin-right: 10px;
                                    font-family: 'Segoe UI', Arial, sans-serif;
                                    font-size: 14px
                                }
                            """)

        if self.scrollsHidden:
            self.textBrowser.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
            self.textBrowser.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        # Центрирование внутри поля
        option = QTextOption()
        option.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Центрирование
        self.textBrowser.document().setDefaultTextOption(option)

        if not self.isFilling:
            self.textBrowser.setFixedSize(self.sizeContainer.width, self.sizeContainer.height)
        else:
            self.textBrowser.setFixedHeight(self.sizeContainer.height)

        label = QLabel(self.text)
        label.setStyleSheet("""
            QLabel {
            font-family: 'Segoe UI', Arial, sans-serif;
            font-size: 14px
            }
            """)

        layout.addWidget(label, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.textBrowser)
        self.setLayout(layout)

