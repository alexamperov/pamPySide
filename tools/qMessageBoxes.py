from PySide6.QtWidgets import QMessageBox


def changeVariantMessageBox(parent) -> int:
    return QMessageBox().warning( parent,"Внимание!", "Смена варианта приведет к удалению данных"
                                                " на последующих вкладках",
                                 QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel, QMessageBox.Cancel)

def wrongVariantMessageBox(parent, upperBound : int):
    return QMessageBox().warning( parent,"Внимание!", f"Выберите вариант от 1 до {upperBound}",
                                 QMessageBox.Ok , QMessageBox.Ok)

def wrongCountsCheck(parent):
    return QMessageBox().warning( parent,"Внимание!", f"Количество состояний либо количество триггеров не соответствуют варианту!",
                                 QMessageBox.Ok , QMessageBox.Ok)

def rightCountsCheck(parent):
    return QMessageBox().information( parent,"Внимание!", f"Количество состояний и количество триггеров соответствуют варианту!",
                                 QMessageBox.Ok , QMessageBox.Ok)