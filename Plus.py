def plus_piece(tile, lastTile):
    if (tile.x == lastTile.x) or (tile.y == lastTile.y):
        return True
    else:
        return False