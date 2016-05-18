class scores:
    pl_score = 0
    p2_score = 0


def scoring(table, tile, scores):
    #vertical
    seq = []
    for x in [0, 1, 2, 3]:
        for y in [0, 1, 2, 3]:
            tile = table[x][y]
            player = tile.player
            seq.append(player)
            print seq
            seq = []