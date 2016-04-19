def check_up(last_tile, tile):
    if tile != 1 or 2 or 3 or 4:
        tile - 4
    else:
        clear = False
        print "You can't make that move"

def check_up_right(last_tile):
    if last_tile != 1 or 2 or 3 or 4 or 8 or 12 or 16:
        last_tile -= 3
    else:
        clear = False
        print "You can't make that move"

def check_right(last_tile):
    if last_tile != 4 or 8 or 12 or 16:
        last_tile += 1
    else:
        clear = False
        print "You can't make that move"

def check_down_right(last_tile):
    if last_tile != 4 or 8 or 12 or 13 or 14 or 15 or 16:
        last_tile += 5
    else:
        clear = False
        print "You can't make that move"

def check_down(last_tile):
    if last_tile != 13 or 14 or 15 or 16:
        last_tile + 4
    else:
        clear = False
        print  "You can't make that move"

def check_down_left(last_tile):
    if last_tile != 1 or 5 or 9 or 13 or 14 or 15 or 16:
        last_tile += 3

def check_left(last_tile):
    if last_tile != 1 or 5 or 9 or 13:
        last_tile -= 1
    else:
        clear = False
        print "You can't make that move"

def check_up_left(last_tile):
    if last_tile != 1 or 2 or 3 or 4 or 5 or 9 or 13:
        last_tile -= 5
    else:
        clear = False
        print "You can't make that move"
