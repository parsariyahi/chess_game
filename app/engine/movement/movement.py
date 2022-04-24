from .. import Board

class Movement:

    def __init__(self) :
        pass

    def move(self, board: list, piece: str, current_location: list, next_location: list) -> list :
        """
        The main function  of each move

        :param
            board type[Board]
            piece type[str] 
            current_location type[list] example: [rank_index, file_index]
            next_location type[list] example: [rank_index, file_index]

        :retrun
            board type[Board]
        """

        # convert locations to more readable form
        rank_index, file_index = current_location[0], current_location[1]
        next_rank, next_file = next_location[0], next_location[1]

        # move piece to new location and put 'None' in previous
        piece = board[rank_index][file_index].piece
        board[rank_index][file_index].piece = None
        board[next_rank][next_file].piece = piece

        return board

#TODO break move function to little parts
    def __find_piece(self, board, piece):
        pass

    def __clear_square(self, square):
        pass

    def __move_piece_to_square(self, board, piece):
        pass

# input example for Movement.move()
move = {
        'piece': 'pawn',
        'current': [1, 0],
        'next': [3, 0],
    }
