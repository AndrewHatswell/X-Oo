def adjacent_piece(Tile, LastTile):
    if Tile.x == (LastTile.x - 1) and ((LastTile.y - 1) <= Tile.y <= (LastTile.y + 1)) or \
            Tile.x == (LastTile.x + 1) and ((LastTile.y - 1) <= Tile.y <= (LastTile.y + 1)) or \
            Tile.x == LastTile.x and ((LastTile.y - 1) <= Tile.y <= (LastTile.y + 1)):
        return True
    else:
        return False