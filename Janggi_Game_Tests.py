import unittest
from JanggiGame import JanggiGame

class TestJanggiGame(unittest.TestCase):
    def setUp(self):
        self.unfinished = 'UNFINISHED'
        self.red_won = 'RED_WON'
        self.blue_won = 'BLUE_WON'
        self.invalid_move = False
        self.valid_move = True

#    @visibility('visible')
    def test_game_can_be_instantiated(self):
        """test that we can create a JanggiGame object"""
        g = JanggiGame()
        self.assertIsInstance(g, JanggiGame)

#    @visibility('visible')
    def test_that_blue_can_start_the_game(self):
        """RULES: Blue can start the game"""
        g = JanggiGame()
        blue_move = g.make_move('c7', 'c6')
        self.assertIs(blue_move, True)

#    @visibility('after_due_date')
    def test_that_red_cannot_start_the_game(self):
        """RULES: Red cannot start the game"""
        g = JanggiGame()
        red_move = g.make_move('c4', 'c5')
        self.assertIs(red_move, False)

#    @visibility('visible')
    def test_passing_the_turn(self):
        """RULES: test that a player can pass the turn"""
        g = JanggiGame()
        g.make_move('a7', 'b7') # first move by Blue
        move_result = g.make_move('a4', 'a4') # passing move by Red
        self.assertIs(move_result, True)
        move_result = g.make_move('b7', 'b7') # passing move by Blue
        self.assertIs(move_result, True)

#    @visibility('after_due_date')
    def test_passing_the_turn_after_capturing(self):
        """RULES: test that a player can pass the turn, a turn after capturing another player's piece"""
        g = JanggiGame()
        g.make_move('a7', 'a6') # first move by Blue
        g.make_move('a4', 'a4') # passing move by Red
        g.make_move('a6', 'a5') # valid move by Blue
        g.make_move('e4', 'e5') # valid move by Red
        g.make_move('a5', 'a4') # capturing move by Blue
        g.make_move('c4', 'c5') # valid move by Red
        passing_move = g.make_move('a4', 'a4')  # passing move by Blue
        self.assertIs(passing_move, True)
        valid_move_after_passing = g.make_move('c5', 'c6')  # valid move by Red
        self.assertIs(valid_move_after_passing, True)

#    @visibility('after_due_date')
    def test_passing_the_turn_after_being_captured(self):
        """RULES: test that a player can pass the turn, after their piece has been captured"""
        g = JanggiGame()
        g.make_move('a7', 'a6')  # first move by Blue
        g.make_move('a4', 'a4')  # passing move by Red
        g.make_move('a6', 'a5')  # valid move by Blue
        g.make_move('e4', 'e5')  # valid move by Red
        g.make_move('a5', 'a4')  # capturing move by Blue
        passing_move = g.make_move('c4', 'c4')  # passing move by Red
        self.assertIs(passing_move, True)
        valid_move_after_passing = g.make_move('a4', 'a3')  # valid move by Blue
        self.assertIs(valid_move_after_passing, True)

#    @visibility('visible')
    def test_valid_forward_move_for_red_soldier(self):
        """SOLDIER: test in the beginning of the game that a red soldier can perform a valid forward move"""
        #take a soldier for red
        g = JanggiGame()
        first_move = g.make_move('c7','c6') #because blue moves first
        red_soldier_forward_move = g.make_move('c4','c5')
        self.assertIs(red_soldier_forward_move, True)

#    @visibility('visible')
    def test_valid_sideway_move_for_red_soldier(self):
        """SOLDIER: test in the beginning of the game that a red soldier can perform a valid sideway move"""
        # take a soldier for red
        g = JanggiGame()
        first_move = g.make_move('c7', 'c6') # because blue moves first
        red_soldier_sideway_move = g.make_move('c4', 'd4')
        self.assertIs(red_soldier_sideway_move, True)

#    @visibility('visible')
    def test_valid_forward_move_for_blue_soldier(self):
        """SOLDIER: test in the beginning of the game that a blue soldier can perform a valid forward move"""
        g = JanggiGame()
        blue_soldier_forward_move = g.make_move('c7', 'c6')  # because blue moves first
        self.assertIs(blue_soldier_forward_move, True)

#    @visibility('visible')
    def test_valid_sideway_move_for_blue_soldier(self):
        """SOLDIER: test in the beginning of the game that a blue soldier can perform a valid sideway move"""
        g = JanggiGame()
        blue_soldier_sideway_move = g.make_move('c7', 'b7')  # because blue moves first
        self.assertIs(blue_soldier_sideway_move, True)

#    @visibility('after_due_date')
    def test_invalid_backward_move_for_blue_soldier(self):
        """SOLDIER: test in the beginning of the game that a blue soldier cannot perform an backward move"""
        g = JanggiGame()
        blue_soldier_backward_move = g.make_move('c7', 'c8')  # try backward move which is illegal
        self.assertIs(blue_soldier_backward_move, False)
        pass

#    @visibility('after_due_date')
    def test_invalid_diagonal_move_for_blue_soldier(self):
        """SOLDIER: test in the beginning of the game that a blue soldier cannot perform an diagonal move"""
        g = JanggiGame()
        blue_soldier_diagonal_move = g.make_move('c7', 'd6')  # try diagonal which is illegal
        self.assertIs(blue_soldier_diagonal_move, False)
        pass

#    @visibility('after_due_date')
    def test_invalid_backward_move_for_red_soldier(self):
        """SOLDIER: test in the beginning of the game that a red soldier cannot perform an backward move"""
        g = JanggiGame()
        g.make_move('c7', 'c6')  # because blue moves first
        red_soldier_backward_move = g.make_move('c4', 'c3')  # try backward move which is illegal
        self.assertIs(red_soldier_backward_move, False)
        pass

#    @visibility('after_due_date')
    def test_invalid_diagonal_move_for_red_soldier(self):
        """SOLDIER: test in the beginning of the game that a red soldier cannot perform an diagonal move"""
        g = JanggiGame()
        g.make_move('c7', 'c6')  # because blue moves first
        red_soldier_backward_move = g.make_move('c4', 'd5')  # try diagonal move which is illegal
        self.assertIs(red_soldier_backward_move, False)

#    @visibility('visible')
    def test_a_soldier_can_capture_a_piece(self):
        """SOLDIER: test that a soldier can capture another piece"""
        g = JanggiGame()
        g.make_move('a7', 'a6') # because blue moves first
        g.make_move('i4', 'i5') # first move by Red
        g.make_move('a6', 'a5') # valid move by Blue
        g.make_move('i5', 'i6') # valid move by Red
        capturing_move = g.make_move('a5', 'a4') # capturing move by Blue
        self.assertIs(capturing_move, True) #move should be succesful

#    @visibility('after_due_date')
    def test_that_a_captured_piece_cannot_be_moved(self):
        """RULES: test that once a piece has been captured, it no longer exists for movement"""
        g = JanggiGame()
        g.make_move('a7', 'a6') # because blue moves first
        g.make_move('i4', 'i5') # first move by Red
        g.make_move('a6', 'a5') # valid move by Blue
        g.make_move('i5', 'i6') # valid move by Red
        capturing_move = g.make_move('a5', 'a4') # capturing move by Blue
        move_on_a_non_existent_piece = g.make_move('a4', 'a5') # move from a location owned by Red
        self.assertIs(move_on_a_non_existent_piece, False)

#    @visibility('after_due_date')
    def test_that_after_a_piece_is_captured_the_game_can_still_continue(self):
        """RULES: test that after a capture, the other player can still move"""
        g = JanggiGame()
        g.make_move('a7', 'a6') # because blue moves first
        g.make_move('i4', 'i5') # first move by Red
        g.make_move('a6', 'a5') # valid move by Blue
        g.make_move('i5', 'i6') # valid move by Red
        capturing_move = g.make_move('a5', 'a4') # capturing move by Blue
        move_on_a_non_existent_piece = g.make_move('a4', 'a5') # move from a location owned by Red
        valid_move_by_red = g.make_move('e4', 'e5') # valid move by Red
        self.assertIs(valid_move_by_red, True)


#    @visibility('visible')
    def test_passing_the_turn(self):
        """RULES: test that a player can pass the turn"""
        g = JanggiGame()
        move_result = g.make_move('a7', 'b7') # first move by Blue
        self.assertIs(move_result, True)
        move_result = g.make_move('a4', 'a4') # passing move by Red
        self.assertIs(move_result, True)
        move_result = g.make_move('b7', 'b6') # valid move by Blue
        self.assertIs(move_result, True)

