def nonadjacent_piece(tile, lastTile):
    if tile.x == (lastTile.x - 1) and ((lastTile.y - 1) <= tile.y <= (lastTile.y + 1)) or \
            tile.x == (lastTile.x + 1) and ((lastTile.y - 1) <= tile.y <= (lastTile.y + 1)) or \
            tile.x == lastTile.x and ((lastTile.y - 1) <= tile.y <= (lastTile.y + 1)):
        return False
    else:
        return True
