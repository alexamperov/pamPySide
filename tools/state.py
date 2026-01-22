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
    triggerCount : int
    stateCount : int
    states : []
    def __init__(self, var_chosen = False, var_number = -1,
                 oneSequence = [], zeroSequence = [], typeTrigger = "",
                 basis = "", triggerCount = 0, stateCount = 0, states = []):
        self.var_chosen = var_chosen
        self.var_number = var_number
        self.oneSequence = oneSequence
        self.zeroSequence = zeroSequence
        self.typeTrigger = typeTrigger
        self.basis = basis
        self.triggerCount = triggerCount
        self.stateCount = stateCount
        self.states = states

    def update(self, var_chosen = False, var_number = -1,
               oneSequence = [], zeroSequence = [], typeTrigger = "",
               basis = "", triggerCount = 0, stateCount = 0, states = []):
        self.var_chosen = var_chosen
        self.var_number = var_number
        self.oneSequence = oneSequence
        self.zeroSequence = zeroSequence
        self.typeTrigger = typeTrigger
        self.basis = basis
        self.triggerCount = triggerCount
        self.stateCount = stateCount
        self.states = states