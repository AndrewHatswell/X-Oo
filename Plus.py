def plus_piece(last_tile, tile):
    x = 1
    while x <= 3:
        if tile == (last_tile-(x*1)) or tile == (last_tile+(x*1)) or tile == (last_tile-(x*4)) or tile == (last_tile+(x*4)):
            return True
        elif x <= 3:
            x += 1
        else:
            return False
