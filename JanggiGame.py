from Player import Player
from Board import Board


class JanggiGame:
    """
    main class to play Janggi
    """

    def __init__(self):
        """initial state of the game when a new game is created."""
        self._game_state = "UNFINISHED"
        self._red_player = Player('red')
        self._blue_player = Player('blue')
        self._in_check = None
        self._board = Board()
        self._turn = 'blue'

        # Setup the board
        red_pieces = self._red_player.get_pieces()
        blue_pieces = self._blue_player.get_pieces()
        for piece in red_pieces:
            coord = self.convert_coord(red_pieces[piece]['initial_location'])
            self._board.set_board(coord, red_pieces[piece]['name'])
        for piece in blue_pieces:
            coord = self.convert_coord(blue_pieces[piece]['initial_location'])
            self._board.set_board(coord, blue_pieces[piece]['name'])

    # ***************** UTILITY FUNCTION TO CONVERT COORDINATE TO LIST INDICES ************************
    @staticmethod
    def convert_coord(coord: str) -> tuple:
        """convert the requested move to valid board indices"""
        key = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
        row = int(coord[1:]) - 1
        for index in range(len(key)):
            if coord[0] == key[index]:
                col = index
                return col, row
        return None, None

    # ***************** GET METHODS FOR THE PRIMARY DATA MEMBERS IN THE INIT FUNCTION *****************
    def get_game_state(self):
        """get current game state"""
        return self._game_state

    def is_in_check(self):
        """get player in check"""
        return self._in_check

    def get_board(self):
        """get the current board"""
        return self._board

    def get_red_player(self):
        """get player private data member"""
        return self._red_player

    def get_blue_player(self):
        """get player private data member"""
        return self._blue_player

    def toggle_turn(self):
        if self._turn == 'red':
            self._turn = 'blue'
        else:
            self._turn = 'red'

    def make_move(self, curr, dest):
        """makes a valid move"""
        board = self._board
        curr = self.convert_coord(curr)
        dest = self.convert_coord(dest)
        piece = board.get_board()[curr[1]][curr[0]]

        # check if player passes
        if curr == dest:
            self.toggle_turn()
            return True

        # no piece exists to move
        if piece == '__':
            return False
        if piece.get_color() != self._turn:
            return False
        # if move is invalid
        if not piece.is_valid_move(board, curr, dest):
            return False
        board.set_board(curr, '__')
        captured_piece = board.get_board()[dest[1]][dest[0]]
        if captured_piece != '__':
            captured_piece.set_state()
        board.set_board(dest, piece)

        self.toggle_turn()
        return True


def main():
    game = JanggiGame()
    game.get_board().print_board()
    move = game.make_move('h10', 'i9')
    print(move)
    game.get_board().print_board()


if __name__ == '__main__':
    main()

