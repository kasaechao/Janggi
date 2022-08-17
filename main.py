import pygame, sys, os, utils
from pygame.locals import *
import JanggiGame

 
class App:
  def __init__(self):
    self._game = None
    self._title = "Janggi"
    self._running = True
    self._display_surf = None
    self.size = self.width, self.height = 800, 600
    self._red_player_moves, self._blue_player_moves = [], [] # stack will record all moves
    
  def on_init(self):
    pygame.init()
    self._game = JanggiGame.JanggiGame()
    
    # component sizing
    # 60 x 60 unit sized squares (0, 0) sits at (151, 31)
    board_scale = 0.6
    piece_size = board_scale * 1

    self._display_surf = pygame.display.set_mode(self.size)
    pygame.display.set_caption(self._title)
    
    # load game components
    board_surf_img, board_rect = self._game.get_board().set_image(utils.load_image('JanggiWood.svg', board_scale, (0,0,0)))
    print('board size is ', board_rect.size)
    square_size = (630 - 150) // 8, (570 - 30) // 9
    print(' each square is ', square_size)

    # load the blue and red pieces
    for key, value in self._game.get_blue_player().get_pieces().items():
      player_pieces = self._game.get_blue_player().get_pieces()
      player_pieces[key]['name'].set_image(utils.load_image(player_pieces[key]['name'].get_image_file(), piece_size, (0,0,0)))
      board_surf_img.blit(player_pieces[key]['name'].get_image()[0], utils.convert_coord(player_pieces[key]['initial_location'])) 

    for key, value in self._game.get_red_player().get_pieces().items():
      player_pieces = self._game.get_red_player().get_pieces()
      player_pieces[key]['name'].set_image(utils.load_image(player_pieces[key]['name'].get_image_file(), piece_size, (0,0,0)))
      board_surf_img.blit(player_pieces[key]['name'].get_image()[0], utils.convert_coord(player_pieces[key]['initial_location'])) 


    # define the background of the screen
    background = pygame.Surface(self._display_surf.get_size())
    background = background.convert()
    background.fill((170, 170, 170))
    background.blit(board_surf_img, (self.width * 0.15 , 0))

    self._display_surf.blit(background, (0,0))
    
    self._running = True

  def on_event(self, event):
    """events such as key presses and mouse clicks"""
    # print(event)
    if event.type == pygame.MOUSEBUTTONUP:
      print(pygame.mouse.get_pos())
    #   if self._game.get_turn() == 'blue':
    #     self._blue_player_moves.append(pygame.mouse.get_pos())
    #   else:
    #     self._red_player_moves.append(pygame.mouse.get_pos())

    if event.type == pygame.QUIT:
      self.running = False
      pygame.quit()
  
  def on_loop(self):
    """computes changes in the game: player moves, game score, AI moves"""
    # if len(self._blue_player_moves) >= 2 or len(self._red_player_moves) >= 2:
    #   if self._game.get_turn() == 'blue':
    #     self._game.make_move(self._blue_player_moves.pop(), self._blue_player_moves.pop())
    #   else:
    #     self._game.make_move(self._red_player_moves.pop(), self._red_player_moves.pop())


  def on_render(self):
    """prints out onto the screen"""
    # draw pieces onto board
    # draw board onto screen surface

    
    pygame.display.flip()

  def on_cleanup(self):
    pygame.quit()

  def on_execute(self):
    if self.on_init() == False:
      self._running = False

    while self._running:
      for event in pygame.event.get():
        self.on_event(event)
      self.on_loop()
      self.on_render()
    self.on_cleanup()
 
if __name__ == "__main__" :
  theApp = App()
  theApp.on_execute()