#    @visibility('after_due_date')
    def test_passing_the_turn_after_capturing(self):
        """RULES: test that a player can pass the turn, a turn after capturing another player's piece"""
        g = JanggiGame()
        g.make_move('a7', 'a6') # first move by Blue
        g.make_move('a4', 'a4') # passing move by Red
        g.make_move('a6', 'a5') # valid move by Blue
        g.make_move('e4', 'e5') # valid move by Red
        g.make_move('a5', 'a4') # capturing move by Blue
        g.make_move('c4', 'c5') # valid move by Red
        passing_move = g.make_move('a4', 'a4')  # passing move by Blue
        self.assertIs(passing_move, True)
        valid_move_after_passing = g.make_move('c5', 'c6')  # valid move by Red
        self.assertIs(valid_move_after_passing, True)

#    @visibility('after_due_date')
    def test_passing_the_turn_after_being_captured(self):
        """RULES: test that a player can pass the turn, after their piece has been captured"""
        g = JanggiGame()
        g.make_move('a7', 'a6')  # first move by Blue
        g.make_move('a4', 'a4')  # passing move by Red
        g.make_move('a6', 'a5')  # valid move by Blue
        g.make_move('e4', 'e5')  # valid move by Red
        g.make_move('a5', 'a4')  # capturing move by Blue
        passing_move = g.make_move('c4', 'c4')  # passing move by Red
        self.assertIs(passing_move, True)
        valid_move_after_passing = g.make_move('a4', 'a3')  # valid move by Blue
        self.assertIs(valid_move_after_passing, True)

#    @visibility('visible')
    def test_valid_forward_move_for_red_chariot(self):
        """CHARIOT: test in the beginning of the game that a red chariot can perform a valid forward move"""
        #take a soldier for red
        g = JanggiGame()
        first_move = g.make_move('c7','c6') #because blue moves first
        red_chariot_forward_move = g.make_move('a1','a3')
        self.assertIs(red_chariot_forward_move, True)

#    @visibility('visible')
    def test_valid_sideway_move_for_red_chariot(self):
        """CHARIOT: test in the beginning of the game that a red chariot can perform a valid sideway move"""
        # take a soldier for red
        g = JanggiGame()
        g.make_move('c7', 'c6') # because blue moves first
        g.make_move('a1', 'a2') # move the red chariot ahead
        g.make_move('g7', 'g6') # blue moves
        red_chariot_sideway_move = g.make_move('a2', 'c2') #chariot moves sideway
        self.assertIs(red_chariot_sideway_move, True)

#    @visibility('visible')
    def test_valid_forward_move_for_blue_chariot(self):
        """CHARIOT: test in the beginning of the game that a blue chariot can perform a valid forward move"""
        g = JanggiGame()
        blue_chariot_forward_move = g.make_move('a10', 'a8')  # because blue moves first
        self.assertIs(blue_chariot_forward_move, True)

#    @visibility('visible')
    def test_valid_sideway_move_for_blue_chariot(self):
        """CHARIOT: test in the beginning of the game that a blue chariot can perform a valid sideway move"""
        g = JanggiGame()
        g.make_move('a10', 'a9')  # because blue moves first
        g.make_move('a1', 'a2')  # move the red chariot ahead
        blue_chariot_sideway_move = g.make_move('a9','c9')
        self.assertIs(blue_chariot_sideway_move, True)

#    @visibility('visible')
    def test_valid_backward_move_for_blue_chariot_in_south(self):
        """CHARIOT: test in the beginning of the game that a blue chariot can perform a backward move to south"""
        g = JanggiGame()
        g.make_move('a10', 'a8')  # because blue moves first
        g.make_move('a1', 'a2')  # move the red chariot ahead
        blue_chariot_backward_move = g.make_move('a8', 'a9') #chariot moves backward
        self.assertIs(blue_chariot_backward_move, True)
        pass

#    @visibility('visible')
    def test_valid_backward_move_for_blue_chariot_in_west(self):
        """CHARIOT: test in the beginning of the game that a blue chariot can perform a backward move to west"""
        g = JanggiGame()
        g.make_move('a10', 'a9')  # because blue moves first
        g.make_move('a1', 'a2')  # move the red chariot ahead
        g.make_move('a9','c9') #blue chariot moves east
        g.make_move('a2','a3') #move the red chariot ahead
        blue_chariot_backward_move = g.make_move('c9','b9')
        self.assertIs(blue_chariot_backward_move, True)
        pass

#    @visibility('after_due_date')
    def test_invalid_diagonal_move_for_blue_chariot_in_northeast(self):
        """CHARIOT: test in the beginning of the game that a blue chariot cannot perform a diagonal move"""
        g = JanggiGame()

        g.make_move('a10', 'a8')  # because blue moves first
        g.make_move('a1', 'a3')  # move the red chariot ahead
        invalid_chariot_diagonal_move = g.make_move('a8','b7') #blue chariot moves east
        self.assertIs(invalid_chariot_diagonal_move, False)
        pass

#    @visibility('after_due_date')
    def test_invalid_diagonal_move_for_red_chariot_to_southeast(self):
        """CHARIOT: test in the beginning of the game that a red chariot cannot perform a diagonal move"""
        g = JanggiGame()

        g.make_move('a10', 'a8')  # because blue moves first
        g.make_move('a1', 'a3')  # move the red chariot ahead
        g.make_move('a7','b7') # blue soldier moves ahead
        invalid_chariot_diagonal_move = g.make_move('a3', 'b4') #red chariot moves southeast
        self.assertIs(invalid_chariot_diagonal_move, False)
        pass

#    @visibility('visible')
    def test_valid_north_move_for_blue_cannon(self):
        """CANNON: test blue cannon can perform a valid north move"""
        g = JanggiGame()
        g.make_move('a7','b7') # blue soldier move sideway
        g.make_move('a4','a5') # red move
        cannon_valid_move = g.make_move('b8','b4') # blue cannon jumps over blue soldier
        self.assertIs(cannon_valid_move, True)

#    @visibility('visible')
    def test_valid_east_move_for_blue_cannon(self):
        """CANNON: test blue cannon can perform a valid east move"""
        g = JanggiGame()
        g.make_move('c7', 'c6')  # blue soldier move ahead
        g.make_move('a4', 'a5')  # red move
        g.make_move('a7', 'b7')  # blue soldier move sideway
        g.make_move('a5', 'a6')  # red move
        g.make_move('b8', 'b6')  # blue cannon jumps north
        g.make_move('a6', 'a7')  # red move
        cannon_valid_move = g.make_move('b6', 'e6')  # blue cannon jumps over blue soldier east two steps
        self.assertIs(cannon_valid_move, True)

#    @visibility('after_due_date')
    def test_valid_west_move_for_blue_cannon(self):
        """CANNON: test blue cannon can perform a valid west move"""
        g = JanggiGame()
        g.make_move('g7','h7') #blue soldier moves to make a screen
        g.make_move('g4','g5') #red soldier moves to make a future screen

        g.make_move('h8','h5') #blue cannon moves front
        g.make_move('g5','g5') #red passes
        
        cannon_valid_west_move = g.make_move('h5','a5')  #blue cannon jumps west
        self.assertIs(cannon_valid_west_move, True)

        #now try moving that cannon again back to make sure it was actually placed there
        g.make_move('g5','g5') #red passes      
        valid_cannon_move_back = g.make_move('a5','h5') #blue cannon moves east
        self.assertIs(valid_cannon_move_back, True)
        
#    @visibility('after_due_date')
    def test_valid_south_move_for_blue_cannon(self):
        """CANNON: test blue cannon can perform a valid south move"""
        g = JanggiGame()
        g.make_move('g7','h7') #blue soldier moves to make a screen
        g.make_move('g4','g5') #red soldier moves to make a future screen

        g.make_move('h8','h5') #blue cannon moves front
        g.make_move('g5','g5') #red passes
        
        g.make_move('h5','a5')  #blue cannon jumps west
        g.make_move('g5','g5') #red passes      
        valid_cannon_move_south = g.make_move('a5','a9') #blue cannon moves south
        self.assertIs(valid_cannon_move_south, True)
        #now try moving that cannon again back to make sure it was actually placed there
        g.make_move('g5','g5') #red passes      
        valid_cannon_move_back = g.make_move('a9','a6') #blue cannon moves north
        self.assertIs(valid_cannon_move_back, True)
 
#    @visibility('visible')
    def test_invalid_diagonal_move_for_blue_cannon_with_a_screen(self):
        """CANNON: test blue cannon cannot perform an invalid diagonal move with a screen"""
        g = JanggiGame()
        cannon_invalid_move = g.make_move('b8', 'd6')  # blue cannon jumps northwest
        self.assertIs(cannon_invalid_move, False)

