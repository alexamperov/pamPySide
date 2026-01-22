from components.tables.baseTable import BaseTable

class EncodeTable(BaseTable):

    countTriggers : int
    def __init__(self, countTriggers = 1):
        self.countTriggers = countTriggers
        rowCount, colCount = self.__calculate_dimensions(countTriggers)
        super().__init__(rowCount=rowCount, colCount=colCount)

    @staticmethod
    def __calculate_dimensions(countTriggers : int) -> list[int]:
        return 2+pow(2,countTriggers), 1 + countTriggers

    def rebuild(self, countTriggers):
        self.countTriggers = countTriggers
        rowCount, colCount = self.__calculate_dimensions(countTriggers)

        self.setRowCount(rowCount)
        self.setColumnCount(colCount)

        super().apply_config(config=self.build_config())

    def build_config(self) -> {}:

        headers= []
        for i in range(0,self.countTriggers**2-1):
            headers.append({
                "title": f"a{i}",
                "coords": (i + 2,0)
            })

        for i in range(0, self.countTriggers):
            headers.append(
                {
                    "title": f"Q{self.countTriggers - i}",
                    "coords": (1, i+1)
                }
            )
        headers.append(
            {
                "title": "Состояние",
                "coords": (0,0)
            }
        )
        headers.append(
            {
                "title": "Код",
                "coords": (0, 1)
            }
        )
        spans = [
            {
                "from": (0,0),
                "to": (1,0)
            },
            {
                "from": (0,1),
                "to": (0, 1+self.countTriggers)
            }
        ]


        config = {
            "regions": {
                "binary": [
                    {
                    "from": (2,1),
                    "to": (pow(2, self.countTriggers) + 1, self.countTriggers)
                    }
                ],
            },
            "headers": headers,
            "spans": spans,
            "binary_variants": ["0", "1"]
        }
        return config

    def onOpen(self, data: [], countTriggers):
        self.countTriggers = countTriggers
        self.rebuild(self.countTriggers)
        self.setData(data)