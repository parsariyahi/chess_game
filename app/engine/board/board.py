from squares.square import Square
from pieces.piece import Piece, EACH_PIECE

class Board:
    board = [
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
    ]

    def __init__(self):
        self.__set_pawns()
        self.__set_knights()
        self.__set_rooks()
        self.__set_queen()
        self.__set_king()

    def __set_pawns(self) -> None:
        """
        Setting the pawns on the board

        :param None
        :return None
        """
        pawn = Piece()

        """
        white pawns
        """
        rank_index = 1
        for file_index in range(7):
            self.board[rank_index][file_index] = Square(rank_index, file_index, 'white', pawn)

        """
        black pawns
        """
        rank_index = 6
        for file_index in range(7):
            self.board[rank_index][file_index] = Square(rank_index, file_index, 'white', pawn)


    def __set_rooks(self) -> None:
        """
        Setting the rooks on the board

        :param None
        :return None
        """
        rook = Piece()

        """
        white rooks
        """
        rank_index = 0
        for file_index in [0, 7]:
            self.board[rank_index][file_index] = Square(rank_index, file_index, 'white', rook)

        """
        black rooks
        """
        rank_index = 7
        for file_index in [0, 7]:
            self.board[rank_index][file_index] = Square(rank_index, file_index, 'white', rook)


    def __set_knights(self) -> None:
        """
        Setting the knights on the board

        :param None
        :return None
        """
        knight = Piece()

        """
        white knights
        """
        rank_index = 0
        for file_index in [1, 6]:
            self.board[rank_index][file_index] = Square(rank_index, file_index, 'white', knight)

        """
        black knights
        """
        rank_index = 7
        for file_index in [1, 6]:
            self.board[rank_index][file_index] = Square(rank_index, file_index, 'white', knight)


    def __set_bishops(self) -> None:
        """
        Setting the bishops on the board

        :param None
        :return None
        """
        bishop = Piece()

        """
        white bishops
        """
        rank_index = 0
        for file_index in [2, 5]:
            self.board[rank_index][file_index] = Square(rank_index, file_index, 'white', bishop)

        """
        black bishops
        """
        rank_index = 7
        for file_index in [2, 5]:
            self.board[rank_index][file_index] = Square(rank_index, file_index, 'white', bishop)

    def __set_queen(self) -> None:
        """
        Setting the queen on the board

        :param None
        :return None
        """
        queen = Piece()

        """
        white queen
        """
        rank_index = 0
        file_index = 3
        self.board[rank_index][file_index] = Square(rank_index, file_index, 'white', queen)

        """
        black queen
        """
        rank_index = 7
        file_index = 3
        self.board[rank_index][file_index] = Square(rank_index, file_index, 'white', queen)

    def __set_king(self) -> None:
        """
        Setting the king on the board

        :param None
        :return None
        """
        king = Piece()

        """
        white king
        """
        rank_index = 0
        file_index = 4
        self.board[rank_index][file_index] = Square(rank_index, file_index, 'white', king)

        """
        black king
        """
        rank_index = 7
        file_index = 4
        self.board[rank_index][file_index] = Square(rank_index, file_index, 'white', king)

    def get(self) -> list :
        """
        
        :return board Type[list]
        """
        return self.board

# b = Board().get()

# print(b[0][0])