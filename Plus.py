def plus_piece(CurrentTile, LastTile):
    if (CurrentTile.x == LastTile.x) or (CurrentTile.y == LastTile.y):
        return True
    else:
        return False