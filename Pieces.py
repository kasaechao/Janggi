import pygame, os, sys


class Piece:
    """Parent class for each game piece"""

    def __init__(self, color):
        self._name = None
        self._location = None
        self._color = color
        self._state = 'active'
        self._image = None

    def get_image(self):
        size = (50, 50)
        self._image = pygame.transform.scale(self._image, size)
        return self._image

    def __repr__(self):
        """override how the object is displayed on the board for testing purposes"""
        piece = self._color[0] + '.' + self._name[0:2]
        return piece

    def get_location(self):
        return self._location

    def get_color(self):
        return self._color

    def get_state(self):
        return self._state

    def set_state(self, state):
        self._state = state
        return self._state

    def set_location(self, location):
        self._location = location
        return self._location


class General(Piece):
    """game piece"""

    def __init__(self, color):
        super().__init__(color)
        if self._color == 'red':
            self._image = pygame.image.load(os.path.join('images/red_general.png'))
        else:
            self._image = pygame.image.load(os.path.join('images/blue_general.png'))
        self._name = 'general'

    def is_valid_move(self, curr, dest, board):
        row_1 = curr[0]
        row_2 = dest[0]
        col_1 = curr[1]
        col_2 = dest[1]
        row_diff = abs(row_2 - row_1)
        col_diff = abs(col_2 - col_1)

        if self._color == 'red':
            # movement is only one space away and does not move out of the palace
            if (row_diff > 1 or col_diff > 1) or board.is_in_palace_red(dest) is False:
                return False
        if self._color == 'blue':
            # movement is only one space away and does not move out of the palace
            if (row_diff > 1 or col_diff > 1) or board.is_in_palace_blue(dest) is False:
                return False
        return True


class Guard(Piece):
    """game piece"""

    def __init__(self, color):
        super().__init__(color)
        if self._color == 'red':
            self._image = pygame.image.load(os.path.join('images/red_guard.png'))
        else:
            self._image = pygame.image.load(os.path.join('images/blue_guard.png'))
        self._name = 'guard'

    def is_valid_move(self, curr, dest, board):
        row_1 = curr[0]
        row_2 = dest[0]
        col_1 = curr[1]
        col_2 = dest[1]
        row_diff = abs(row_2 - row_1)
        col_diff = abs(col_2 - col_1)

        if self._color == 'red':
            # movement is only one space away and does not move out of the palace
            if (row_diff > 1 or col_diff > 1) or board.is_in_palace_red(dest) is False:
                return False
        if self._color == 'blue':
            # movement is only one space away and does not move out of the palace
            if (row_diff > 1 or col_diff > 1) or board.is_in_palace_blue(dest) is False:
                return False
        return True


class Horse(Piece):
    """game piece"""

    def __init__(self, color):
        super().__init__(color)
        if self._color == 'red':
            self._image = pygame.image.load(os.path.join('images/red_horse.png'))
        else:
            self._image = pygame.image.load(os.path.join('images/blue_horse.png'))
        self._name = 'horse'

    def is_valid_move(self, curr, dest, board):
        row_1 = curr[0]
        col_1 = curr[1]
        row_2 = dest[0]
        col_2 = dest[1]
        board = board.get_board()

        if (row_2 - row_1) == -2:   # north movement
            if (col_2 - col_1) == -1 or (col_2 - col_1) == 1:
                if board[row_1 - 1][col_1] == '  ':
                    return True
        if (row_2 - row_1) == 2:   # South movement
            if (col_2 - col_1) == -1 or (col_2 - col_1) == 1:
                if board[row_1 + 1][col_1] == '  ':
                    return True
        if (col_2 - col_1) == 2:   # East movement
            if (row_2 - row_1) == -1 or (row_2 - row_1) == 1:
                if board[row_1][col_1 + 1] == '  ':
                    return True
        if (col_2 - col_1) == -2:   # East movement
            if (row_2 - row_1) == -1 or (row_2 - row_1) == 1:
                if board[row_1][col_1 - 1] == '  ':
                    return True
        return False


class Elephant(Piece):
    """game piece"""

    def __init__(self, color):
        super().__init__(color)
        if self._color == 'red':
            self._image = pygame.image.load(os.path.join('images/red_elephant.png'))
        else:
            self._image = pygame.image.load(os.path.join('images/blue_elephant.png'))
        self._name = 'elephant'

    def is_valid_move(self, curr, dest, board):
        row_1 = curr[0]
        col_1 = curr[1]
        row_2 = dest[0]
        col_2 = dest[1]
        board = board.get_board()

        if (row_2 - row_1) == -3:   # north movement
            if (col_2 - col_1) == -2 or (col_2 - col_1) == 2:
                if board[row_1 - 1][col_1] == '  ':
                    return True
        if (row_2 - row_1) == 3:   # South movement
            if (col_2 - col_1) == -2 or (col_2 - col_1) == 2:
                if board[row_1 + 1][col_1] == '  ':
                    return True
        if (col_2 - col_1) == 3:   # East movement
            if (row_2 - row_1) == -2 or (row_2 - row_1) == 2:
                if board[row_1][col_1 + 1] == '  ':
                    return True
        if (col_2 - col_1) == -3:   # East movement
            if (row_2 - row_1) == -2 or (row_2 - row_1) == 2:
                if board[row_1][col_1 - 1] == '  ':
                    return True
        return False


