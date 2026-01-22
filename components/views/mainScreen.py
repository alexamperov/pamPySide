from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QTabWidget, QMessageBox
)
from components.tabs.variantTab import VariantTab
from components.tabs.stateEncodingTab import StateEncodingTab
from tools.checkType import CheckType
from tools.qMessageBoxes import changeVariantMessageBox, wrongVariantMessageBox, wrongCountsCheck, rightCountsCheck
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
        #TODO вынести в отдельный класс
        #   Метод отключения вкладок начиная с такой-то
        #   Метод открытия вкладки по такому-то индексу
        self.tabs = QTabWidget()
        self.tabs.setStyleSheet("""
            QTabBar::tab:disabled {
                background: #ccc;
                color: gray;
                border-left: 1px solid #ccc;
                border-top: 1px solid #ccc;
                border-right: 1px solid #ccc;
                border-top-left-radius: 3px;
                border-top-right-radius: 3px;
                padding-left: 5px;
                padding-right: 5px;
                margin-left: 1px;
            }
        """)

        self.varTab = VariantTab(self.state,onChangeVariantRequested=self.onChangeVariantRequested)

        #TODO вынести все коннекты в отдельный метод
        self.varTab.variantSelected.connect(self.onVariantSelected)
        self.varTab.wrongVariantSelected.connect(self.onWrongVariantSelected)
        self.tabs.addTab(self.varTab, "Выбор варианта")

        self.stateEncodingTab = StateEncodingTab(self.state)
        self.stateEncodingTab.checkResult.connect(self.onCheck)
        self.tabs.addTab(self.stateEncodingTab, "Кодировка состояний")

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

        btn_open = QPushButton("Открыть")


        btn_layout.addStretch(1)
        btn_layout.addWidget(btn_back)
        btn_layout.addWidget(btn_save)
        btn_layout.addWidget(btn_open)
        btn_layout.addWidget(btn_next)
        btn_layout.addStretch(1)

        btn_save.clicked.connect(self.onSaveClicked)
        btn_next.clicked.connect(self.onNextClicked)
        btn_open.clicked.connect(self.onOpenClicked)
        btn_back.clicked.connect(self.parent().show_welcome)

        return btn_layout

    #Биндинги
    #TODO Пока что заглушка
    def onNextClicked(self):
        print(self.state.var_number)

    #TODO Пока что заглушка
    def onSaveClicked(self):
        # TODO
        #   Открываем файл, пихаем туда стейт
        #   собираем конфиги таблиц и данные из вкладок и пихаем в файл
        print("Unimplemented")

    def onOpenClicked(self):
        # TODO
        #   Открываем файл, достаем из него стейт и данные
        #   Переопределяем self.state -> мы его закидывали во вкладки
        #   следовательно он автоматически должен поменяться
        #   Вызываем onOpen(...) у вкладок, которые подставят данные в текстовые поля
        #   и вызовут rebuild и setData
        print("Unimplemented")

    #Reaction on Signals
    def onVariantSelected(self):
        self.stateEncodingTab.variantChanged()
        #TODO открыть следующую вкладку

    def onWrongVariantSelected(self, upperBound:int):
        wrongVariantMessageBox(self, upperBound)

    def onCheck(self, is_valid : bool, typeMsg : CheckType):
        if typeMsg == CheckType.COUNTS and not is_valid:
            wrongCountsCheck(self)
        else:
            rightCountsCheck(self)

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
