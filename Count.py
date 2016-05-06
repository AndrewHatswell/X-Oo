class number_of_pieces:
    cross_count_p1 = 2
    plus_count_p1 = 2
    adjacent_count_p1 = 2
    nonAdjacent_count_p1 = 2

    cross_count_p2 = 2
    plus_count_p2 = 2
    adjacent_count_p2 = 2
    nonAdjacent_count_p2 = 2

def piece_count(tile, last_piece, number_of_pieces):
    if tile.player == 1:
        if last_piece == 1:
            number_of_pieces.cross_count_p1 -= 1
            return number_of_pieces.cross_count_p1
        elif last_piece == 2:
            number_of_pieces.plus_count_p1 -= 1
            return number_of_pieces.plus_count_p1
        elif last_piece == 3:
            number_of_pieces.adjacent_count_p1 -= 1
            return number_of_pieces.adjacent_count_p1
        elif last_piece == 4:
            number_of_pieces.nonAdjacent_count_p1 -= 1
            return number_of_pieces.nonAdjacent_count_p1
        else:
            return
    if tile.player == 2:
        if last_piece == 1:
            number_of_pieces.cross_count_p2 -= 1
            return number_of_pieces.cross_count_p2
        elif last_piece == 2:
            number_of_pieces.plus_count_p2 -= 1
            return number_of_pieces.plus_count_p2
        elif last_piece == 3:
            number_of_pieces.adjacent_count_p2 -= 1
            return number_of_pieces.adjacent_count_p2
        elif last_piece == 4:
            number_of_pieces.nonAdjacent_count_p2 -= 1
            return number_of_pieces.nonAdjacent_count_p2
        else:
            return


def out_of_pieces(tile, number_of_pieces):
    if tile.player == 1:
        if int(tile.piece_type) == 1:
            if number_of_pieces.cross_count_p1 != 0:
                return True
            else:
                print "You don't have any X's left"
                return False
        elif int(tile.piece_type) == 2:
            if number_of_pieces.plus_count_p1 != 0:
                return True
            else:
                print "You don't have any +'s left"
                return False
        elif int(tile.piece_type) == 3:
            if number_of_pieces.plus_count_p1 != 0:
                return True
            else:
                print "You don't have any o's left"
                return False
        elif int(tile.piece_type) == 4:
            if number_of_pieces.plus_count_p1 != 0:
                return True
            else:
                print "You don't have any O's left"
                return False
        else:
            print "That is not a piece"
    if tile.player == 2:
        if int(tile.piece_type) == 1:
            if number_of_pieces.cross_count_p2 != 0:
                return True
            else:
                print "You don't have any X's left"
                return False
        elif int(tile.piece_type) == 2:
            if number_of_pieces.plus_count_p2 != 0:
                return True
            else:
                print "You don't have any +'s left"
                return False
        elif int(tile.piece_type) == 3:
            if number_of_pieces.plus_count_p2 != 0:
                return True
            else:
                print "You don't have any o's left"
                return False
        elif int(tile.piece_type) == 4:
            if number_of_pieces.plus_count_p2 != 0:
                return True
            else:
                print "You don't have any O's left"
                return False
        else:
            print "That is not a piece"