class Chariot(Piece):
    """game piece"""

    def __init__(self, color):
        super().__init__(color)
        if self._color == 'red':
            self._image = pygame.image.load(os.path.join('images/red_chariot.png'))
        else:
            self._image = pygame.image.load(os.path.join('images/blue_chariot.png'))
        self._name = 'chariot'

    def is_valid_move(self, curr, dest, board):
        row_1 = curr[0]
        col_1 = curr[1]
        row_2 = dest[0]
        col_2 = dest[1]
        row_diff = row_2 - row_1
        col_diff = col_2 - col_1
        game_board = board.get_board()
        not_blocked = True

        if abs(row_diff) > 0 and abs(col_diff) > 0:
            if self._color == 'red':
                if board.is_in_palace_corners(curr) is False or board.is_in_palace_red(dest) is False:
                    return False
            if self._color == 'blue':
                if board.is_in_palace_corners(curr) is False or board.is_in_palace_blue(dest) is False:
                    return False

        if row_diff == 0:   # move right
            node = col_1 + 1
            while node < col_2:
                if game_board[row_1][node] != '  ':
                    not_blocked = False
                node += 1

        if row_diff == 0:   # move left
            node = col_1 - 1
            while node > col_2:
                if game_board[row_1][node] != '  ':
                    not_blocked = False
                node -= 1

        if col_diff == 0:   # move up
            node = row_1 - 1
            while node > row_2:
                if game_board[node][col_1] != '  ':
                    not_blocked = False
                node -= 1

        if col_diff == 0:   # move down
            node = row_1 + 1
            while node < row_2:
                if game_board[node][col_1] != '  ':
                    not_blocked = False
                node += 1

        return not_blocked


class Cannon(Piece):
    """game piece"""

    def __init__(self, color):
        super().__init__(color)
        if self._color == 'red':
            self._image = pygame.image.load(os.path.join('images/red_cannon.png'))
        else:
            self._image = pygame.image.load(os.path.join('images/blue_cannon.png'))
        self._name = 'cannon'

    def is_valid_move(self, curr, dest, board):
        row_1 = curr[0]
        col_1 = curr[1]
        row_2 = dest[0]
        col_2 = dest[1]
        row_diff = row_2 - row_1
        col_diff = col_2 - col_1
        game_board = board.get_board()
        screen_piece = 0
        valid_screen = True

        if abs(row_diff) > 0 and abs(col_diff) > 0:
            if self._color == 'red':
                if board.is_in_palace_corners(curr) is False or board.is_in_palace_red(dest) is False:
                    return False
            if self._color == 'blue':
                if board.is_in_palace_corners(curr) is False or board.is_in_palace_blue(dest) is False:
                    return False

        # up movement with screen piece
        if row_1 > row_2 and col_diff == 0:
            node = row_1 - 1
            while node > row_2:
                if game_board[node][col_1] != '  ':
                    if game_board[node][col_1]._name != 'cannon':
                        screen_piece += 1
                    else:
                        valid_screen = False
                        break
                node -= 1
            if screen_piece != 1:
                valid_screen = False

        if row_1 < row_2 and col_diff == 0:
            node = row_1 + 1
            while node < row_2:
                if game_board[node][col_1] != '  ':
                    if game_board[node][col_1]._name != 'cannon':
                        screen_piece += 1
                    else:
                        valid_screen = False
                        break
                node += 1
            if screen_piece != 1:
                valid_screen = False

        # right movement w/ screen piece
        if col_1 < col_2 and row_diff == 0:
            node = col_1 + 1
            while node < col_2:
                if game_board[row_1][node] != '  ':
                    if game_board[row_1][node]._name != 'cannon':
                        screen_piece += 1
                    else:
                        valid_screen = False
                        break
                node += 1
            if screen_piece != 1:
                valid_screen = False

        # left move w/ screen piece
        if col_1 > col_2 and row_diff == 0:
            node = col_1 - 1
            while node > col_2:
                if game_board[row_1][node] != '  ':
                    if game_board[row_1][node]._name != 'cannon':
                        screen_piece += 1
                    else:
                        valid_screen = False
                        break
                node -= 1
            if screen_piece != 1:
                valid_screen = False

        return valid_screen


class Soldier(Piece):
    """game piece"""

    def __init__(self, color):
        super().__init__(color)
        if self._color == 'red':
            self._image = pygame.image.load(os.path.join('images/red_soldier.png'))
        else:
            self._image = pygame.image.load(os.path.join('images/blue_soldier.png'))
        self._name = 'soldier'

    def is_valid_move(self, curr, dest, board):
        row_1 = curr[0]
        row_2 = dest[0]
        col_1 = curr[1]
        col_2 = dest[1]
        row_diff = abs(row_2 - row_1)
        col_diff = abs(col_2 - col_1)
        if self._color == 'red':
            # check that movement is not outside of the board
            if board.is_in_board(dest) is False:
                return False
            # forward movement
            if row_2 < row_1:
                return False
            # diagonal movement if only in the palace
            if row_2 != row_1 and col_2 != col_1:
                if board.is_in_palace_blue(curr) is False or board.is_in_palace_blue(dest) is False:
                    return False
            # check that movement in only +1
            if row_diff > 1 or col_diff > 1:
                return False

        if self._color == 'blue':
            # check that movement is not outside of the board
            if board.is_in_board(dest) is False:
                return False
            # forward movement
            if row_2 > row_1:
                return False
            # diagonal movement if only in the palace
            if row_2 != row_1 and col_2 != col_1:
                if board.is_in_palace_red(curr) is False or board.is_in_palace_red(dest) is False:
                    return False
            # check that movement in only +1
            if row_diff > 1 or col_diff > 1:
                return False
        return True

