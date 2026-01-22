from PySide6.QtWidgets import QTableWidget, QTableWidgetItem


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

        for i in headers:
            item = QTableWidgetItem()
            item.setText(i["title"])
            self.setItem(i["coords"][0],i["coords"][1], item)


    def check(self) -> bool:
        print("Unoverrided method")
        return True
