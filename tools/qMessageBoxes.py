from PySide6.QtWidgets import QMessageBox


def changeVariantMessageBox(parent) -> int:
    return QMessageBox().warning( parent,"Внимание!", "Смена варианта приведет к удалению данных"
                                                " на последующих вкладках",
                                 QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel, QMessageBox.Cancel)

def wrongVariantMessageBox(parent, upperBound : int):
    return QMessageBox().warning( parent,"Внимание!", f"Выберите вариант от 1 до {upperBound}",
                                 QMessageBox.Ok , QMessageBox.Ok)