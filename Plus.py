def plus_piece(last_tile, tile):
    x = 1
    while x <= 3:
        if tile == (last_tile-(x*1)) or tile == (last_tile+(x*1)) or tile == (last_tile-(x*4)) or tile == (last_tile+(x*4)):
            return True
        elif x <= 3:
            x += 1
        else:
            return False

def plus_piece(CurrentTile, LastTile):
    z = 1
    while z <= 3:
        if (CurrentTile.x == LastTile.x-z)\
                or (CurrentTile.x == LastTile.x+z)\
                or (CurrentTile.y == LastTile.y-z)\
                or (CurrentTile.y == LastTile.y+z):
            return True
        elif z <= 3:
            z += 1
        else:
            return False