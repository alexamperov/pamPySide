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

    def from_dict(self, data: dict):
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)

@dataclass
class EncodingTabState:
    triggerCount: int = 0
    stateCount: int = 0
    isTableVisible:bool = False
    isCountsRight:bool = False
    isVerified : bool = False
    tableData : List[Dict[str, Any]]= field(default_factory=list)
    states: List[Dict[str, Any]] = field(default_factory=dict)

    def from_dict(self, data: dict):
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)

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

    def from_dict(self, data:dict[str, Any]):
        self.variant.from_dict(data["variant"])
        self.tabs["variant"].from_dict(data["variant"])
        self.tabs["encoding"].from_dict(data["tabs"]["encoding"])
