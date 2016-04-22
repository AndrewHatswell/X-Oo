cross_count = 2
plus_count = 2
adjacent_count = 2
nonAdjacent_count = 2

class pieces_count:
    

def piece_count(last_piece, cross_count, plus_count, adjacent_count, nonAdjacent_count):

    if last_piece == 1:
        cross_count -= 1
        return cross_count
    elif last_piece == 2:
        plus_count -= 1
        return plus_count
    elif last_piece == 3:
        adjacent_count -= 1
        return adjacent_count
    elif last_piece == 4:
        nonAdjacent_count -= 1
        return nonAdjacent_count
    else:
        print ("You have ", cross_count, "X's, ", plus_count, "+'s, ", adjacent_count, "o's, ",\
               nonAdjacent_count, "O's")

    if cross_count == 0:
        print "You don't have any more X's"
    if plus_count == 0:
        print "You don't have any more +'s"
    if adjacent_count == 0:
        print "You don't have any more o's"
    if nonAdjacent_count == 0:
        print "You don't have any more O's"

    total = plus_count + cross_count + adjacent_count + nonAdjacent_count
    if total == 0:
        print "You have no pieces left"

    return total






