def adjacent_piece(CurrentTile, LastTile):
    if abs(CurrentTile.x) == abs(LastTile.x - 1) and abs(CurrentTile.y) == abs(LastTile.y - 1):
        return True
    else:
        return False