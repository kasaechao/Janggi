class Piece:
    """Parent class for creating pieces"""

    def __init__(self, color):
        self._initial_location = None
        self._current_location = None
        self._color = color
        self._state = True   # True = alive, False= dead
        self._image_file = None
        self._image, self._rect = None, None

    # ***************** GET METHODS FOR THE DATA MEMBERS IN THE CONSTRUCTOR FUNCTION *****************
    def get_image_file(self):
        return self._image

    def set_image_file(self, name):
        self._image = name

    def get_image(self):
        return self._image, self._rect

    def set_image(self, image):
        self._image, self._rect = image

    def get_initial_location(self):
        """get method for private data member"""
        return self._initial_location

    def get_current_location(self):
        """get method for private data member"""
        return self._current_location

    def get_color(self):
        """get method for private data member"""
        return self._color

    def get_state(self):
        """get method for private data member"""
        return self._state

    # ***************** SET METHODS FOR THE DATA MEMBERS IN THE CONSTRUCTOR FUNCTION *****************

    def set_initial_location(self, location):
        """get method for private data member"""
        self._initial_location = location
        return self._initial_location

    def set_current_location(self, location):
        """get method for private data member"""
        self._current_location = location
        return self._current_location

    def set_color(self, color):
        """get method for private data member"""
        self._color = color
        return self._color

    def set_state(self):
        """set piece to dead state"""
        self._state = not self._state

