from dataclasses import dataclass

@dataclass
class Piece:
    name: str 
    color: str

@dataclass
class Pawn(Piece):
    movement = 'pawn movement'

@dataclass
class Bishop(Piece):
    movement = 'bishop movement'

@dataclass
class Knight(Piece):
    movement = 'knight movement'

@dataclass
class Rook(Piece):
    movement = 'rook movement'

@dataclass
class Queen(Piece):
    movement = 'queen movement'

@dataclass
class King(Piece):
    movement = 'king movement'

EACH_PIECE = [
    'pawn',
    'bishop',
    'knight',
    'rook',
    'queen',
    'king',
]
