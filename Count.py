class pieces:
    cross_count = 2
    plus_count = 2
    adjacent_count = 2
    nonAdjacent_count = 2


def piece_count(last_piece):
    if last_piece == 1:
        pieces.cross_count -= 1
        return pieces.cross_count
    elif last_piece == 2:
        pieces.plus_count -= 1
        return pieces.plus_count
    elif last_piece == 3:
        pieces.adjacent_count -= 1
        return pieces.adjacent_count
    elif last_piece == 4:
        pieces.nonAdjacent_count -= 1
        return pieces.nonAdjacent_count
    else:
        return



#if pieces.cross_count > 0:
#else:
#print "You have no X's left!"
#if pieces.plus_count == 0:
#print "You have no +'s left!"
#else:
#if pieces.adjacent_count == 0:
#print "You have no o's left!"
#else:
#if pieces.nonAdjacent_count == 0:
#print "You have no O's left!"
#else: