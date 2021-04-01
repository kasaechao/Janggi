import pygame as p
from pygame.locals import *
import os, sys
import JanggiGame


class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self._size = self._width, self._height = 450, 503
        self._game = JanggiGame.JanggiGame()
        self._loc_selected = ()  # record last user click
        self._player_clicks = []  # track the user clicks
        self._img_size = 50
        self._board_surf = p.transform.scale(self._game.get_board().get_board_img(),
                                             self._game.get_board().get_board_size())

    def on_init(self):
        p.init()
        self._display_surf = p.display.set_mode(self._size)
        self._running = True
        red_player = self._game.get_red_player()
        blue_player = self._game.get_blue_player()
        board = self._game.get_board()

        # place pieces on the board
        red_pieces = self._game.get_red_player().get_player_pieces()
        blue_pieces = self._game.get_blue_player().get_player_pieces()
        # draw board onto screen first, then draw pieces onto screen
        self._display_surf.blit(self._board_surf, (0, 0))

        for i, piece in enumerate(red_pieces):
            board.set_board(red_player.get_initial_placements()[i], piece)
            piece.set_location(red_player.get_initial_placements()[i])
            pix_loc = board.coord_to_pix(piece.get_location())
            self._display_surf.blit(piece.get_image(), pix_loc)
        for i, piece in enumerate(blue_pieces):
            board.set_board(blue_player.get_initial_placements()[i], piece)
            piece.set_location(blue_player.get_initial_placements()[i])
            pix_loc = board.coord_to_pix(piece.get_location())
            self._display_surf.blit(piece.get_image(), pix_loc)

        # draw board with pieces on screen
        return self._running

    def on_event(self, event):
        if event.type == p.QUIT:
            self._running = False
        elif event.type == p.MOUSEBUTTONDOWN:
            mouse_pos = p.mouse.get_pos()  # returns (col, row), remember that we have to use (row, col)
            col = mouse_pos[0] // self._img_size
            row = mouse_pos[1] // self._img_size
            self._loc_selected = (row, col)
            print(self._loc_selected, self._game.get_board().get_board()[self._loc_selected[0]][self._loc_selected[1]])
            self._player_clicks.append(self._loc_selected)
            print(self._player_clicks)

            if len(self._player_clicks) == 2:
                curr = self._player_clicks[0]
                dest = self._player_clicks[1]
                if self._game.make_move(curr, dest) is True:
                    piece = self._game.get_board().get_board()[self._player_clicks[0][0]][self._player_clicks[0][1]]
                    print(piece)
                    self._loc_selected = ()
                    self._player_clicks = []

                    self._display_surf = p.display.set_mode(self._size)
                    self._running = True
                    board = self._game.get_board()

                    # place pieces on the board
                    red_pieces = self._game.get_red_player().get_player_pieces()
                    blue_pieces = self._game.get_blue_player().get_player_pieces()

                    # draw board onto screen first, then draw pieces onto screen
                    self._display_surf.blit(self._board_surf, (0, 0))

                    for i, piece in enumerate(red_pieces):
                        if piece.get_state() != 'inactive':
                            pix_loc = board.coord_to_pix(piece.get_location())
                            self._display_surf.blit(piece.get_image(), pix_loc)
                    for i, piece in enumerate(blue_pieces):
                        if piece.get_state() != 'inactive':
                            pix_loc = board.coord_to_pix(piece.get_location())
                            self._display_surf.blit(piece.get_image(), pix_loc)
                    self._game.get_board().display_board()

                else:
                    self._loc_selected = ()
                    self._player_clicks = []

    def on_loop(self):
        pass

    def on_render(self):
        p.display.update()

    def on_cleanup(self):
        p.quit()

    def on_execute(self):
        if self.on_init() is False:
            self._running = False
        while self._running:
            for event in p.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()


if __name__ == '__main__':
    theApp = App()
    theApp.on_execute()
