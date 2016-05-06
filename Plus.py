def plus_piece(Tile, LastTile):
    if (Tile.x == LastTile.x) or (Tile.y == LastTile.y):
        return True
    else:
        return False