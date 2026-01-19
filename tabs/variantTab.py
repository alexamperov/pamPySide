from PySide6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout,
                               QLabel, QLineEdit, QPushButton,
                               QSizePolicy, QTextBrowser, QSpacerItem, QLayout)
from PySide6.QtCore import Qt, QSize

from tools.database import Database


class VariantTab(QWidget):
    def __init__(self, state = None):
        super().__init__()
        #Подгрузка базы
        self.variants = Database().fVars
        self.trigger_list = ["RS", "D", "T", "JK"]
        self.basis_list = ["Буля", "Пирса", "Шеффера"]

        #Config
        self.var_number = 0
        self.var_chosen = False

        if state is not None:
            self.state = state

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)

        label = QLabel("Вариантов в базе: " + str(len(self.variants)))
        layout.addWidget(label)

        varLayout = self.getVariantLayout()
        layout.addLayout(varLayout)

        dataLayout = self.getVariantDataLayout()

        layout.addWidget(dataLayout)

        layout.addStretch(1)
        self.setLayout(layout)

    def getVariantLayout(self):
        variant_layout = QHBoxLayout()
        variant_layout.addWidget(QLabel("Номер варианта:", alignment=Qt.AlignCenter))

        self.varEdit = QLineEdit()
        self.varEdit.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)

        self.acceptButton = QPushButton("Принять")
        self.acceptButton.setObjectName('acceptButton')

        self.acceptButton.clicked.connect(self.onClickButton)

        variant_layout.addWidget(self.varEdit)
        variant_layout.addWidget(self.acceptButton)

        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        return variant_layout

    def getVariantDataLayout(self):
        container = QWidget()
        variant_layout = QHBoxLayout()

        container.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        container.setFixedHeight(50)


        self.zeroSequencePreview = QTextBrowser()
        variant_layout.addWidget(self.zeroSequencePreview)

        self.oneSequencePreview = QTextBrowser()
        variant_layout.addWidget(self.oneSequencePreview)

        self.basisPreview = QTextBrowser()
        variant_layout.addWidget(self.basisPreview)

        self.triggerPreview = QTextBrowser()
        variant_layout.addWidget(self.triggerPreview)

        for i in variant_layout.children():
            i.setContentsMargins(100,0,100,0)

        container.setLayout(variant_layout)

        return container

    def onClickButton(self):

        #TODO Установка флага self.var_chosen
        #   Проверка был ли флаг установлен True
        #   Отправление сигнала variantSelected и
        #   отправка данных последовательностей, базиса и триггера
        #   Если флаг self.var_chosen был установлен - испускаем сигнал variantChangeRequested

        var_num = int(self.varEdit.text())

        self.state.var_number = var_num

        #Обновление текущих данных варианта
        zeroSequence = self.variants[var_num][0].split(" ")
        oneSequence = self.variants[var_num][1].split(" ")
        basis = self.basis_list[int(self.variants[var_num][3])]
        trigger = self.trigger_list[int(self.variants[var_num][2])]

        self.state.trigger = trigger
        self.state.basis = basis
        self.state.var_chosen = True
        self.state.oneSequence = oneSequence
        self.state.zeroSequence = zeroSequence

        #########################################################
        self.updatePreview()

    #Установка в превью текущих значений
    def updatePreview(self):
        self.zeroSequencePreview.setText(", ".join(self.state.zeroSequence))
        self.oneSequencePreview.setText(", ".join(self.state.oneSequence))
        self.triggerPreview.setText(self.state.trigger)
        self.basisPreview.setText(self.state.basis)