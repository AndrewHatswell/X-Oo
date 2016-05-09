def blockOut(lastTile, table, TileClass, cross_piece, plus_piece, adjacent_piece, nonadjacent_piece):

    if lastTile == None:
        return True
    elif int(lastTile.piece_type) == 1:
        for x in [0, 1, 2, 3]:
            for y in [0, 1, 2, 3]:
                if table[x][y] == " ":
                    newTile = TileClass(x, y)
                    if cross_piece(newTile, lastTile):
                        return True
        return False
    elif int(lastTile.piece_type) == 2:
        for x in [0, 1, 2, 3]:
            for y in [0, 1, 2, 3]:
                if table[x][y] == " ":
                    newTile = TileClass(x, y)
                    if plus_piece(newTile, lastTile):
                        return True
        return False
    elif int(lastTile.piece_type) == 3:
        for x in [0, 1, 2, 3]:
            for y in [0, 1, 2, 3]:
                if table[x][y] == " ":
                    newTile = TileClass(x, y)
                    if adjacent_piece(newTile, lastTile):
                        return True
        return False
    elif int(lastTile.piece_type) == 4:
        for x in [0, 1, 2, 3]:
            for y in [0, 1, 2, 3]:
                if table[x][y] == " ":
                    newTile = TileClass(x, y)
                    if nonadjacent_piece(newTile, lastTile):
                        return True
        return False
    else:
        return False

