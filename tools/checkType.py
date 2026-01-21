from enum import Enum

class CheckType(Enum):
    COUNTS = "counts"
    ENCODE_STATES = "encode_states"
    TIME_DIAGRAM = "time_diagram"
    TRANSITIONS = "transitions"
    STRUCTURE = "structure"
    CARNO_MAP = "carno"