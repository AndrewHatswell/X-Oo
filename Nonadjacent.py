#def nonadjacent_piece(last_tile, tile):
#    if tile == (last_tile - 5) or (last_tile - 4) or (last_tile -3) or (last_tile - 1) or (last_tile + 1) or (last_tile + 3) or (last_tile + 4) or (last_tile +5):
#        clear = False
#        print "You can't make that move"

def nonadjacent_piece(last_tile, tile):
    if tile == (last_tile - 5) or tile == (last_tile - 4) or tile == (last_tile -3) or tile == (last_tile - 1) or \
            tile == (last_tile + 1) or tile == (last_tile + 3) or tile == (last_tile + 4) or tile == (last_tile +5):
        return True
    else:
        return False