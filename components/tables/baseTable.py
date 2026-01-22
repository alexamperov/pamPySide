from PySide6.QtWidgets import QTableWidget, QTableWidgetItem
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor

class BaseTable(QTableWidget):
    _last_config : {}

    def __init__(self, rowCount:int, colCount:int):
        super().__init__(rowCount=rowCount, columnCount=colCount)
        self.verticalHeader().setVisible(False)
        self.horizontalHeader().setVisible(False)
        self.config = self.build_config()
        self.apply_config(self.config)
        self.init_ui()

    def init_ui(self):
        self.setAlternatingRowColors(True)

    def __highlightErrors(self, forRow = False, forColumn = True, avoidHeaders = True):
        print("Unimplemented")

    def build_config(self) -> {}:
        """
        Must Return config set
        config = {
            "regions": {
                "binary": [],
                "editable": []
            },
            "binaryVariants": [],
            "headers": [
                {
                   "title": "",
                   "cords": (0, 0)
                }
            ]
        }
        """
        raise NotImplementedError("Child class not implemented this method")

    def apply_config(self, config):

        if hasattr(self, "_last_config") and self._last_config == config:
            return
        self._last_config = config.copy()

        headers = config.get("headers", [])
        spans = config.get("spans", [])
        regions = config.get("regions", {})

        binary = regions.get("binary", [])
        for i in headers:
            item = QTableWidgetItem()
            item.setText(i["title"])
            item.setBackground(QColor("gray"))
            item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            item.setFlags(item.flags()
                          &~Qt.ItemFlag.ItemIsEditable
                          &~Qt.ItemFlag.ItemIsSelectable)
            self.setItem(i["coords"][0],i["coords"][1], item)

        for i in spans:
            self.setSpan(
                i["from"][0],
                i["from"][1],
                i["to"][0]-i["from"][0] + 1,
                i["to"][1]-i["from"][1] + 1)

        for i in binary:
            for row in range(i["from"][0], i["to"][0] + 1):
                for col in range(i["from"][1], i["to"][1] + 1):
                    item = QTableWidgetItem()
                    item.setText("0")
                    item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)
                    item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                    self.setItem(row, col, item)

    # TODO добавить еще трипл регион для [0,1,*] для структурной таблицы
    def mouseDoubleClickEvent(self, event, /):
        index = self.indexAt(event.pos())

        if index.isValid():
            row, col = index.row(), index.column()
            item = self.item(row, col)
            binary = self._last_config.get("regions", {}).get("binary", [])

            variants = self._last_config.get("binary_variants")
            for i in binary:
                if row >= i["from"][0] & row <= i["to"][0]:
                    if col >= i["from"][1] & col <= i["to"][1]:
                        print(i["to"][1])
                        if item.text() in variants:
                            nextIndex = (variants.index(item.text()) + 1) % len(variants)
                            item.setText(variants[nextIndex])
        super().mouseDoubleClickEvent(event)

    #TODO Override doubleClick Event Reaction
    def check(self) -> bool:
        print("Unoverrided method")
        return True