#    @visibility('visible')
    def test_invalid_forward_move_for_blue_cannon_without_a_screen(self):
        """CANNON: test blue cannon cannot perform an invalid forward move without a screen"""
        g = JanggiGame()
        cannon_invalid_move = g.make_move('b8', 'b7')  # blue cannon move forward without a screen
        self.assertIs(cannon_invalid_move, False)

#    @visibility('after_due_date')
    def test_invalid_forward_move_for_blue_cannon_capturing_another_cannon(self):
        """CANNON: test blue cannon cannot perform an invalid capture of red cannon"""
        g = JanggiGame()
        g.make_move('c7', 'c6')  # blue soldier move ahead
        g.make_move('a4', 'a5')  # red move
        g.make_move('a7', 'b7')  # blue soldier move sideway
        g.make_move('a5', 'a6')  # red move
        g.make_move('b8', 'b6')  # blue cannon jumps north
        g.make_move('c4', 'b4')  # red move
        invalid_cannon_move = g.make_move('b6', 'b3') # cannon jumps over red soldier to capture red cannon
        self.assertIs(invalid_cannon_move, False)

#    @visibility('after_due_date')
    def test_invalid_forward_move_for_blue_cannon_jumping_over_red_cannon(self):
        """CANNON: test blue cannon cannot perform an invalid jump over red cannon"""
        g = JanggiGame()
        g.make_move('c7', 'c6')  # blue soldier move ahead
        g.make_move('a4', 'a5')  # red move
        g.make_move('a7', 'b7')  # blue soldier move sideway
        g.make_move('a5', 'a6')  # red move
        g.make_move('b8', 'b6')  # blue cannon jumps north
        g.make_move('c4', 'c5')  # red move
        invalid_cannon_move = g.make_move('b6', 'b2')  # blue cannon jumps over red cannon
        self.assertIs(invalid_cannon_move, False)

#    @visibility('after_due_date')
    def test_valid_forward_move_for_blue_cannon_capturing_red_soldier(self):
        """CANNON: test blue cannon can capture red soldier successfully"""
        g = JanggiGame()
        g.make_move('c7', 'c6')  # blue soldier move ahead
        g.make_move('a4', 'a5')  # red move
        g.make_move('a7', 'b7')  # blue soldier move sideway
        g.make_move('a5', 'b5')  # red move
        capturing_move = g.make_move('b8', 'b5')  # blue cannon jumps north to capture red soldier
        self.assertIs(capturing_move, True)
        move_on_a_non_existent_piece = g.make_move('b5', 'b6')
        self.assertIs(move_on_a_non_existent_piece, False)
        valid_move_by_red = g.make_move('e4', 'e5')  # valid move by Red
        self.assertIs(valid_move_by_red, True)


    """HORSES"""

#    @visibility('visible')
    def test_valid_forward_move_for_blue_horse_on_west_side(self):
        """HORSE: test blue horse from west can make a valid move forward"""
        g = JanggiGame()
        valid_move = g.make_move('c10', 'd8')
        self.assertIs(valid_move, True)

#    @visibility('visible')
    def test_valid_forward_move_for_blue_horse_on_east_side(self):
        """HORSE: test blue horse from east can make a valid move forward"""
        g = JanggiGame()
        valid_move = g.make_move('h10', 'g8')
        self.assertIs(valid_move, True)

#    @visibility('visible')
    def test_invalid_forward_move_for_blue_horse_on_west_side(self):
        """HORSE: test blue horse from west cannot make an invalid move forward"""
        g = JanggiGame()
        invalid_move = g.make_move('c10', 'd7')
        self.assertIs(invalid_move, False)

#    @visibility('visible')
    def test_invalid_forward_move_for_blue_horse_on_east_side(self):
        """HORSE: test blue horse from east cannot make an invalid move forward"""
        g = JanggiGame()
        valid_move = g.make_move('h10', 'f8')
        self.assertIs(valid_move, False)

#    @visibility('visible')
    def test_horse_is_blocked_by_a_piece(self):
        """HORSE: test horse cannot jump over their own piece"""
        g = JanggiGame()
        g.make_move('c10', 'd8') #blue horse moves
        g.make_move('c1','d3') #red horse move
        g.make_move('c7','d7') #blue soldier moves to block the blue horse
        g.make_move('c4','d4') #red soldier moves to block the red horse
        try:
            invalid_move_because_of_block = g.make_move('d8','c6') #invalid move because blocked by own soldier
            self.assertIs(invalid_move_because_of_block, False)
        except:
            self.fail("Blue horse from west should not be able to jump over a blue piece")
        g.make_move('d8','d8') # blue passes the turn
        
        try:
            invalid_move_because_of_block = g.make_move('d3','d6') #invalid move by red because blocked by own soldier
            self.assertIs(invalid_move_because_of_block, False)
        except:
            self.fail("Red horse from west should not be able to jump over a red piece")
        g.make_move('d3','d3') #red passes the turn
        
        g.make_move('h10', 'g8') #blue horse move
        g.make_move('h2','g3') #red horse move
        try:
            invalid_move_because_of_block = g.make_move('g8','h6') #invalid move by blue because blocked by own soldier
            self.assertIs(invalid_move_because_of_block, False)
        except:
            self.fail("Blue horse from east should not be able to jump over a blue piece")
        
        g.make_move('g8','g8') #blue passes the turn

        try:
            invalid_move_because_of_block = g.make_move('g3','g5') #invalid move because blocked by own soldier
            self.assertIs(invalid_move_because_of_block, False)
        except:
            self.fail("Red horse from east should not be able to jump over a red piece")

#    @visibility('visible')
    def test_horse_can_capture_a_piece(self):
        """HORSE: test that a horse can capture another player's piece"""
        g = JanggiGame()
        g.make_move('c10','d8') #blue horse moves
        g.make_move('c1','d3') #red horse moves
        g.make_move('e7','e6') #blue soldier
        g.make_move('e4','e5') #red
        g.make_move('c7','c6') #blue
        g.make_move('c4','c5') #red

        g.make_move('c6','c5') #blue soldier captures red
        g.make_move('e5','e6') #red soldier captures blue

        try:
            capturing_move = g.make_move('d8','e6')
            self.assertIs(capturing_move, True)
        except:
            self.fail("Blue Horse from West should be able to capture a Red soldier")

        try:
            capturing_move = g.make_move('d3','c5') #red capture
            self.assertIs(capturing_move, True)
        except:
            self.fail("Red Horse from West should be able to capture a Blue Soldier")

        g.make_move('h10', 'g8')  # blue horse from east
        g.make_move('h1', 'i3') #red horse from east

        g.make_move('g7','h7') #blue
        g.make_move('g4', 'f4') #red

        g.make_move('h7', 'h6') #blue
        g.make_move('i4','i5') #red
        g.make_move('h6','h5') #blue
        g.make_move('i5','i6') #red

        g.make_move('g8','g8') #blue passes

        try:
            valid_capture_move = g.make_move('i3','h5')
            self.assertIs(valid_capture_move, True)
        except:
            self.fail("Red Horse from East should be able to capture a Blue Soldier")

        g.make_move('g8','g8') #blue passes
        g.make_move('i6','h6') #red moves

        try:
            valid_capture_move = g.make_move('g8', 'h6')
            self.assertIs(valid_capture_move, True)
        except:
            self.fail("Blue Horse from East should be able to capture a Red soldier")

#    @visibility('after_due_date')
    def test_horse_cannot_capture_own_piece(self):
        """HORSE: test that a horse cannot capture same player's piece"""
        g = JanggiGame()
        try:
            invalid_capturing_move = g.make_move('c10', 'b8')  # blue horse tries to get at the same place as Cannon
            self.assertIs(invalid_capturing_move, False)
        except:
            self.fail("Blue Horse from west should not be able to capture a blue piece")

        g.make_move('g7', 'g7')  # blue passing move

        try:
            invalid_capturing_move = g.make_move('c1', 'b3')  # red horse tries to get at the same place as Cannon
            self.assertIs(invalid_capturing_move, False)
        except:
            self.fail("Red Horse from west should not be able to capture a red piece")

        try:
            g.make_move('h1', 'g3')  #red horse moves
            g.make_move('g7', 'g7') #blue passes
            invalid_capturing_move = g.make_move('g3', 'f1') #red horse tries to get at the same place as red guard
            self.assertIs(invalid_capturing_move, False)
        except:
            self.fail("Red Horse from west should not be able to capture a red piece")

        g.make_move('f1','f1') #red passing move
        try:
            g.make_move('h10', 'g8')  # blue horse moves
            g.make_move('f1', 'f1')  # red passes
            invalid_capturing_move = g.make_move('g8', 'f10')  # blue horse tries to get at the same place as blue guard
            self.assertIs(invalid_capturing_move, False)
        except:
            self.fail("Blue Horse from east should not be able to capture a blue piece")

    """GUARDS"""
