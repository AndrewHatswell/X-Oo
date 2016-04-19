from check import *

#def cross_piece(tile, last_tile):
#    tile = check_up_right(last_tile)
#    tile = check_down_right(last_tile)
#    tile = check_down_left(last_tile)
#    tile = check_up_left(last_tile)

def cross_piece(last_tile, tile):
    x = 1
    if tile == (last_tile-(x*3)) or tile == (last_tile+(x*3)) or tile == (last_tile-(x*5)) or tile == (last_tile+(x*5)):
        return True
    elif x <= 3:
        x += 1
    else:
        return False
