import Board
import Players


class JanggiGame:
    """A game of janggi"""

    def __init__(self):
        self._board = Board.Board()
        self._red_player = Players.Player('red')
        self._blue_player = Players.Player('blue')
        self._game_over = False
        self._player_in_check = None
        self._turn = 'blue'
        self._captured_pieces = []
        self._move_log = []

        for i, piece in enumerate(self._red_player.get_player_pieces()):
            self._board.set_board(self._red_player.get_initial_placements()[i], piece)
            piece.set_location(self._red_player.get_initial_placements()[i])
        for i, piece in enumerate(self._blue_player.get_player_pieces()):
            self._board.set_board(self._blue_player.get_initial_placements()[i], piece)
            piece.set_location(self._blue_player.get_initial_placements()[i])

    def get_board(self):
        return self._board

    def get_red_player(self):
        return self._red_player

    def is_in_check(self, player):
        blue_pieces = self._blue_player.get_player_pieces()
        red_pieces = self._red_player.get_player_pieces()
        blue_gen = blue_pieces[0]
        red_gen = red_pieces[0]
        in_check = False
        i = 0   # counter for looping through a red/blue player pieces

        # if player's general is in danger, change check status
        if player == 'red':
            while i < len(blue_pieces):
                piece = blue_pieces[i]
                if piece != 'inactive':
                    if piece.is_valid_move(piece.get_location(), red_gen.get_location(), self._board):
                        in_check = True
                        i = len(blue_pieces)    # break while loop
                    else:
                        i += 1
            if in_check:
                self._player_in_check = 'red'
                return True
            else:
                return False

        if player == 'blue':
            while i < len(red_pieces):
                piece = red_pieces[i]
                if piece != 'inactive':
                    if piece.is_valid_move(piece.get_location(), blue_gen.get_location(), self._board):
                        in_check = True
                        i = len(blue_pieces)    # break while loop
                    else:
                        i += 1
            if in_check is True:
                return True
            else:
                return False

    def get_blue_player(self):
        return self._blue_player

    def is_game_over(self):
        return self._game_over

    def get_player_in_check(self):
        return self._player_in_check

    def is_checkmate(self, player):
        # check if general can escape
        # check if a piece can block for the general
        pass

    def get_current_turn(self):
        return self._turn

    def convert_to_coord(self, move):
        """convert requested move to coordinates for the 2D array"""
        key = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
        letter_portion = move[0]
        for i in range(len(key)):
            if letter_portion == key[i]:
                letter_portion = i
        remaining = move[1:]
        num_portion = ""
        while len(remaining) > 0:
            num_portion += remaining[0]
            remaining = remaining[1:]
        num_portion = int(num_portion) - 1
        return num_portion, letter_portion

    def make_move(self, curr, dest):
        if type(curr) == str and type(dest) == str:
            self.convert_to_coord(curr)
            self.convert_to_coord(dest)

        piece = self._board.get_board()[curr[0]][curr[1]]
        dest_piece = self._board.get_board()[dest[0]][dest[1]]

        # check current game state
        if self._game_over is True:
            print("game is over")
            return False
        # check that a piece is selected
        if piece == '  ':
            print("No piece present at that location.")
            return False
        # check that piece belongs to the current turn
        if piece.get_color() != self._turn:
            print("piece does not belong to", self._turn)
            return False
        # check that move is valid for the piece
        if piece.is_valid_move(curr, dest, self._board) is False:
            print("The move is not valid for the", piece)
            return False
        # check that destination is not blocked by one's own piece
        if dest_piece != '  ' and curr != dest and dest_piece.get_color() == self._turn:
            print("space is occupied by one's own piece")
            return False

        # if above conditions are met, then make the move
        #   update piece's state is there is a piece to be captured
        temp = dest_piece
        #   modify board locations
        self._board.set_board(curr, '  ')
        self._board.set_board(dest, piece)
        # if making move places player in check, undo the move
        if self.is_in_check(self._turn) is True:
            print("The move places you in check")
            self._board.set_board(curr, piece)
            self._board.set_board(dest, temp)
            return False

        piece.set_location(dest)
        if temp != '  ':
            temp.set_state('inactive')

        if self._turn == 'red':
            self.is_checkmate('blue')
            self.is_in_check('blue')
            if self.is_in_check('blue'):
                self._player_in_check = 'blue'
            self._turn = 'blue'
        else:
            self.is_checkmate('red')
            self.is_in_check('red')
            if self.is_in_check('red'):
                self._player_in_check = 'red'
            self._turn = 'red'

        return True