#    @visibility('visible')
    def test_valid_move_for_guard(self):
        """GUARD: test valid moves for guard"""
        g = JanggiGame()
        try:
            valid_move = g.make_move('d10','d9') #blue guard moves
            self.assertIs(valid_move, True)
        except:
            self.fail("Blue Guard from west should be able to make a valid move")

        try:
            valid_move = g.make_move('d1','d2') #red guard moves
            self.assertIs(valid_move, True)
        except:
            self.fail("Red Guard from west should be able to make a valid move")

        try:
            valid_move = g.make_move('f10','f9') #blue guard moves
            self.assertIs(valid_move, True)
        except:
            self.fail("Blue Guard from east should be able to make a valid move")

        try:
            valid_move = g.make_move('f1','f2') #red guard moves
            self.assertIs(valid_move, True)
        except:
            self.fail("Red Guard from east should be able to make a valid move")

        try:
            valid_move = g.make_move('d9','d8') #blue guard moves
            self.assertIs(valid_move, True)
        except:
            self.fail("Blue Guard from west should be able to make a valid move")

        try:
            valid_move = g.make_move('d2','d3') #red guard moves
            self.assertIs(valid_move, True)
        except:
            self.fail("Red Guard from west should be able to make a valid move")

        try:
            valid_move = g.make_move('f9','f8') #blue guard moves
            self.assertIs(valid_move, True)
        except:
            self.fail("Blue Guard from east should be able to make a valid move")

        try:
            valid_move = g.make_move('f2','f3') #red guard moves
            self.assertIs(valid_move, True)
        except:
            self.fail("Red Guard from east should be able to make a valid move")

        #perform diagonal moves
        g.make_move('e9','e10') #blue general moves
        g.make_move('e2','e1') #red general moves

        try:
            valid_diagonal_move = g.make_move('d8','e9')  #blue guard moves
            self.assertIs(valid_diagonal_move, True)
        except:
            self.fail("Blue Guard should be able to make a diagonal move")

        try:
            valid_diagonal_move = g.make_move('d3','e2')  #red guard moves
            self.assertIs(valid_diagonal_move, True)
        except:
            self.fail("Red Guard should be able to make a diagonal move")

#    @visibility('after_due_date')
    def test_invalid_move_for_guard(self):
        """GUARD: test invalid moves for guard"""
        g = JanggiGame()
        g.make_move('d10','d9') #blue moves
        g.make_move('d1','d2') #red moves
        g.make_move('f10','f9') #blue moves
        g.make_move('f1','f2') #red moves

        g.make_move('d9','d8') #blue moves
        g.make_move('d2','d3') #red moves
        g.make_move('f9','f8') #blue moves
        g.make_move('f2','f3') #red moves

        try:
            invalid_move = g.make_move('d8','c8') #blue guard tries to move outside the palace
            self.assertIs(invalid_move, False)
        except:
            self.fail("Blue Guard should not be able to move outside the palace")

        g.make_move('d8','d8') #blue passes

        try:
            invalid_move = g.make_move('d3','c3') #red guard tries to move outside the palace
            self.assertIs(invalid_move, False)
        except:
            self.fail("Red Guard should not be able to move outside the palace")

        g.make_move('d3','d3') #red passes

        try:
            invalid_move = g.make_move('f8','g8') #blue guard tries to move outside the palace
            self.assertIs(invalid_move, False)
        except:
            self.fail("Blue Guard should not be able to move outside the palace")

        g.make_move('f8','f8') #blue passes

        try:
            invalid_move = g.make_move('f3','g3') #red guard tries to move outside the palace
            self.assertIs(invalid_move, False)
        except:
            self.fail("Red Guard should not be able to move outside the palace")

#    @visibility('visible')
    def test_valid_move_for_elephant(self):
        """ELEPHANT: test elephants can make valid moves"""
        g = JanggiGame()

        try:
            valid_move = g.make_move('b10','d7') #blue elephant moves
            self.assertIs(valid_move, True)
        except:
            self.fail("Blue Elephant from west should be able to make a valid move")

        try:
            valid_move = g.make_move('b1','d4') #red elephant moves
            self.assertIs(valid_move, True)
        except:
            self.fail("Red Elephant from west should be able to make a valid move")

        g.make_move('e7', 'e6')  # blue soldier moves to make place for eastern blue elephant
        g.make_move('e4', 'e5')  # red  soldier moves to make place for eastern red elephant

        try:
            valid_move = g.make_move('g10','e7') #blue elephant moves
            self.assertIs(valid_move, True)
        except:
            self.fail("Blue Elephant from east should be able to make a valid move")

        try:
            valid_move = g.make_move('g1','e4') #red elephant moves
            self.assertIs(valid_move, True)
        except:
            self.fail("Red Elephant from east should be able to make a valid move")

#    @visibility('after_due_date')
    def test_invalid_move_for_elephant(self):
        """ELEPHANT: test elephant cannot make invalid moves"""
        g = JanggiGame()
        invalid_move = g.make_move('b10','c8') #blue
        self.assertIs(invalid_move, False)
        invalid_move = g.make_move('b10','b9') #moves forward like a soldier
        self.assertIs(invalid_move, False)
        invalid_move = g.make_move('b10','b9') #move one diagonal
        self.assertIs(invalid_move, False)
        invalid_move = g.make_move('b10','b7') #tries to jump over cannon
        self.assertIs(invalid_move, False)

        g.make_move('b10','b10') #blue passes

        #try on red
        invalid_move = g.make_move('g1','g2') #red move like a soldier
        self.assertIs(invalid_move, False)
        invalid_move = g.make_move('g1','f2') #move one diagonal
        self.assertIs(invalid_move, False)
        invalid_move = g.make_move('g1','g5') #tries to jump over the soldier
        self.assertIs(invalid_move, False)

#    @visibility('visible')
    def test_valid_moves_for_general(self):
        """GENERAL: test general can perform valid moves"""
        g = JanggiGame()
        valid_move = g.make_move('e9', 'f8') # blue
        self.assertIs(valid_move, True)

        valid_move = g.make_move('e2', 'f3') # red
        self.assertIs(valid_move, True)

        valid_move = g.make_move('f8','e8') # blue
        self.assertIs(valid_move, True)

        valid_move = g.make_move('f3','e3') # red
        self.assertIs(valid_move, True)

        valid_move = g.make_move('e8','d8') # blue
        self.assertIs(valid_move, True)

        valid_move = g.make_move('e3', 'd3') # red
        self.assertIs(valid_move, True)

        valid_move = g.make_move('d8', 'd9') # blue
        self.assertIs(valid_move, True)

        valid_move = g.make_move('d3', 'd2') # red
        self.assertIs(valid_move, True)

        valid_move = g.make_move('d9','e9') #blue
        self.assertIs(valid_move, True)

        valid_move = g.make_move('d2','e2') #red
        self.assertIs(valid_move, True)

        valid_move = g.make_move('e9', 'e10') #blue
        self.assertIs(valid_move, True)

        valid_move = g.make_move('e2','e1') #red
        self.assertIs(valid_move, True)


#    @visibility('visible')
    def test_invalid_moves_for_general(self):
        """GENERAL: test general cannot perform invalid moves"""
        g = JanggiGame()
        valid_move = g.make_move('e9', 'f8') # blue
        valid_move = g.make_move('e2', 'f3') # red

        #moving outside the palace
        invalid_move = g.make_move('f8','g8') #blue
        self.assertIs(invalid_move, False)

        #blue passes
        g.make_move('f8','f8')

        invalid_move = g.make_move('f3', 'f4')  # red
        self.assertIs(invalid_move, False)

        # red passes
        g.make_move('f3', 'f3')


        #prepare for the move
        g.make_move('f10','e10') #blue
        g.make_move('f1','e1') #red

        #moving two spaces
        invalid_move = g.make_move('f8','f10')
        self.assertIs(invalid_move, False)

        g.make_move('f8','f8') #blue passes

        # moving two spaces
        invalid_move = g.make_move('f3', 'f1')
        self.assertIs(invalid_move, False)

        g.make_move('f3','f3') #red passes

        g.make_move('e10','e9') #blue moves
        g.make_move('e1','e2') #red moves

        #moving at a place where another piece already exists
        invalid_move = g.make_move('f8','e9') #blue
        self.assertIs(invalid_move, False)

        g.make_move('f8','f8') #blue passes

        invalid_move = g.make_move('f3', 'e2')  # blue
        self.assertIs(invalid_move, False)

