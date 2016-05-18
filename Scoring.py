class scores:
    pl_score = 0
    p2_score = 0


def scoring(table, tile, scores):
    #vertical
    seq = []
    for tile.x in [0, 1, 2, 3]:
        for tile.y in [0, 1, 2, 3]:
            player = tile.player
            seq.append(player)
            print seq