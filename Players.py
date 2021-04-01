import Pieces


class Player:
    """player of Janggi game"""

    def __init__(self, color):
        self._color = color
        self._player_pieces = [Pieces.General(color), Pieces.Guard(color), Pieces.Guard(color),
                               Pieces.Horse(color), Pieces.Horse(color), Pieces.Elephant(color),
                               Pieces.Elephant(color), Pieces.Chariot(color), Pieces.Chariot(color),
                               Pieces.Cannon(color), Pieces.Cannon(color), Pieces.Soldier(color),
                               Pieces.Soldier(color), Pieces.Soldier(color), Pieces.Soldier(color),
                               Pieces.Soldier(color)]

        if self._color == 'red':  # (row, col)
            self._initial_placements = [(1, 4), (0, 3), (0, 5), (0, 2), (0, 7), (0, 1), (0, 6), (0, 0),
                                        (0, 8), (2, 1), (2, 7), (3, 0), (3, 2), (3, 4), (3, 6), (3, 8)]
        else:
            self._initial_placements = [(8, 4), (9, 3), (9, 5), (9, 2), (9, 7), (9, 1), (9, 6), (9, 0),
                                        (9, 8), (7, 1), (7, 7), (6, 0), (6, 2), (6, 4), (6, 6), (6, 8)]

        # if self._color == 'red':  # (row, col)
        #     self._initial_placements = [(4, 1), (3, 0), (5, 0), (2, 0), (7, 0), (1, 0), (6, 0), (0, 0),
        #                                 (8, 0), (1, 2), (7, 2), (0, 3), (2, 3), (4, 3), (6, 3), (8, 3)]
        # else:
        #     self._initial_placements = [(4, 8), (3, 9), (5, 9), (2, 9), (7, 9), (1, 9), (6, 9), (0, 9),
        #                                 (8, 9), (1, 7), (7, 7), (0, 6), (2, 6), (4, 6), (6, 6), (8, 6)]

    def get_player_pieces(self):
        return self._player_pieces

    def get_initial_placements(self):
        return self._initial_placements