#    @visibility('visible')
    def test_unfinished_game_state(self):
        """RULES: test that get_game_state returns UNFINISHED correctly"""
        g = JanggiGame()
        g.make_move('e7','f7') #blue
        self.assertEqual(g.get_game_state().upper(),'UNFINISHED')

        g.make_move('e4','e5')#red
        self.assertEqual(g.get_game_state().upper(), 'UNFINISHED')

#    @visibility('after_due_date')
    def test_unfinished_game_state_after_capture(self):
        """RULES: test that get_game_state returns UNFINISHED correctly after a piece is captured"""
        g = JanggiGame()
        g.make_move('c7','c6') #blue moves
        g.make_move('e4','f4') #red moves
        g.make_move('b10','d7') #blue elephant moves
        g.make_move('d1','d2') #red
        g.make_move('c10','c9') #blue
        g.make_move('g4','h4') #red
        g.make_move('i10','i8')
        g.make_move('e2','f2') #red
        g.make_move('g7','h7')
        g.make_move('h3','h5') #red
        g.make_move('h7','g7')
        g.make_move('c1','e2') #red
        g.make_move('i7','i6')
        g.make_move('g1','e4') #red
        g.make_move('i6','h6') #blue captures red cannon
        try:
            self.assertEqual(g.get_game_state().upper(),'UNFINISHED')
        except:
            self.fail("Game state should be UNFINISHED if no one has won")


#    @visibility('visible')
    def test_is_in_check_blue(self):
        """RULES: test that is_in_check detects check correctly for blue"""
        g = JanggiGame()
        
        g.make_move('c7','c6') #blue
        g.make_move('c1','d3') #red
        g.make_move('b10','d7') #blue
        g.make_move('b3','e3') #red
        g.make_move('c10','d8') #blue
        g.make_move('h1','g3') #red
        g.make_move('e7','e6') # blue
        g.make_move('e3', 'e6') #red cannon captures soldier -- check here
        
        try:
            self.assertEqual(g.get_game_state().upper(), 'UNFINISHED')
        except:
            self.fail("Game state should be unfinished before an actual check")

        try:
            self.assertIs(g.is_in_check('red'), False)
        except:
            self.fail("General is not in check and yet is_in_check returns True for red")

        try:
            self.assertIs(g.is_in_check('blue'), False)
        except:
            self.fail("General is not in check and yet is_in_check returns True for blue")
        
        g.make_move('h8','c8') #blue cannon moves -- check here
        g.make_move('d3','e5') #red
        g.make_move('c8','c4') #blue cannon captures red soldier -- check here
        try:
            self.assertEqual(g.get_game_state().upper(), 'UNFINISHED')
        except:
            self.fail("Game state should be unfinished before an actual check")

        try:
            self.assertIs(g.is_in_check('red'), False)
        except:
            self.fail("General is not in check and yet is_in_check returns True for red")

        try:
            self.assertIs(g.is_in_check('blue'), False)
        except:
            self.fail("General is not in check and yet is_in_check returns True for blue")

        g.make_move('e5','c4') #red horse captures blue cannon
        g.make_move('i10','i8') #blue chariot moves
        g.make_move('g4','f4')
        g.make_move('i8','f8') #blue chariot moves sideway
        g.make_move('g3','h5')
        g.make_move('h10','g8') #blue horse
        self.assertTrue(g.make_move('e6','e3')) #red CHECKS blue using a cannon -- special test for checks using a cannon -- check here
        
        try:
            self.assertEqual(g.get_game_state().upper(),'UNFINISHED')
        except:
            self.fail("Game state should be UNFINISHED when a general is in check but not checkmated")

        try:
            self.assertIs(g.is_in_check('red'), False)
        except:
            self.fail("Red General is not in check and yet is_in_check returns True for red")

        try:
            self.assertIs(g.is_in_check('blue'), True)
        except:
            self.fail("Blue General is in check and is_in_check should return True for blue")
 
        g.make_move('e9','d9') #general moves to avoid check -- check here
        
        try:
            self.assertIs(g.is_in_check('red'), False)
        except:
            self.fail("General is not in check and yet is_in_check returns True for red")

        try:
            self.assertIs(g.is_in_check('blue'), False)
        except:
            self.fail("General is not in check and yet is_in_check returns True for blue")
        
        try:
            self.assertEqual(g.get_game_state().upper(),'UNFINISHED')
        except:
            self.fail("Game state should be UNFINISHED when a general is in check")

#    @visibility('after_due_date')
    def test_is_in_check_red(self):
        """RULES: test that is_in_check detects check correctly for red"""
        g = JanggiGame()
        
        g.make_move('c7','c6') #blue
        g.make_move('c1','d3') #red
        g.make_move('b10','d7') #blue
        g.make_move('b3','e3') #red
        g.make_move('c10','d8')
        g.make_move('h1','g3')
        g.make_move('e7','e6')
        g.make_move('e3', 'e6') #red cannon captures soldier -- check here
        
        try:
            self.assertEqual(g.get_game_state().upper(), 'UNFINISHED')
        except:
            self.fail("Game state should be unfinished before an actual check")

        try:
            self.assertIs(g.is_in_check('red'), False)
        except:
            self.fail("General is not in check and yet is_in_check returns True for Red")

        try:
            self.assertIs(g.is_in_check('blue'), False)
        except:
            self.fail("General is not in check and yet is_in_check returns True for Blue")
        
        g.make_move('h8','c8') #blue moves -- check here
        g.make_move('d3','e5') #red
        g.make_move('c8','c4') #blue cannon captures red soldier -- check here
        try:
            self.assertEqual(g.get_game_state().upper(), 'UNFINISHED')
        except:
            self.fail("Game state should be unfinished before an actual win")

        try:
            self.assertIs(g.is_in_check('red'), False)
        except:
            self.fail("General is not in check and yet is_in_check returns True for Red")

        try:
            self.assertIs(g.is_in_check('blue'), False)
        except:
            self.fail("General is not in check and yet is_in_check returns True for Blue")

        g.make_move('e5','c4') #red horse captures blue cannon
        g.make_move('i10','i8') #blue chariot moves
        g.make_move('g4','f4')
        g.make_move('i8','f8') #blue chariot moves sideway
        g.make_move('g3','h5')
        g.make_move('h10','g8') #blue horse
        g.make_move('e6','e3') #red CHECKS blue using a cannon -- special test for checks using a cannon -- check here
        
        try:
            self.assertEqual(g.get_game_state().upper(),'UNFINISHED')
        except:
            self.fail("Game state should be UNFINISHED when a general is in check but not checkmated")

        try:
            self.assertIs(g.is_in_check('red'), False)
        except:
            self.fail("Red General is not in check and yet is_in_check returns True for red")

        try:
            self.assertIs(g.is_in_check('blue'), True)
        except:
            self.fail("Blue General is in check and is_in_check should return True for blue")

        g.make_move('e9','d9') #blue moves 
        g.make_move('c4','e5') #red
        g.make_move('c6','d6')
        g.make_move('e5','c4')
        g.make_move('a7','a6')#blue
        g.make_move('h3', 'h9') #red cannon moves to a position where it COULD Check but has not. -- check here
        g.make_move('a10','a7')
        g.make_move('c4','d6') #red horse captures blue soldier
        g.make_move('a6','b6')
        g.make_move('h5','g7')
        g.make_move('b8','b1')#blue cannon captures red elephant
        g.make_move('a1','b1') #red chariot captures blue cannon
        g.make_move('a7','a4')
        g.make_move('b1','c1')
        g.make_move('a4','a2') #blue CHECKS red using a chariot -- check here
        
        try:
            self.assertIs(g.is_in_check('red'), True)
        except:
            self.fail("Red General is in check and yet is_in_check returns False for red")

        try:
            self.assertIs(g.is_in_check('blue'), False)
        except:
            self.fail("Blue General is not in check and yet is_in_check returns True for blue")
        
        try:
            self.assertEqual(g.get_game_state().upper(),'UNFINISHED')
        except:
            self.fail("Game state should be UNFINISHED when a general is in check but not checkmated")

        g.make_move('e2','e1') #red general moves to avoid capture -- check after this

        try:
            self.assertIs(g.is_in_check('red'), False)
        except:
            self.fail("General is not in check and yet is_in_check returns True for red")

        try:
            self.assertIs(g.is_in_check('blue'), False)
        except:
            self.fail("General is not in check and yet is_in_check returns True for blue")
        
        try:
            self.assertEqual(g.get_game_state().upper(),'UNFINISHED')
        except:
            self.fail("Game state should be UNFINISHED when a general is in check")


