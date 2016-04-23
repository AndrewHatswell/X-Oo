def nonadjacent_piece(CurrentTile, LastTile):
    if abs(CurrentTile.x) == abs(LastTile.x - 1) and abs(CurrentTile.y) == abs(LastTile.y - 1):
        return False
    else:
        return True





#    if tile == (last_tile - 5) or tile == (last_tile - 4) or tile == (last_tile -3) or tile == (last_tile - 1) or \
#            tile == (last_tile + 1) or tile == (last_tile + 3) or tile == (last_tile + 4) or tile == (last_tile +5):
#        return False
#    else:
#        return True