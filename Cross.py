def cross_piece(CurrentTile, LastTile):
    if abs(LastTile.x - CurrentTile.x) == abs(LastTile.y - CurrentTile.y):
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
