make_pieces = 0

def piece_count ():
    Plus_count = 2
    Cross_count = 2
    Adjacent_count = 2
    NonAdjacent_count = 2

    if make_pieces == 1:
        Cross_count -= 1
        return Cross_count
    elif make_pieces == 2:
        Plus_count -= 1
        return Plus_count
    elif make_pieces == 3:
        Adjacent_count -= 1
        return Adjacent_count
    elif make_pieces == 4:
        NonAdjacent_count -= 1
        return NonAdjacent_count
    else:
        return

    if Cross_count == 0:
        print "You don't have any more X's"
    if Plus_count == 0:
        print "You don't have any more +'s"
    if Adjacent_count == 0:
        print "You don't have any more o's"
    if NonAdjacent_count == 0:
        print "You don't have any more O's"

    total = Plus_count + Cross_count + Adjacent_count + NonAdjacent_count
    if total == 0:
        print "You have no more pieces"

    return total





