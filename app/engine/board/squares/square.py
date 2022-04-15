from dataclasses import dataclass
from typing import Any

@dataclass
class Square:

    rank_index: int
    file_index: int
    color: str

    piece: Any