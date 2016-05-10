def scoring(table, tile):
    #vertical
    seq = []
    for x in [0, 1, 2, 3]:
        for y in [0, 1, 2, 3]:
            tile = table[x][y]
            seq.append(tile)
            print seq