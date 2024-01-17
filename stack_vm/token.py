from enum import Enum, auto
from dataclasses import dataclass


class Tokens(Enum):
    Integer = auto()
    Float = auto()
    Identifier = auto()
    Plus = auto()
    Minus = auto()
    Equal = auto()
    EOL = auto()
    EOF = auto()
    Illegal = auto()
    Slash = auto()
    Star = auto()
    Dot = auto()

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}.{self._name_}"


@dataclass(frozen=True, slots=True)
class Token:
    type: Tokens
    value: str | int | float
