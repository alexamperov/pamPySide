from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QLabel,
    QStackedWidget,
    QTabWidget, QSizePolicy, QMessageBox
)
from PySide6.QtCore import Qt
from tools.database import Database
from tabs.variantTab import VariantTab
from tools.qMessageBoxes import changeVariantMessageBox, wrongVariantMessageBox
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

        self.varTab = VariantTab(self.state,onChangeVariantRequested=self.onChangeVariantRequested)
        #TODO вынести все коннекты в отдельный метод
        self.varTab.variantSelected.connect(self.onVariantSelected)
        self.varTab.wrongVariantSelected.connect(self.onWrongVariantSelected)
        self.tabs.addTab(self.varTab, "Выбор варианта")

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

    #Биндинги
    #TODO Пока что заглушка
    def onNextClicked(self):
        print(self.state.var_number)

    #TODO Пока что заглушка
    def onSaveClicked(self):
        #TODO save function
        print("Save Clicked")

    #Reaction on Signals
    def onVariantSelected(self):
        print(f"Variant Selected {self.state.var_number}")
        #TODO открыть следующую вкладку

    def onWrongVariantSelected(self, upperBound:int):
        wrongVariantMessageBox(self, upperBound)
        print(f"Emit wrong variant with {upperBound} upperBound")

    #CallBacks
    def onChangeVariantRequested(self) -> bool:
        """
        :return: True -> если смена варианта подтверждена
        """
        #TODO вызвать метод для проверки заполнена ли следующая вкладка
        reply = changeVariantMessageBox(self)
        if reply == QMessageBox.Cancel:
            return False
        elif reply == QMessageBox.Save:
            #TODO save function
            print("Save Clicked")
            return True
        else:
            print("Discard Clicked")
            return True
