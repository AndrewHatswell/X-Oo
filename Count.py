class number_of_pieces:
    cross_count = 2
    plus_count = 2
    adjacent_count = 2
    nonAdjacent_count = 2

<<<<<<< HEAD
=======
class pieces_count:
    

def piece_count(last_piece, cross_count, plus_count, adjacent_count, nonAdjacent_count):
>>>>>>> master

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
<<<<<<< HEAD
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
=======
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






>>>>>>> master
