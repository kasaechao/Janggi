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
            red_pieces[piece]['name'].set_current_location(coord)
            red_pieces[piece]['name'].set_image_file('red' + '_' + red_pieces[piece]['name'].get_name().lower() + '.svg')
        for piece in blue_pieces:
            coord = self.convert_coord(blue_pieces[piece]['initial_location'])
            self._board.set_board(coord, blue_pieces[piece]['name'])
            blue_pieces[piece]['name'].set_current_location(coord)
            blue_pieces[piece]['name'].set_image_file('blue' + '_' + blue_pieces[piece]['name'].get_name().lower()  + '.svg')


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

    def get_turn(self):
        """get the current turn"""
        return self._turn

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

    def is_in_check(self, player):
        """get player in check"""
        if player == 'red':     # get the color general we need, and opposing player pieces
            gen = self._red_player.get_pieces()['General']['name']
            gen_coord = gen.get_current_location()
            for i in self._blue_player.get_pieces():
                piece = self._blue_player.get_pieces()[i]['name']
                piece_loc = piece.get_current_location()
                if piece.get_state() is True:
                    if piece.is_valid_move(self._board, piece_loc, gen_coord):
                        self._in_check = 'red'
                        return True

        elif player == 'blue':
            gen = self._blue_player.get_pieces()['General']['name']
            gen_coord = gen.get_current_location()
            for i in self._red_player.get_pieces():
                piece = self._red_player.get_pieces()[i]['name']
                piece_loc = piece.get_current_location()
                if piece.get_state() is True:
                    if piece.is_valid_move(self._board, piece_loc, gen_coord):
                        self._in_check = 'blue'
                        return True
        return False

    def is_checkmate(self) -> bool:
        """return checkmate event"""
        # check if gen can escape check
        if self._in_check == 'red':
            red_gen = self._red_player.get_pieces()['General']['name']
            red_gen_coord = self._red_player.get_pieces()['General']['name'].get_current_location()
            for coord in self._board.red_palace():
                if red_gen.is_valid_move(red_gen_coord, coord):
                    for piece in self._blue_player.get_pieces():
                        piece_coord = self._blue_player.get_pieces()[piece]['name'].get_current_location()
                        if not self._blue_player.get_pieces()[piece]['name'].is_valid_move(piece_coord, coord):
                            return True

        elif self._in_check == 'blue':
            blue_gen = self._blue_player.get_pieces()['General']['name']
            blue_gen_coord = self._blue_player.get_pieces()['General']['name'].get_current_location()
            for coord in self._board.blue_palace():
                if blue_gen.is_valid_move(blue_gen_coord, coord):
                    for piece in self._red_player.get_pieces():
                        piece_coord = self._red_player.get_pieces()[piece]['name'].get_current_location()
                        if not self._red_player.get_pieces()[piece]['name'].is_valid_move(piece_coord, coord):
                            return True

        return False

    def make_move(self, curr, dest):
        """makes a valid move"""
        board = self._board
        curr = self.convert_coord(curr)
        dest = self.convert_coord(dest)
        piece = board.get_board()[curr[1]][curr[0]]

        # # check for checkmate
        # if self.is_checkmate():
        #     return False

        # check game state
        if self.get_game_state() != 'UNFINISHED':
            print('game over')
            return False

        # check if player passes, and not in check
        if curr == dest and not self.is_in_check(self._turn):
            self.toggle_turn()
            return True

        # no piece exists to move
        if piece == '__':
            print('no piece to move')
            return False
        if piece.get_color() != self._turn:
            return False
        # if move is invalid
        if not piece.is_valid_move(board, curr, dest):
            print('invalid move')
            return False
        # complete the move
        board.set_board(curr, '__')
        captured_piece = board.get_board()[dest[1]][dest[0]]
        if captured_piece != '__':
            captured_piece.set_state()
        board.set_board(dest, piece)
        piece.set_current_location(dest)

        # check if player is in check, then the move was invalid, and undo the moves
        if self.is_in_check(self._turn):
            if captured_piece != '__':
                captured_piece.set_state()
            board.set_board(dest, captured_piece)
            board.set_board(curr, piece)
            piece.set_current_location(curr)
            print('move does not remove check')
            return False

        # toggle turn if move is valid
        if self._turn == self._in_check:
            self._in_check = None

        self.toggle_turn()
        return True


def main():
    g = JanggiGame()
    while g.get_game_state() == 'UNFINISHED':
        valid_move = False
        if g.get_turn() == 'blue':
            while not valid_move:
                g.get_board().print_board()
                print('blue''s turn to make a move.')
                curr = input('from: ')
                dest = input("destination: ")
                valid_move = g.make_move(curr, dest)
                if not valid_move:
                    print('move invalid, please make a valid move...')
        else:
            while not valid_move:
                g.get_board().print_board()
                print('red''s turn to make a move.')
                curr = input('from: ')
                dest = input("destination: ")
                valid_move = g.make_move(curr, dest)
                if not valid_move:
                    print('move invalid, please make a valid move...')


if __name__ == '__main__':
    main()
