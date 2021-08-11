from General import General
from Guard import Guard
from Horse import Horse
from Elephant import Elephant
from Chariot import Chariot
from Cannon import Cannon
from Soldier import Soldier

class Player:
    """Creates players for Janggi game"""

    def __init__(self, color):
        self._color = color
        if color == 'red':
            self._pieces = {
                {"general": General(color), "color": color, "current_location": '', "initial_location": 'e2'},
                {"general": Guard(color), "color": color, "current_location": '', "initial_location": 'd1'},
                {"general": Guard(color), "color": color, "current_location": '', "initial_location": 'f1'},
                {"general": Horse(color), "color": color, "current_location": '', "initial_location": 'c1'},
                {"general": Horse(color), "color": color, "current_location": '', "initial_location": 'h1'},
                {"general": Elephant(color), "color": color, "current_location": '', "initial_location": 'b1'},
                {"general": Elephant(color), "color": color, "current_location": '', "initial_location": 'g1'},
                {"general": Chariot(color), "color": color, "current_location": '', "initial_location": 'a1'},
                {"general": Chariot(color), "color": color, "current_location": '', "initial_location": 'i1'},
                {"general": Cannon(color), "color": color, "current_location": '', "initial_location": 'b3'},
                {"general": Cannon(color), "color": color, "current_location": '', "initial_location": 'h3'},
                {"general": Soldier(color), "color": color, "current_location": '', "initial_location": 'a4'},
                {"general": Soldier(color), "color": color, "current_location": '', "initial_location": 'c4'},
                {"general": Soldier(color), "color": color, "current_location": '', "initial_location": 'e4'},
                {"general": Soldier(color), "color": color, "current_location": '', "initial_location": 'g4'},
                {"general": Soldier(color), "color": color, "current_location": '', "initial_location": 'i4'}
            }
        else:
            self._pieces = {
                {"general": General(color), "color": color, "current_location": '', "initial_location": 'e9'},
                {"general": Guard(color), "color": color, "current_location": '', "initial_location": 'd10'},
                {"general": Guard(color), "color": color, "current_location": '', "initial_location": 'f10'},
                {"general": Horse(color), "color": color, "current_location": '', "initial_location": 'c10'},
                {"general": Horse(color), "color": color, "current_location": '', "initial_location": 'h10'},
                {"general": Elephant(color), "color": color, "current_location": '', "initial_location": 'b10'},
                {"general": Elephant(color), "color": color, "current_location": '', "initial_location": 'g10'},
                {"general": Chariot(color), "color": color, "current_location": '', "initial_location": 'a10'},
                {"general": Chariot(color), "color": color, "current_location": '', "initial_location": 'i10'},
                {"general": Cannon(color), "color": color, "current_location": '', "initial_location": 'b8'},
                {"general": Cannon(color), "color": color, "current_location": '', "initial_location": 'h8'},
                {"general": Soldier(color), "color": color, "current_location": '', "initial_location": 'a7'},
                {"general": Soldier(color), "color": color, "current_location": '', "initial_location": 'c7'},
                {"general": Soldier(color), "color": color, "current_location": '', "initial_location": 'e7'},
                {"general": Soldier(color), "color": color, "current_location": '', "initial_location": 'g7'},
                {"general": Soldier(color), "color": color, "current_location": '', "initial_location": 'i7'}
            }

    def get_color(self):
        """get method for self._color"""
        return self._color

    def get_pieces(self):
        """returns the player's pieces"""
        return self._pieces
