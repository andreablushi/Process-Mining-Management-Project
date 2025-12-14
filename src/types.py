from dataclasses import dataclass
from typing import Union, Literal

# Define Condition and Path types
@dataclass(frozen=True)
class BooleanCondition:
    feature: str
    value: bool
@dataclass(frozen=True)
class ThresholdCondition:
    feature: str
    op: Literal["<=", ">"]
    threshold: float
Condition = Union[BooleanCondition, ThresholdCondition]
Path = list[Condition]