#    @visibility('after_due_date')
    def test_is_in_check_after_a_check_was_countered(self):
        """RULES: test that is_in_check detects check correctly after a check is countered"""
        g = JanggiGame()
        
        g.make_move('c7','c6') #blue
        g.make_move('c1','d3') #red
        g.make_move('b10','d7') #blue
        g.make_move('b3','e3') #red
        g.make_move('c10','d8')
        g.make_move('h1','g3')
        g.make_move('e7','e6')
        g.make_move('e3', 'e6') #red cannon captures soldier -- check here
        
        g.make_move('h8','c8') #blue moves -- check here
        g.make_move('d3','e5') #red
        g.make_move('c8','c4') #blue cannon captures red soldier -- check here
        g.make_move('e5','c4') #red horse captures blue cannon
        g.make_move('i10','i8') #blue chariot moves
        g.make_move('g4','f4')
        g.make_move('i8','f8') #blue chariot moves sideway
        g.make_move('g3','h5')
        g.make_move('h10','g8') #blue horse
        g.make_move('e6','e3') #red CHECKS blue using a cannon -- special test for checks using a cannon -- check here

        g.make_move('e9','d9') #general moves to avoid check -- check here
        
        try:
            self.assertIs(g.is_in_check('red'), False)
        except:
            self.fail("General is not in check and yet is_in_check returns True for Red")

        try:
            self.assertIs(g.is_in_check('blue'), False)
        except:
            self.fail("General is not in check and yet is_in_check returns True for Blue")

        try:
            self.assertEqual(g.get_game_state().upper(),'UNFINISHED')
        except:
            self.fail("Game state should be UNFINISHED since no one has won")


#    @visibility('after_due_date')
    def test_a_checkmate_is_detected_correctly(self):
        g = JanggiGame()
        
        g.make_move('c7','c6') #blue
        g.make_move('c1','d3') #red
        g.make_move('b10','d7') #blue
        g.make_move('b3','e3') #red
        g.make_move('c10','d8')
        g.make_move('h1','g3')
        g.make_move('e7','e6')
        g.make_move('e3', 'e6') #red cannon captures soldier -- check here
        
        try:
            self.assertEqual(g.get_game_state().upper(), 'UNFINISHED')
        except:
            self.fail("Game state should be unfinished before an actual check")

        try:
            self.assertIs(g.is_in_check('red'), False)
        except:
            self.fail("General is not in check and yet is_in_check returns True for Red")

        try:
            self.assertIs(g.is_in_check('blue'), False)
        except:
            self.fail("General is not in check and yet is_in_check returns True for Blue")
        
        g.make_move('h8','c8') #blue moves -- check here
        g.make_move('d3','e5') #red
        g.make_move('c8','c4') #blue cannon captures red soldier -- check here
        try:
            self.assertEqual(g.get_game_state().upper(), 'UNFINISHED')
        except:
            self.fail("Game state should be unfinished before an actual win")

        try:
            self.assertIs(g.is_in_check('red'), False)
        except:
            self.fail("General is not in check and yet is_in_check returns True for Red")

        try:
            self.assertIs(g.is_in_check('blue'), False)
        except:
            self.fail("General is not in check and yet is_in_check returns True for Blue")

        g.make_move('e5','c4') #red horse captures blue cannon
        g.make_move('i10','i8') #blue chariot moves
        g.make_move('g4','f4')
        g.make_move('i8','f8') #blue chariot moves sideway
        g.make_move('g3','h5')
        g.make_move('h10','g8') #blue horse
        g.make_move('e6','e3') #red CHECKS blue using a cannon -- special test for checks using a cannon -- check here
        
        try:
            self.assertEqual(g.get_game_state().upper(),'UNFINISHED')
        except:
            self.fail("Game state should be UNFINISHED when a general is in check but not checkmated")

        try:
            self.assertIs(g.is_in_check('red'), False)
        except:
            self.fail("Red General is not in check and yet is_in_check returns True for red")

        try:
            self.assertIs(g.is_in_check('blue'), True)
        except:
            self.fail("Blue General is in check and is_in_check should return True for blue")

        g.make_move('e9','d9') #blue moves 
        g.make_move('c4','e5') #red
        g.make_move('c6','d6')
        g.make_move('e5','c4')
        g.make_move('a7','a6')#blue
        g.make_move('h3', 'h9') #red cannon moves to a position where it COULD Check but has not. -- check here
        g.make_move('a10','a7')
        g.make_move('c4','d6') #red horse captures blue soldier
        g.make_move('a6','b6')
        g.make_move('h5','g7')
        g.make_move('b8','b1')#blue cannon captures red elephant
        g.make_move('a1','b1') #red chariot captures blue cannon
        g.make_move('a7','a4')
        g.make_move('b1','c1')
        g.make_move('a4','a2') #blue CHECKS red using a chariot -- check here
        
        g.make_move('e2','e1') #red general moves to avoid capture -- check after this

        g.make_move('i7','h7') #blue moves
        g.make_move('c1','c9') #red chariot moves to the palace to CHECKMATE blue
    
        try:
            self.assertIs(g.is_in_check('red'), False)
        except:
            self.fail("Red General is not in check and yet is_in_check returns True for red")

        try:
            self.assertIs(g.is_in_check('blue'), True)
        except:
            self.fail("Blue General is in check and is_in_check should return True for blue")
        
        try:
            self.assertEqual(g.get_game_state().upper(),'RED_WON')
        except:
            self.fail("Game state should be RED_WON when the BLUE general is checkmated")

#    @visibility('after_due_date')
    def test_a_move_cannot_be_made_after_checkmate(self):
        """RULES: test that a move cannot be made after checkmate i.e. the one of the players has won"""

        g = JanggiGame()
        
        g.make_move('c7','c6') #blue
        g.make_move('c1','d3') #red
        g.make_move('b10','d7') #blue
        g.make_move('b3','e3') #red
        g.make_move('c10','d8')
        g.make_move('h1','g3')
        g.make_move('e7','e6')
        g.make_move('e3', 'e6') #red cannon captures soldier -- check here

        g.make_move('h8','c8') #blue moves -- check here
        g.make_move('d3','e5') #red
        g.make_move('c8','c4') #blue cannon captures red soldier -- check here
        g.make_move('e5','c4') #red horse captures blue cannon
        g.make_move('i10','i8') #blue chariot moves
        g.make_move('g4','f4')
        g.make_move('i8','f8') #blue chariot moves sideway
        g.make_move('g3','h5')
        g.make_move('h10','g8') #blue horse
        g.make_move('e6','e3') #red CHECKS blue using a cannon -- special test for checks using a cannon -- check here
        
        g.make_move('e9','d9') #blue moves 
        g.make_move('c4','e5') #red
        g.make_move('c6','d6')
        g.make_move('e5','c4')
        g.make_move('a7','a6')#blue
        g.make_move('h3', 'h9') #red cannon moves to a position where it COULD Check but has not. -- check here
        g.make_move('a10','a7')
        g.make_move('c4','d6') #red horse captures blue soldier
        g.make_move('a6','b6')
        g.make_move('h5','g7')
        g.make_move('b8','b1')#blue cannon captures red elephant
        g.make_move('a1','b1') #red chariot captures blue cannon
        g.make_move('a7','a4')
        g.make_move('b1','c1')
        g.make_move('a4','a2') #blue CHECKS red using a chariot -- check here
        
        g.make_move('e2','e1') #red general moves to avoid capture -- check after this

        g.make_move('i7','h7') #blue moves
        g.make_move('c1','c9') #red chariot moves to the palace to CHECKMATE blue
    
        try:
            self.assertIs(g.is_in_check('red'), False)
        except:
            self.fail("Red General is not in check and yet is_in_check returns True for red")

        try:
            self.assertIs(g.is_in_check('blue'), True)
        except:
            self.fail("Blue General is in check and is_in_check should return True for blue")
        
        try:
            self.assertEqual(g.get_game_state().upper(),'RED_WON')
        except:
            self.fail("Game state should be RED_WON when the BLUE general is checkmated")

        #try moving a non-General piece
        try:
            invalid_move_after_checkmate = g.make_move('c9', 'c1') #red chariot move
            self.assertIs(invalid_move_after_checkmate, False)
            invalid_move_after_checkmate = g.make_move('i8', 'i7')  # red Elephant move
            self.assertIs(invalid_move_after_checkmate, False)
        except:
            self.fail("make_move should not allow any move after a checkmate")

        # try moving the General piece
        try:
            invalid_move_after_checkmate = g.make_move('d9', 'e9')  # blue General move
            self.assertIs(invalid_move_after_checkmate, False)
            invalid_move_after_checkmate = g.make_move('e1', 'f2')  # red General move
            self.assertIs(invalid_move_after_checkmate, False)
        except:
            self.fail("make_move should not allow any move after a checkmate")

