from dataclasses import dataclass
@dataclass
class State:
    """
    field var_number
    field var_chosen
    field oneSequence
    field zeroSequence
    field basis
    field trigger
    """
    def __init__(self):
        self.var_chosen = False
        self.var_number = -999
        self.oneSequence = []
        self.zeroSequence = []
        self.trigger = ""
        self.basis = ""