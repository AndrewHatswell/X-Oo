class number_of_pieces:
    cross_count = 2
    plus_count = 2
    adjacent_count = 2
    nonAdjacent_count = 2


def piece_count(last_piece, number_of_pieces):
    if last_piece == 1:
        number_of_pieces.cross_count -= 1
        return number_of_pieces.cross_count
    elif last_piece == 2:
        number_of_pieces.plus_count -= 1
        return number_of_pieces.plus_count
    elif last_piece == 3:
        number_of_pieces.adjacent_count -= 1
        return number_of_pieces.adjacent_count
    elif last_piece == 4:
        number_of_pieces.nonAdjacent_count -= 1
        return number_of_pieces.nonAdjacent_count
    else:
        return



#if number_of_pieces.cross_count > 0:
#else:
#print "You have no X's left!"
#if number_of_pieces.plus_count == 0:
#print "You have no +'s left!"
#else:
#if number_of_pieces.adjacent_count == 0:
#print "You have no o's left!"
#else:
#if number_of_pieces.nonAdjacent_count == 0:
#print "You have no O's left!"
#else: