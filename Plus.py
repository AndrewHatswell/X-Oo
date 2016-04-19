from check import *

#def plus_piece(tile, last_tile):
#    tile == check_up(last_tile)
#    tile == check_right(last_tile)
#    tile == check_down(last_tile)
#    tile == check_left(last_tile)

def plus_piece(last_tile, tile):
    x = 1
    if tile == (last_tile-(x*1)) or tile == (last_tile+(x*1)) or tile == (last_tile-(x*4)) or tile == (last_tile+(x*4)):
        return True
    elif x <= 3:
        x += 1
    else:
        return False
