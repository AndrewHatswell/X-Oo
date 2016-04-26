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

def out_of_pieces(piece, number_of_pieces):
    if int(piece) == 1:
        if number_of_pieces.cross_count != 0:
            return True
        else:
            print "You don't have any X's left"
            return False
    elif int(piece) == 2:
        if number_of_pieces.plus_count != 0:
            return True
        else:
            print "You don't have any +'s left"
            return False
    elif int(piece) == 3:
        if number_of_pieces.plus_count != 0:
            return True
        else:
            print "You don't have any o's left"
            return False
    elif int(piece) == 4:
        if number_of_pieces.plus_count != 0:
            return True
        else:
            print "You don't have any O's left"
            return False
    else:
        print "That is not a piece"

