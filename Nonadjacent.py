def nonadjacent_piece(CurrentTile, LastTile):
    if CurrentTile.x == (LastTile.x - 1) and ((LastTile.y - 1) <= CurrentTile.y <= (LastTile.y + 1)) or \
            CurrentTile.x == (LastTile.x + 1) and ((LastTile.y - 1) <= CurrentTile.y <= (LastTile.y + 1)) or \
            CurrentTile.x == LastTile.x and ((LastTile.y - 1) <= CurrentTile.y <= (LastTile.y + 1)):
        return False
    else:
        return True
