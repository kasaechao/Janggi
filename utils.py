# Import Modules
import os
import pygame as pg

def convert_coord_Janggi(coord):
    row_key = {'a': 0, 'b': 60, 'c': 120, 'd': 180, 'e': 240, 'f': 300, 'g': 360, 'h': 420, 'i': 480}
    col_key = {'1': 0, '2': 60, '3': 120, '4': 180, '5': 240, '6': 200, '7': 360, '8': 420, '9': 480, '10': 540}

    pass

def convert_coord(coord, origin=(0,0)):
    """convert coord to pygame coord"""
    row_key = {'a': 0, 'b': 60, 'c': 120, 'd': 180, 'e': 240, 'f': 300, 'g': 360, 'h': 420, 'i': 480}
    col_key = {'1': 0, '2': 60, '3': 120, '4': 180, '5': 240, '6': 200, '7': 360, '8': 420, '9': 480, '10': 540}

    pg_coord = (row_key[coord[0]], col_key[coord[1:]])
    return pg_coord

def load_image(name, scale=1, colorkey=None):
  main_dir = os.path.split(os.path.abspath(__file__))[0]
  data_dir = os.path.join(main_dir, 'assets')
  fullname = os.path.join(data_dir, name)
  image = pg.image.load(fullname)

  size = image.get_size()
  size = (size[0] * scale, size[1] * scale)
  image = pg.transform.scale(image, size)

  image = image.convert()
  if colorkey is not None:
      if colorkey == -1:
          colorkey = image.get_at((0, 0))
      image.set_colorkey(colorkey, pg.RLEACCEL)
  return image, image.get_rect()