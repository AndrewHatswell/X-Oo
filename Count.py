class pieces:
    cross_count = 2
    plus_count = 2
    adjacent_count = 2
    nonAdjacent_count = 2


def piece_count(last_piece, piece_count):

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
        print ("You have ", pieces.cross_count, "X's, ", pieces.plus_count, "+'s, ",\
               pieces.adjacent_count, "o's, ", pieces.nonAdjacent_count, "O's")




