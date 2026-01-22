from dataclasses import asdict

from PySide6.QtCore import Signal
from PySide6.QtWidgets import (QWidget, QVBoxLayout,
                               QSpacerItem, QSizePolicy,
                               QHBoxLayout, QPushButton,
                               QLabel)
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
    triggers : int

    countsRight : bool
    tableRight : bool

    #Signals
    checkResult = Signal(bool, CheckType)

    def __init__(self, state : State):
        super().__init__()
        self.state = state
        self.tableRight = False
        self.init_ui()

    def init_ui(self):
        #Tab Container
        container = QVBoxLayout()

        #Upper Block with Count inputs and Variant Data above Table Layout
        infoInputLayout = QHBoxLayout()
        infoInputLayout.setAlignment(Qt.AlignmentFlag.AlignTop)

        #Variant Data block
        self.infolabel = self.createInfoLabel()

        #Count inputs block
        self.countBlock = self.createCountBlock()
        self.infolabel.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        infoInputLayout.addWidget(self.infolabel)
        infoInputLayout.addWidget(self.createCountBlock())

        container.addLayout(infoInputLayout)

        self.table = EncodeTable(self.state.triggerCount)
        self.table.setVisible(False)

        checkTableButton = QPushButton("Принять")
        checkTableButton.clicked.connect(self.__checkStates__)

        container.addWidget(self.table)
        container.addWidget(checkTableButton)
        self.setLayout(container)

# Creating Blocks Methods
    def createCountBlock(self) -> QWidget:
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

    def createInfoLabel(self) -> QWidget:
        """
        Variant Data block
        """
        infolabel = QVBoxLayout()

        zeroInfo = QHBoxLayout()
        zeroInfo.addWidget(QLabel("X = 0"))
        zeroInfo.addSpacing(20)
        self.zeroData = QLabel(" ".join(self.state.zeroSequence))
        zeroInfo.addWidget(self.zeroData, alignment=Qt.AlignmentFlag.AlignLeft)

        oneInfo = QHBoxLayout()
        oneInfo.addWidget(QLabel("X = 1"))
        oneInfo.addSpacing(20)
        self.oneData = QLabel(" ".join(self.state.oneSequence))
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

    # Check Counts Algorythm
    def __checkCounts__(self):
        countMatch = True
        try:
            self.state.triggerCount = int(self.countTriggersInput.getText())
            self.state.stateCount = int(self.countStatesInput.getText())
        except ValueError:
            self.checkResult.emit(False, CheckType.COUNTS)
            return

        if self.state.stateCount != max(len(self.state.zeroSequence), len(self.state.oneSequence)):
            countMatch = False
        if self.state.triggerCount != math.ceil(math.log2(self.state.stateCount)):
            countMatch = False

        self.countsRight = countMatch
        if countMatch:
            self.table.rebuild(self.state.triggerCount)
            self.table.setVisible(True)
        self.checkResult.emit(countMatch, CheckType.COUNTS)

    # Check Table Slot
    def __checkStates__(self):
        isValid, states = self.table.check()
        if isValid:
            self.state.states = states
        self.checkResult.emit(isValid, CheckType.ENCODE_STATES)

    # Updating data info on changed variant
    def __updateInfoLabel__(self):
        """
        Func update Variant Data from state
        """
        self.zeroData.setText(" ".join(self.state.zeroSequence))
        self.oneData.setText(" ".join(self.state.oneSequence))
        self.infolabel.update()

    def variantChanged(self):
        self.__updateInfoLabel__()

        self.countStatesInput.setText()
        self.countTriggersInput.setText()
        self.table.setVisible(False)

    def onOpen(self, data):
        self.countTriggersInput.setText(str(self.state.triggerCount))
        self.countStatesInput.setText(str(self.state.stateCount))

        self.countsRight = data.get("countsRight", False)
        self.tableRight = data.get("tableRight", False)
        if self.countsRight:
            self.table.setVisible(True)
        tableData = data.get("tableData", [])


        self.table.onOpen(tableData, self.state.triggerCount)

    def onSave(self):

        return {
            "countsRight": self.countsRight,
            "tableRight": self.tableRight,
            "tableData": self.table.getData()
        }