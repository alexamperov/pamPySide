from dataclasses import dataclass, field
from typing import Any, Dict, Optional, List


@dataclass
class VariantState:
    var_chosen: bool = False
    var_number: Optional[int] = None
    oneSequence: List[str] = field(default_factory=list)
    zeroSequence: List[str] = field(default_factory=list)
    typeTrigger: str = ""
    typeBasis: str = ""

class EncodingTabState:
    triggerCount: int
    stateCount: int
    isTableVisible:bool
    isCountsRight:bool
    isVerified : bool
    tableData : field(default_factory=List[Dict[str, Any]])
    states: List[Dict[str, Any]] = field(default_factory=dict)

@dataclass
class State:

    variant : VariantState = field(default_factory=VariantState)
    tabs: Dict[str, Any] = field(default_factory=dict)

    def __post_init__(self):
        if not self.tabs:
            self.tabs = {
                'variant': self.variant,
                'encoding': EncodingTabState(),
                'transitions': {} #TODO
            }

