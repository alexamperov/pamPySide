from dataclasses import asdict

from PySide6.QtCore import Signal
from PySide6.QtWidgets import (QWidget, QVBoxLayout,
                               QSizePolicy, QHBoxLayout,
                               QPushButton, QLabel)
from components.compound.labeledInput import LabeledInput
from tools.state import State
import math
from PySide6.QtCore import Qt
from tools.checkType import CheckType
from components.tables.encodeTable import EncodeTable

class StateEncodingTab(QWidget):
    #fields
    countStatesInput : LabeledInput
    countTriggersInput : LabeledInput

    #Signals
    checkResult = Signal(bool, CheckType)

    def __init__(self, state : State):
        super().__init__()
        self.state = state
        self.init_ui()

    def init_ui(self):
        #Tab Container
        container = QVBoxLayout()

        #Upper Block with Count inputs and Variant Data above Table Layout
        infoInputLayout = QHBoxLayout()
        infoInputLayout.setAlignment(Qt.AlignmentFlag.AlignTop)

        #Variant Data block
        self.infolabel = self.__create_info_label__()

        #Count inputs block
        self.countBlock = self.__create_count_block()
        self.infolabel.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        infoInputLayout.addWidget(self.infolabel)
        infoInputLayout.addWidget(self.__create_count_block())

        container.addLayout(infoInputLayout)

        self.table = EncodeTable(self.state.tabs["encoding"].triggerCount)
        self.table.setVisible(False)

        checkTableButton = QPushButton("Принять")
        checkTableButton.clicked.connect(self.__checkStates__)

        container.addWidget(self.table)
        container.addWidget(checkTableButton)
        self.setLayout(container)

# Creating Blocks Methods
    def __create_count_block(self) -> QWidget:
        """
        Input Data Block with CountTriggers and CountStates
        """
        countBlock = QWidget()
        container = QHBoxLayout()

        # fieldsLayout -> контейнер с полями и кнопкой
        fieldsLayout = QVBoxLayout()
        self.countStatesInput = LabeledInput(text="Максимальное количество состояний в циклах", isVertical=False)
        self.countTriggersInput = LabeledInput(text="Требуемое количество триггеров log₂ Nₘₐₓ", isVertical=False)
        fieldsLayout.addWidget(self.countStatesInput)
        fieldsLayout.addWidget(self.countTriggersInput)

        countsCheckButton = QPushButton("Принять")
        countsCheckButton.clicked.connect(self.__checkCounts__)

        countsCheckButton.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        container.addLayout(fieldsLayout)
        container.addSpacing(30)
        container.addWidget(countsCheckButton)

        # Fixed left position of block
        container.setAlignment(Qt.AlignmentFlag.AlignLeft)
        countBlock.setLayout(container)
        return countBlock

    def __create_info_label__(self) -> QWidget:
        """
        Variant Data block
        """
        infolabel = QVBoxLayout()

        zeroInfo = QHBoxLayout()
        zeroInfo.addWidget(QLabel("X = 0"))
        zeroInfo.addSpacing(20)
        self.zeroData = QLabel(" ".join(self.state.variant.zeroSequence))
        zeroInfo.addWidget(self.zeroData, alignment=Qt.AlignmentFlag.AlignLeft)

        oneInfo = QHBoxLayout()
        oneInfo.addWidget(QLabel("X = 1"))
        oneInfo.addSpacing(20)
        self.oneData = QLabel(" ".join(self.state.variant.oneSequence))
        self.oneData.setAlignment(Qt.AlignmentFlag.AlignLeft)
        oneInfo.addWidget(self.oneData, alignment=Qt.AlignmentFlag.AlignLeft)

        zeroInfo.setContentsMargins(0, 5, 0, 5)
        oneInfo.setContentsMargins(0, 5, 0, 5)

        infolabel.addLayout(zeroInfo)
        infolabel.addLayout(oneInfo)

        container = QWidget()
        container.setLayout(infolabel)
        return container
#########################

############## Checking
    # Check Counts Algorythm
    def __checkCounts__(self):
        self.state.tabs["encoding"].isCountsRight = True
        try:
            self.state.tabs["encoding"].triggerCount = int(self.countTriggersInput.getText())
            self.state.tabs["encoding"].stateCount = int(self.countStatesInput.getText())
        except ValueError:
            self.state.tabs["encoding"].isCountsRight = False
            self.checkResult.emit(False, CheckType.COUNTS)
            return

        if self.state.tabs["encoding"].stateCount != max(len(self.state.variant.zeroSequence),
                                                         len(self.state.variant.oneSequence)):
            self.state.tabs["encoding"].countsRight = False
        if self.state.tabs["encoding"].triggerCount != math.ceil(
                math.log2(self.state.tabs["encoding"].stateCount)):
            self.state.tabs["encoding"].isCountsRight = False

        if self.state.tabs["encoding"].isCountsRight:
            self.table.rebuild(self.state.tabs["encoding"].triggerCount)
            self.state.tabs["encoding"].isTableVisible = True
            self.table.setVisible(True)
        self.checkResult.emit(self.state.tabs["encoding"].isCountsRight, CheckType.COUNTS)

    # Check Table Slot
    def __checkStates__(self):
        (self.state.tabs["encoding"].isVerified,
         self.state.tabs["encoding"].states) = self.table.check()
        self.checkResult.emit(self.state.tabs["encoding"].isVerified,
                              CheckType.ENCODE_STATES)
##############

############## Refreshing
    # Updating data info on changed variant
    def __updateInfoLabel__(self):
        """
        Func update Variant Data from state when variant changed
        """
        self.zeroData.setText(" ".join(self.state.variant.zeroSequence))
        self.oneData.setText(" ".join(self.state.variant.oneSequence))
        self.infolabel.update()
##############

############## Func clearing inputs and updates data
    def variantChanged(self):
        self.__updateInfoLabel__()

        self.countStatesInput.setText()
        self.countTriggersInput.setText()
        #Пока что здесь, чтобы не разносить логику вверх - но можно реакцию сделать на очищение
        self.state.tabs["encoding"].isVerified = False
        self.table.setVisible(self.state.tabs["encoding"].isTableVisible)

    def onOpen(self):
        if self.state.tabs["encoding"].triggerCount:
            self.countTriggersInput.setText(
            str(self.state.tabs["encoding"].triggerCount))

        if self.state.tabs["encoding"].stateCount:
            self.countStatesInput.setText(
                str(self.state.tabs["encoding"].stateCount))

        self.table.setVisible(self.state.tabs["encoding"].isTableVisible)
        self.table.restore_from_data(self.state.tabs["encoding"].tableData,
                                     self.state.tabs["encoding"].triggerCount)

    def onSave(self):
        self.state.tabs["encoding"].tableData = self.table.getData()

