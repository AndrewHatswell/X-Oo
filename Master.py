from Count import *
from Board import *
from Tile_Numbers import *
from Cross import *
from Plus import *
from Adjacent import *
from Nonadjacent import *
from Make import *



print_table(table)
last_piece = None
turn = 0


while piece_count > 0:

    print "Type in the number of the peice you want to select: '\n 1 = X \n 2 = + \n 3 = o \n 4 = O"
    print "Type the coordinates (originating from the top left of the box) where you want to put your piece " \
          "into in the format \'x y\' (e.g. 4 2)"
    piece = raw_input('\n'"Choose your piece: ")
    move = raw_input("Choose where you want to go: ")

    y = int(move[0]) - 1
    x = int(move[2]) - 1
    tiles(x +1, y + 1)
    tile = tiles(x +1, y + 1)
    place_last_piece = False

    if len(move) == 3:
        if last_piece == None:
            if 1 <= tile <= 16: #Check the user has entered valid coordinates
                if table[x][y] == " ": #Check the box is empty
                    table[x][y] = make_pieces(piece) #Places the piece in chosen spot
                    print_table(table)
                    place_last_piece = True
        else:
            if 1 <= int(move[0]) <= 4 and 1 <= int(move[2]) <= 4: #Check the user has entered valid coordinates
                if table[x][y] == " ": #Check the box is empty
                    if last_piece == 1:
                        if cross_piece(last_tile, tile) == True:
                            table[x][y] = make_pieces(piece) #Places the piece in chosen spot
                            print_table(table)
                            place_last_piece = True
                        else:
                            print "You can not make that move as it is not in X's limit"
                    elif last_piece == 2:
                        if plus_piece(last_tile, tile) == True and pieces.plus_count > 0:
                            table[x][y] = make_pieces(piece) #Places the piece in chosen spot
                            print_table(table)
                            place_last_piece = True
                        else:
                            print "You can not make that move as it is not in +'s limit"
                    elif last_piece == 3:
                        if adjacent_piece(last_tile, tile) == True:
                            table[x][y] = make_pieces(piece)
                            print_table(table)
                            place_last_piece = True
                        else:
                            print "You can not make that move as it is not in o's limit"
                    elif last_piece == 4:
                        if nonadjacent_piece(last_tile, tile) == True:
                            table[x][y] = make_pieces(piece) #Places the piece in chosen spot
                            print_table(table)
                            place_last_piece = True
                        else:
                            print "You can not make that move as it is not in O's limit"
                    else:
                        print_table(table)
                        print ("You can't do that!11")
                        continue
                else:
                    print "You can't do that as the space is not empty!"
                    print_table(table)
    else:
        print "You can't do that! You have selected an incorrect piece or place on the board!"

    if place_last_piece:
        last_piece = int(piece)
        last_tile = tile
        turn += 1
        piece_count(last_piece, pieces)
        print pieces.cross_count


