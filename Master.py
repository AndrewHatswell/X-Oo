from Count import *
from Board import *
from Tile import *
from Cross import *
from Plus import *
from Adjacent import *
from Nonadjacent import *
from Make import *
from BlockOut import *

first_turn = True
last_piece = None
player = 1

while number_of_pieces.p1 or number_of_pieces.p2 != 0:

    place_last_piece = False
    print_table(table)
    print "Type in the number of the piece you want to select: \n 1 = X \n 2 = + \n 3 = o \n 4 = O"
    print "Type the coordinates (originating from the top left of the box) where you want to put your piece " \
          "into in the format \'x y\' (e.g. 4 2)"

    try:
        piece_type = raw_input('\n'"Player " + str(player) + ": Choose your piece: ")

        try:
            move = raw_input("Choose where you want to go: ")

            if 1 <= int(move[0]) <= 4 and 1 <= int(move[2]) <= 4:
                x = int(move[0]) - 1
                y = int(move[2]) - 1
                tile = TileClass(x, y, piece_type, player)

                if out_of_pieces(tile, number_of_pieces):
                    if first_turn:
                        if 0 <= tile.x <= 3 and 0 <= tile.y <= 3: # Check the user has entered valid coordinates
                            if table[tile.x][tile.y] == " ": # Check the box is empty
                                table[tile.x][tile.y] = make_pieces(tile) # Places the piece in chosen spot
                                place_last_piece = True
                    else:
                        if 0 <= tile.x <= 3 and 0 <= tile.y <= 3: # Check the user has entered valid coordinates
                            if table[tile.x][tile.y] == " ": # Check the box is empty
                                if int(lastTile.piece_type) == 1: # Check the last piece is an X
                                    if cross_piece(tile, lastTile) == True: # Check current piece abides by last piece rules
                                        table[tile.x][tile.y] = make_pieces(tile) # Places the piece in chosen spot
                                        place_last_piece = True
                                    else:
                                        print "You can not make that move as it is not in X's limit"
                                elif int(lastTile.piece_type) == 2:
                                    if plus_piece(tile, lastTile) == True:
                                        table[tile.x][tile.y] = make_pieces(tile)
                                        place_last_piece = True
                                    else:
                                        print "You can not make that move as it is not in +'s limit"
                                elif int(lastTile.piece_type) == 3:
                                    if adjacent_piece(tile, lastTile) == True:
                                        table[tile.x][tile.y] = make_pieces(tile)
                                        place_last_piece = True
                                    else:
                                        print "You can not make that move as it is not in o's limit"
                                elif int(lastTile.piece_type) == 4:
                                    if nonadjacent_piece(tile, lastTile) == True:
                                        table[tile.x][tile.y] = make_pieces(tile)
                                        place_last_piece = True
                                    else:
                                        print "You can not make that move as it is not in O's limit"
                                else:
                                    print ("You can't do that!11")
                                    continue
                            else:
                                print "You can't do that as the space is not empty!"
            else:
                print "Invalid placement!"

            if place_last_piece:
                first_turn = False
                lastTile = tile
                piece_count(tile, number_of_pieces)
                if blockOut(lastTile, table, TileClass, cross_piece, plus_piece, adjacent_piece, nonadjacent_piece)\
                        and player == 1:
                    player = 2
                elif blockOut(lastTile, table, TileClass, cross_piece, plus_piece, adjacent_piece, nonadjacent_piece)\
                        and player == 2:
                    player = 1
                else:
                    print "You blocked out the other player! Go again"
        except ValueError:
            print "Invalid placement"
    except ValueError:
        print "Invalid piece"
