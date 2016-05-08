def blockOut(lastTile, table, TileClass, cross_piece, plus_piece, adjacent_piece, nonadjacent_piece):
    if lastTile == 1:
        for x in [0, 1, 2, 3]:
            for y in [0, 1, 2, 3]:
                if table[x][y] == " ":
                    newTile = TileClass(x, y)
                    print "table check"
                    if cross_piece(newTile, lastTile):
                        print "cross check"
                        return True
        return False
    elif lastTile == 2:
        for x in [0, 1, 2, 3]:
            for y in [0, 1, 2, 3]:
                if table[x][y] == " ":
                    newTile = TileClass(x, y)
                    if plus_piece(newTile, lastTile):
                        return True
        return False
    elif lastTile == 3:
        for x in [0, 1, 2, 3]:
            for y in [0, 1, 2, 3]:
                if table[x][y] == " ":
                    newTile = TileClass(x, y)
                    if adjacent_piece(newTile, lastTile):
                        return True
        return False
    elif lastTile == 4:
        for x in [0, 1, 2, 3]:
            for y in [0, 1, 2, 3]:
                if table[x][y] == " ":
                    newTile = TileClass(x, y)
                    if nonadjacent_piece(newTile, lastTile):
                        return True
        return False
    else:
        return False
