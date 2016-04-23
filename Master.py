from Count import *
from Board import *
from Tile import *
from Cross import *
from Plus import *
from Adjacent import *
from Nonadjacent import *
from Make import *



print_table(table)
last_piece = None

while piece_count > 0:

    print "Type in the number of the piece you want to select: '\n 1 = X \n 2 = + \n 3 = o \n 4 = O"
    print "Type the coordinates (originating from the top left of the box) where you want to put your piece " \
          "into in the format \'x y\' (e.g. 4 2)"
    piece = raw_input('\n'"Choose your piece: ")
    move = raw_input("Choose where you want to go: ")

    x = int(move[0]) - 1
    y = int(move[2]) - 1
    CurrentTile = Tile(x, y)
    place_last_piece = False

    if len(move) == 3:
        if last_piece == None:
            if 0 <= x <= 3 and 0 <= y <= 3: #Check the user has entered valid coordinates
                if table[x][y] == " ": #Check the box is empty
                    table[x][y] = make_pieces(piece) #Places the piece in chosen spot
                    print_table(table)
                    place_last_piece = True
        else:
            if 0 <= x <= 3 and 0 <= y <= 3: #Check the user has entered valid coordinates
                if table[x][y] == " ": #Check the box is empty
                    if last_piece == 1: # Check the last piece is an X
                        if cross_piece(CurrentTile, LastTile) == True: # Check current piece abides by last piece rules
                            table[x][y] = make_pieces(piece) # Places the piece in chosen spot
                            print_table(table)
                            place_last_piece = True
                        else:
                            print "You can not make that move as it is not in X's limit"
                    elif last_piece == 2:
                        if plus_piece(CurrentTile, LastTile) == True: # Check current piece abides by last piece rules
                            table[x][y] = make_pieces(piece) #Places the piece in chosen spot
                            print_table(table)
                            place_last_piece = True
                        else:
                            print "You can not make that move as it is not in +'s limit"
                    elif last_piece == 3:
                        if adjacent_piece(CurrentTile, LastTile) == True: # Check current piece abides by last piece rules
                            table[x][y] = make_pieces(piece)
                            print_table(table)
                            place_last_piece = True
                        else:
                            print "You can not make that move as it is not in o's limit"
                    elif last_piece == 4:
                        if nonadjacent_piece(CurrentTile, LastTile) == True: # Check current piece abides by last piece rules
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
        LastTile = Tile(x,y)
        piece_count(last_piece, number_of_pieces)
        print number_of_pieces.cross_count
