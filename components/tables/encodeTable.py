from components.tables.baseTable import BaseTable

class EncodeTable(BaseTable):

    countTriggers : int
    def __init__(self, countTriggers = 1):
        self.countTriggers = countTriggers
        rowCount, colCount = self.__calculate_dimensions(countTriggers)
        super().__init__(rowCount=rowCount, colCount=colCount)

    @staticmethod
    def __calculate_dimensions(countTriggers : int) -> list[int]:
        return 1+pow(2,countTriggers), 1 + countTriggers

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
                "coords": (i + 1,0)
            })

        for i in range(0, self.countTriggers):
            headers.append(
                {
                    "title": f"Q{self.countTriggers - i}",
                    "coords": (0, i+1)
                }
            )

        config = {
            "regions": {
                "binary": [
                    {
                    "from": (1,1),
                    "to": (self.countTriggers ** 2 + 1, 1 + self.countTriggers)
                    }
                ],
            },
            "headers": headers
        }
        return config
