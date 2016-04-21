def cross_piece(last_tile, tile):
    x = 1
    while x <= 3:
        if tile == (last_tile-(x*3)) or tile == (last_tile+(x*3)) or tile == (last_tile-(x*5)) or tile == (last_tile+(x*5)):
            return True
        elif x <= 3:
            x += 1
        else:
            return False
