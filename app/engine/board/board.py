from squares.square import Square
from pieces.piece import (
        Piece, 
        Pawn,
        Bishop,
        Knight,
        Rook,
        Queen,
        King,
    )



"""
Accessing each piece is :

    board[rank_index][file_index].piece.movement
                               (Square).(Piece)

"""


class Board:

    def __init__(self):
        """
        Define a complete fresh board
        """
        self.__set_board()
        self.__set_pawns()
        self.__set_knights()
        self.__set_rooks()
        self.__set_bishops()
        self.__set_queen()
        self.__set_king()

    def __set_board(self) -> None:
        """
        Setting the Board

        the structure is :
        [rank_index][file_index] : Square

        :param None
        :return None
        """
        board = []

        for rank_index in range(8):
            files = [] 

            if rank_index % 2 == 0 : #if the index is even the first square of the file is blask
                for file_index in range(8):
                    if file_index % 2 == 0 :
                        files.append(
                                Square(rank_index, file_index, 'black')
                        )
                    else :
                        files.append(
                                Square(rank_index, file_index, 'white')
                        )
            else : #if the index is odd the first square of the file is white
                for file_index in range(8):
                    if file_index % 2 == 0 :
                        files.append(
                                Square(rank_index, file_index, 'white')
                        )
                    else :
                        files.append(
                                Square(rank_index, file_index, 'black')
                        )

            board.append(files)

        self.board = board

    def __set_pawns(self) -> None:
        """
        Setting the pawns on the board

        :param None
        :return None
        """

        """ white pawns """
        white_pawn = Pawn('pawn', 'white')
        rank_index = 1
        for file_index in range(8):
            self.board[rank_index][file_index].piece = white_pawn

        """ black pawns """
        black_pawn = Pawn('pawn', 'black')
        rank_index = 6
        for file_index in range(8):
            self.board[rank_index][file_index].piece = black_pawn

    def __set_knights(self) -> None:
        """
        Setting the knights on the board

        :param None
        :return None
        """

        """ white knights """
        white_knight = Knight('knight', 'white')
        rank_index = 0
        for file_index in [1, 6]:
            self.board[rank_index][file_index].piece = white_knight

        """ black knights """
        black_knight = Knight('knight', 'black')
        rank_index = 7
        for file_index in [1, 6]:
            self.board[rank_index][file_index].piece = black_knight

    def __set_rooks(self) -> None:
        """
        Setting the rooks on the board

        :param None
        :return None
        """

        """ white rooks """
        white_rook = Rook('rook', 'white')
        rank_index = 0
        for file_index in [0, 7]:
            self.board[rank_index][file_index].piece = white_rook

        """ black rooks """
        black_rook = Rook('rook', 'black')
        rank_index = 7
        for file_index in [0, 7]:
            self.board[rank_index][file_index].piece = black_rook

    def __set_bishops(self) -> None:
        """
        Setting the bishops on the board

        :param None
        :return None
        """

        """ white bishops """
        white_bishop = Bishop('bishop', 'white')
        rank_index = 0
        for file_index in [2, 5]:
            self.board[rank_index][file_index].piece = white_bishop

        """ black bishops """
        black_bishop = Bishop('bishop', 'bishop')
        rank_index = 7
        for file_index in [2, 5]:
            self.board[rank_index][file_index].piece = black_bishop

    def __set_queen(self) -> None:
        """
        Setting the queen on the board

        :param None
        :return None
        """

        """ white queen """
        white_queen = Queen('queen', 'white')
        rank_index = 0
        file_index = 3
        self.board[rank_index][file_index].piece = white_queen

        """ black queen """
        black_queen = Queen('queen', 'black')
        rank_index = 7
        file_index = 3
        self.board[rank_index][file_index].piece = black_queen

    def __set_king(self) -> None:
        """
        Setting the king on the board

        :param None
        :return None
        """

        """ white king """
        white_king = King('king', 'white')
        rank_index = 0
        file_index = 4
        self.board[rank_index][file_index].piece = white_king

        """ black king """
        black_king = King('king', 'black')
        rank_index = 7
        file_index = 4
        self.board[rank_index][file_index].piece = black_king

    def get(self) -> list :
        """
        Returns the board
        
        :return board Type[list]
        """
        return self.board

b = Board().get()

#for rank in b :
    #print(rank, '\n \n')

#print(b[0][2].color)

def test(board, piece, current, next) :
    rank_index, file_index = current[0], current[1]
    next_rank, next_file = next[0], next[1]
    piece = board[rank_index][file_index].piece
    board[rank_index][file_index].piece = None
    board[next_rank][next_file].piece = piece

    return board

move = {
        'piece': 'pawn',
        'current': [1, 0],
        'next': [3, 0],
    }

b = test(b, **move)
for rank in b :
    print(rank, '\n \n')