#    @visibility('visible')
    def test_turn_taking_is_implemented_correctly(self):
        """RULES: test that turn taking is implemented correctly"""
        g = JanggiGame()
        #blue moves first
        try:
            invalid_first_move = g.make_move('a1','a3') #red tries to move first
            self.assertIs(invalid_first_move, False)
        except:
            self.fail("Red should not be able to move first")

        try:
            valid_first_move = g.make_move('a7','a6') #blue moves first
            self.assertIs(valid_first_move, True)
        except:
            self.fail("Blue should be able to move first")

        try:
            valid_first_move = g.make_move('a1','a2') #red moves now
            self.assertIs(valid_first_move, True)
        except:
            self.fail("Red should be able to move after blue")

        try:
            valid_first_move = g.make_move('d10','d9') #blue moves
            self.assertIs(valid_first_move, True)
        except:
            self.fail("Blue should be able to move after red")

        try:
            valid_first_move = g.make_move('c4', 'c5')  # red moves now
            self.assertIs(valid_first_move, True)
        except:
            self.fail("Red should be able to move after blue")

#    @visibility('after_due_date')
    def test_that_horse_is_transposed_with_elephant_in_the_initial_setup_by_trying_to_move_it(self):
        """RULES: Transposition of Horse and Elephant is correct in the beginning"""
        g = JanggiGame()

        g.make_move('e7', 'e6')  # blue soldier moves to make place for eastern blue elephant
        g.make_move('e4', 'e5')  # red  soldier moves to make place for eastern red elephant

        try:
            valid_move = g.make_move('g10','e7') #blue elephant moves
            self.assertIs(valid_move, True)
        except:
            self.fail("Blue Elephant from east is either not transposed correctly with Horse in the inital setup or cannot perform valid moves")

        try:
            valid_move = g.make_move('g1','e4') #red elephant moves
            self.assertIs(valid_move, True)
        except:
            self.fail("Red Elephant from east is either not transposed correctly with Horse in the inital setup or cannot perform valid moves") 


#    @visibility('after_due_date')
    def test_that_a_check_by_a_cannon_outside_the_palace_is_detected(self):
        """RULES: Check by a cannon outside the palace is detected"""
        g = JanggiGame()
        
        g.make_move('c7','c6') #blue
        g.make_move('c1','d3') #red
        g.make_move('b10','d7') #blue
        g.make_move('b3','e3') #red
        g.make_move('c10','d8')
        g.make_move('h1','g3')
        g.make_move('e7','e6')
        g.make_move('e3', 'e6') #red cannon captures soldier -- check here
        g.make_move('h8','c8') #blue cannon moves -- check here
        g.make_move('d3','e5') #red
        g.make_move('c8','c4') #blue cannon captures red soldier -- check here
        g.make_move('e5','c4') #red horse captures blue cannon
        g.make_move('i10','i8') #blue chariot moves
        g.make_move('g4','f4')
        g.make_move('i8','f8') #blue chariot moves sideway
        g.make_move('g3','h5')
        g.make_move('h10','g8') #blue horse
        self.assertTrue(g.make_move('e6','e3')) #red CHECKS blue using a cannon -- special test for checks using a cannon -- check here
        
        try:
            self.assertEqual(g.get_game_state().upper(),'UNFINISHED')
        except:
            self.fail("Game state should be UNFINISHED when a general is in check but not checkmated")

        try:
            self.assertIs(g.is_in_check('red'), False)
        except:
            self.fail("Red General is not in check and yet is_in_check returns True for red")

        try:
            self.assertIs(g.is_in_check('blue'), True)
        except:
            self.fail("Blue General is in check with a Cannon outside the palace and is_in_check should return True for blue")
 
#    @visibility('after_due_date')
    def test_that_a_check_by_a_horse_outside_the_palace_is_detected(self):
        """RULES: Check by a horse outside the palace is detected"""
        g = JanggiGame()
        
        g.make_move('c7','c6') #blue
        g.make_move('c1','d3') #red
        g.make_move('b10','d7') #blue
        g.make_move('b3','e3') #red
        g.make_move('c10','d8')
        g.make_move('h1','g3')
        g.make_move('e7','e6')
        g.make_move('e3', 'e6') #red cannon captures soldier -- check here
        g.make_move('h8','c8') #blue cannon moves -- check here
        g.make_move('d3','e5') #red
        g.make_move('c8','c4') #blue cannon captures red soldier -- check here
        g.make_move('e5','c4') #red horse captures blue cannon
        g.make_move('i10','i8') #blue chariot moves
        g.make_move('g4','f4')
        g.make_move('i8','f8') #blue chariot moves sideway
        g.make_move('g3','h5')
        g.make_move('h10','g8') #blue horse
        g.make_move('e6','e3') #red CHECKS blue using a cannon -- special test for checks using a cannon -- check here
        g.make_move('e9','d9') #blue general moves to counter check

        g.make_move('c4','b6') #red horse moves
        g.make_move('g7','f7') #blue soldier moves
        g.make_move('e4','e5') #red moves
        g.make_move('f7','e7') #blue moves
        g.make_move('e5','e6') #red moves
        g.make_move('d9','e9') #blue general moves
        g.make_move('b6','a8') #red horse moves southwest
        g.make_move('d8','b7') #blue horse moves
        g.make_move('a8','b10') #red horse moves
        g.make_move('e9','e9') #blue passes
        g.make_move('b10','c8') #red horse puts blue general in check

        try:
            self.assertEqual(g.get_game_state().upper(),'UNFINISHED')
        except:
            self.fail("Game state should be UNFINISHED when a general is in check but not checkmated")

        try:
            self.assertIs(g.is_in_check('red'), False)
        except:
            self.fail("Red General is not in check and yet is_in_check returns True for red")

        try:
            self.assertIs(g.is_in_check('blue'), True)
        except:
            self.fail("Blue General is in check with a Horse outside the palace and is_in_check should return True for blue")

#    @visibility('after_due_date')
    def test_that_countering_the_check_by_capturing_the_cannon_is_detected_correctly(self):
        """RULES: Countering the check by capturing the cannon is detected correctly"""
        g = JanggiGame()
        
        g.make_move('c7','c6') #blue
        g.make_move('c1','d3') #red
        g.make_move('b10','d7') #blue
        g.make_move('b3','b3') #red passes
        g.make_move('c10','d8')
        g.make_move('h1','g3')
        g.make_move('e7','e6')
        g.make_move('b3','b3') #red passes
        g.make_move('e6', 'f6') #blue soldier moves sidewways
        g.make_move('b3','b3') #red passes
        g.make_move('h8','c8') #blue cannon moves -- check here
        g.make_move('d3','e5') #red
        g.make_move('c8','c4') #blue cannon captures red soldier -- check here
        g.make_move('e5','c4') #red horse captures blue cannon
        g.make_move('i10','i8') #blue chariot moves
        g.make_move('g4','f4')
        g.make_move('i8','f8') #blue chariot moves sideway
        g.make_move('g3','h5')
        g.make_move('h10','g8') #blue horse
        g.make_move('d1','d2') #red moves
        g.make_move('e9','e9') #blue passes
        g.make_move('d2','d3') #red moves
        self.assertTrue(g.make_move('e9','e9')) #blue passes
        self.assertTrue(g.make_move('d3','d3')) #red passes

        #prep moves to kill the cannon in future
        self.assertTrue(g.make_move('g7','g6')) #blue soldier moves
        self.assertTrue(g.make_move('f4','g4')) #red soldier moves sideways
        self.assertTrue(g.make_move('f6','f5')) #blue soldier moves
        self.assertTrue(g.make_move('g4','g5')) #red soldier moves
        self.assertTrue(g.make_move('g8','f6')) #blue horse moves
        self.assertTrue(g.make_move('e2','e2')) #red passes
        self.assertTrue(g.make_move('f6','d5')) #blue horse moves
        self.assertTrue(g.make_move('b3','e3')) #red CHECKS blue using a cannon -- special test for checks using a cannon -- check here
        
        try:
            self.assertEqual(g.get_game_state().upper(),'UNFINISHED')
        except:
            self.fail("Game state should be UNFINISHED when a general is in check but not checkmated")

        try:
            self.assertIs(g.is_in_check('red'), False)
        except:
            self.fail("Red General is not in check and yet is_in_check returns True for red")

        try:
            self.assertIs(g.is_in_check('blue'), True)
        except:
            self.fail("Blue General is in check with a Cannon outside the palace and is_in_check should return True for blue")

        counter_check_move = g.make_move('d5','e3') #evade the cannon check by capturing the cannon using a horse
        self.assertTrue(counter_check_move)
        
        try:
            self.assertIs(g.is_in_check('red'), False)
        except:
            self.fail("Red General is not in check and yet is_in_check returns True for red")

        try:
            self.assertIs(g.is_in_check('blue'), False)
        except:
            self.fail("Countering of the check by cannon by capturing it should be detected correctly and is_in_check should return False for blue")

        try:
            self.assertEqual(g.get_game_state().upper(),'UNFINISHED')
        except:
            self.fail("Game state should be UNFINISHED when a general is in check but not checkmated")

