from dataclasses import dataclass

#TODO 
#import the Piece object here,
#turn this app in to a package and install it 
from typing import Any

@dataclass
class Square:

    rank_index: int
    file_index: int
    color: str

    piece: Any = None
