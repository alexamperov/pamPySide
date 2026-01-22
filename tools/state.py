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
    var_chosen :bool
    var_number : int
    oneSequence : []
    zeroSequence : []
    typeTrigger : str
    basis : str
    triggers : int
    states : int
    def __init__(self, var_chosen = False, var_number = -1,
                 oneSequence = [], zeroSequence = [], typeTrigger = "",
                 basis = "", triggers = 0, states = 0):
        self.var_chosen = var_chosen
        self.var_number = var_number
        self.oneSequence = oneSequence
        self.zeroSequence = zeroSequence
        self.typeTrigger = typeTrigger
        self.basis = basis
        self.triggers = triggers
        self.states = states

    def update(self, var_chosen = False, var_number = -1,
                 oneSequence = [], zeroSequence = [], typeTrigger = "",
                 basis = "", triggers = 0, states = 0):
        self.var_chosen = var_chosen
        self.var_number = var_number
        self.oneSequence = oneSequence
        self.zeroSequence = zeroSequence
        self.typeTrigger = typeTrigger
        self.basis = basis
        self.triggers = triggers
        self.states = states