#    @visibility('after_due_date')
    def test_that_countering_the_check_by_blocking_the_cannon_is_detected_correctly(self):
        """RULES: Countering the check by blocking the cannon is detected correctly"""
        g = JanggiGame()
        
        g.make_move('c7','c6') #blue
        g.make_move('c1','d3') #red
        g.make_move('b10','d7') #blue
        g.make_move('b3','b3') #red passes
        g.make_move('c10','d8')
        g.make_move('h1','g3')
        g.make_move('e7','e6')
        g.make_move('b3','b3') #red passes
        g.make_move('e6', 'f6') #blue soldier moves sidewways
        g.make_move('b3','b3') #red passes
        g.make_move('h8','c8') #blue cannon moves -- check here
        g.make_move('d3','e5') #red
        g.make_move('c8','c4') #blue cannon captures red soldier -- check here
        g.make_move('e5','c4') #red horse captures blue cannon
        g.make_move('i10','i8') #blue chariot moves
        g.make_move('g4','f4')
        g.make_move('i8','f8') #blue chariot moves sideway
        g.make_move('g3','h5')
        g.make_move('h10','g8') #blue horse
        g.make_move('d1','d2') #red moves
        g.make_move('e9','e9') #blue passes
        g.make_move('d2','d3') #red moves
        g.make_move('e9','e9') #blue passes
        self.assertTrue(g.make_move('b3','e3')) #red CHECKS blue using a cannon -- special test for checks using a cannon -- check here
        
        try:
            self.assertEqual(g.get_game_state().upper(),'UNFINISHED')
        except:
            self.fail("Game state should be UNFINISHED when a general is in check but not checkmated")

        try:
            self.assertIs(g.is_in_check('red'), False)
        except:
            self.fail("Red General is not in check and yet is_in_check returns True for red")

        try:
            self.assertIs(g.is_in_check('blue'), True)
        except:
            self.fail("Blue General is in check with a Cannon outside the palace and is_in_check should return True for blue")

        counter_check_move = g.make_move('f8','e8') #evade the cannon check by blocking the cannon using the chariot
        self.assertTrue(counter_check_move)
        
        try:
            self.assertIs(g.is_in_check('red'), False)
        except:
            self.fail("Red General is not in check and yet is_in_check returns True for red")

        try:
            self.assertIs(g.is_in_check('blue'), False)
        except:
            self.fail("Countering of the check by cannon by blocking it should be detected correctly and is_in_check should return False for blue")

        try:
            self.assertEqual(g.get_game_state().upper(),'UNFINISHED')
        except:
            self.fail("Game state should be UNFINISHED when a general is in check but not checkmated")

#    @visibility('after_due_date')
    def test_that_check_forces_a_move_to_be_made_to_counter_the_check(self):
        """RULES:  Check forces a move to be made to counter the check"""
        g = JanggiGame()
        
        g.make_move('c7','c6') #blue
        g.make_move('c1','d3') #red
        g.make_move('b10','d7') #blue
        g.make_move('b3','b3') #red passes
        g.make_move('c10','d8')
        g.make_move('h1','g3')
        g.make_move('e7','e6')
        g.make_move('b3','b3') #red passes
        g.make_move('e6', 'f6') #blue soldier moves sidewways
        g.make_move('b3','b3') #red passes
        g.make_move('h8','c8') #blue cannon moves -- check here
        g.make_move('d3','e5') #red
        g.make_move('c8','c4') #blue cannon captures red soldier -- check here
        g.make_move('e5','c4') #red horse captures blue cannon
        g.make_move('i10','i8') #blue chariot moves
        g.make_move('g4','f4')
        g.make_move('i8','f8') #blue chariot moves sideway
        g.make_move('g3','h5')
        g.make_move('h10','g8') #blue horse
        g.make_move('d1','d2') #red moves
        g.make_move('e9','e9') #blue passes
        g.make_move('d2','d3') #red moves
        g.make_move('e9','e9') #blue passes
        self.assertTrue(g.make_move('b3','e3')) #red CHECKS blue using a cannon -- special test for checks using a cannon -- check here
        
        try:
            self.assertEqual(g.get_game_state().upper(),'UNFINISHED')
        except:
            self.fail("Game state should be UNFINISHED when a general is in check but not checkmated")

        try:
            self.assertIs(g.is_in_check('red'), False)
        except:
            self.fail("Red General is not in check and yet is_in_check returns True for red")

        try:
            self.assertIs(g.is_in_check('blue'), True)
        except:
            self.fail("Blue General is in check with a Cannon outside the palace and is_in_check should return True for blue")

        non_counter_check_move = g.make_move('f8','f7') #a move that does not evade the check
        try:
            self.assertFalse(non_counter_check_move)
        except:
            self.fail("Blue should be forced to make a move that evades a check when checked")
        
        non_counter_check_move = g.make_move('e9','e10') #general moves not countering the check
        try:
            self.assertFalse(non_counter_check_move)
        except:
            self.fail("Blue should be forced to make a move that evades a check when checked")

        non_counter_check_move = g.make_move('f6','f5') #soldier moves not countering the check
        try:
            self.assertFalse(non_counter_check_move)
        except:
            self.fail("Blue should be forced to make a move that evades a check when checked")


#    @visibility('after_due_date')
    def test_red_won(self):
        """RULES: Test that red win is detected correctly."""
        g = JanggiGame()
        
        g.make_move('c7','c6') #blue
        g.make_move('c1','d3') #red
        g.make_move('b10','d7') #blue
        g.make_move('b3','e3') #red
        g.make_move('c10','d8')
        g.make_move('h1','g3')
        g.make_move('e7','e6')
        g.make_move('e3', 'e6') #red cannon captures soldier -- check here

        g.make_move('h8','c8') #blue moves -- check here
        g.make_move('d3','e5') #red
        g.make_move('c8','c4') #blue cannon captures red soldier -- check here
        g.make_move('e5','c4') #red horse captures blue cannon
        g.make_move('i10','i8') #blue chariot moves
        g.make_move('g4','f4')
        g.make_move('i8','f8') #blue chariot moves sideway
        g.make_move('g3','h5')
        g.make_move('h10','g8') #blue horse
        g.make_move('e6','e3') #red CHECKS blue using a cannon -- special test for checks using a cannon -- check here
        
        g.make_move('e9','d9') #blue moves 
        g.make_move('c4','e5') #red
        g.make_move('c6','d6')
        g.make_move('e5','c4')
        g.make_move('a7','a6')#blue
        g.make_move('h3', 'h9') #red cannon moves to a position where it COULD Check but has not. -- check here
        g.make_move('a10','a7')
        g.make_move('c4','d6') #red horse captures blue soldier
        g.make_move('a6','b6')
        g.make_move('h5','g7')
        g.make_move('b8','b1')#blue cannon captures red elephant
        g.make_move('a1','b1') #red chariot captures blue cannon
        g.make_move('a7','a4')
        g.make_move('b1','c1')
        g.make_move('a4','a2') #blue CHECKS red using a chariot -- check here
        
        g.make_move('e2','e1') #red general moves to avoid capture -- check after this

        g.make_move('i7','h7') #blue moves
        g.make_move('c1','c9') #red chariot moves to the palace to CHECKMATE blue
    
        try:
            self.assertIs(g.is_in_check('red'), False)
        except:
            self.fail("Red General is not in check and yet is_in_check returns True for red")

        try:
            self.assertIs(g.is_in_check('blue'), True)
        except:
            self.fail("Blue General is in check and is_in_check should return True for blue")
        
        try:
            self.assertEqual(g.get_game_state().upper(),'RED_WON')
        except:
            self.fail("Game state should be RED_WON when the BLUE general is checkmated")

