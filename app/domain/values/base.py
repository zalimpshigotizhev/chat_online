from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Generic, TypeVar, Any

VT = TypeVar("VT", bound=Any)


@dataclass(frozen=True) # Изучить moment И пересмотреть
class BaseValueObject(ABC, Generic[VT]):
    value: VT

    def __post_init__(self):
        self.validate()

    @abstractmethod
    def validate(self):
        pass

    @abstractmethod
    def as_generic_type(self):
        pass