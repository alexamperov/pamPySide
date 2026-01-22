from PySide6.QtWidgets import QTableWidget, QTableWidgetItem
from PySide6.QtCore import Qt

class BaseTable(QTableWidget):
    config : {}
    def __init__(self, rowCount:int, colCount:int):
        super().__init__(rowCount=rowCount, columnCount=colCount)
        self.verticalHeader().setVisible(False)
        self.horizontalHeader().setVisible(False)
        self.config = self.build_config()

        self.init_ui()

    def init_ui(self):
        self.setVisible(True)

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
        headers = config.get("headers", [])
        spans = config.get("spans", [])
        regions = config.get("regions", {})

        binary = regions.get("binary", [])
        for i in headers:
            item = QTableWidgetItem()
            item.setText(i["title"])
            self.setItem(i["coords"][0],i["coords"][1], item)
            item.setFlags(item.flags() &~Qt.ItemFlag.ItemIsEditable &~Qt.ItemFlag.ItemIsSelectable)
            item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

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

    def check(self) -> bool:
        print("Unoverrided method")
        return True
