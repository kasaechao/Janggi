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
                "General": {"name": General(color), "color": color, "current_location": '', "initial_location": 'e2'},
                "Guard1": {"name": Guard(color), "color": color, "current_location": '', "initial_location": 'd1'},
                "Guard2": {"name": Guard(color), "color": color, "current_location": '', "initial_location": 'f1'},
                "Horse1": {"name": Horse(color), "color": color, "current_location": '', "initial_location": 'c1'},
                "Horse2": {"name": Horse(color), "color": color, "current_location": '', "initial_location": 'h1'},
                "Elephant1": {"name": Elephant(color), "color": color, "current_location": '', "initial_location": 'b1'},
                "Elephant2": {"name": Elephant(color), "color": color, "current_location": '', "initial_location": 'g1'},
                "Chariot1": {"name": Chariot(color), "color": color, "current_location": '', "initial_location": 'a1'},
                "Chariot2": {"name": Chariot(color), "color": color, "current_location": '', "initial_location": 'i1'},
                "Cannon1": {"name": Cannon(color), "color": color, "current_location": '', "initial_location": 'b3'},
                "Cannon2": {"name": Cannon(color), "color": color, "current_location": '', "initial_location": 'h3'},
                "Soldier1": {"name": Soldier(color), "color": color, "current_location": '', "initial_location": 'a4'},
                "Soldier2": {"name": Soldier(color), "color": color, "current_location": '', "initial_location": 'c4'},
                "Soldier3": {"name": Soldier(color), "color": color, "current_location": '', "initial_location": 'e4'},
                "Soldier4": {"name": Soldier(color), "color": color, "current_location": '', "initial_location": 'g4'},
                "Soldier5": {"name": Soldier(color), "color": color, "current_location": '', "initial_location": 'i4'}
            }
        else:
            self._pieces = {
                "General": {"name": General(color), "color": color, "current_location": '', "initial_location": 'e9'},
                "Guard1": {"name": Guard(color), "color": color, "current_location": '', "initial_location": 'd10'},
                "Guard2": {"name": Guard(color), "color": color, "current_location": '', "initial_location": 'f10'},
                "Horse1": {"name": Horse(color), "color": color, "current_location": '', "initial_location": 'c10'},
                "Horse2": {"name": Horse(color), "color": color, "current_location": '', "initial_location": 'h10'},
                "Elephant1": {"name": Elephant(color), "color": color, "current_location": '', "initial_location": 'b10'},
                "Elephant2": {"name": Elephant(color), "color": color, "current_location": '', "initial_location": 'g10'},
                "Chariot1": {"name": Chariot(color), "color": color, "current_location": '', "initial_location": 'a10'},
                "Chariot2": {"name": Chariot(color), "color": color, "current_location": '', "initial_location": 'i10'},
                "Cannon1": {"name": Cannon(color), "color": color, "current_location": '', "initial_location": 'b8'},
                "Cannon2": {"name": Cannon(color), "color": color, "current_location": '', "initial_location": 'h8'},
                "Soldier1": {"name": Soldier(color), "color": color, "current_location": '', "initial_location": 'a7'},
                "Soldier2": {"name": Soldier(color), "color": color, "current_location": '', "initial_location": 'c7'},
                "Soldier3": {"name": Soldier(color), "color": color, "current_location": '', "initial_location": 'e7'},
                "Soldier4": {"name": Soldier(color), "color": color, "current_location": '', "initial_location": 'g7'},
                "Soldier5": {"name": Soldier(color), "color": color, "current_location": '', "initial_location": 'i7'}
        }
        for piece in self._pieces:
            location = self._pieces[piece]['initial_location']
            self._pieces[piece]['name'].set_current_location(location)

    def get_color(self):
        """get method for self._color"""
        return self._color

    def get_pieces(self):
        """returns the player's pieces"""
        return self._pieces


