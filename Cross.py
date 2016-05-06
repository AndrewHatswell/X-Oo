def cross_piece(tile, lastTile):
    if abs(lastTile.x - tile.x) == abs(lastTile.y - tile.y):
        return True
    else:
        return False

#def cross_piece(CurrentTile, LastTile):
#    z = 1
#    while z <= 3:
#        if (CurrentTile.x == LastTile.x-z) and (CurrentTile.y == LastTile.y-z)\
#                or (CurrentTile.x == LastTile.x+z) and (CurrentTile.y == LastTile.y+z)\
#                or (CurrentTile.x == LastTile.x-z) and (CurrentTile.y == LastTile.y+z)\
#                or (CurrentTile.x == LastTile.x+z) and (CurrentTile.y == LastTile.y-z):
#            return True
#        elif z <= 3:
#            z += 1
#        else:
#            return False
