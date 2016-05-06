from colorama import *

def make_pieces(Tile):
    if Tile.piece_type == "0":
            return " "

    if Tile.player == 1:
        if Tile.piece_type == "1":
            return Fore.BLUE + "X" + Fore.RESET
        elif Tile.piece_type == "2":
            return Fore.BLUE + "+" + Fore.RESET
        elif Tile.piece_type == "3":
            return Fore.BLUE + "o" + Fore.RESET
        elif Tile.piece_type == "4":
            return Fore.BLUE + "O" + Fore.RESET
        else:
            return

    if Tile.player == 2:
        if Tile.piece_type == "1":
            return Fore.RED + "X" + Fore.RESET
        elif Tile.piece_type == "2":
            return Fore.RED + "+" + Fore.RESET
        elif Tile.piece_type == "3":
            return Fore.RED + "o" + Fore.RESET
        elif Tile.piece_type == "4":
            return Fore.RED + "O" + Fore.RESET
        else:
            return

#def place_piece(table, x, y, piece, player):
#    if player == 1:
#        table[x][y] = Fore.RED + make_pieces(piece) + Fore.RESET
#    if player == 2:
#        table[x][y] = Fore.BLUE + make_pieces(piece) + Fore.RESET

#place_piece(table, x, y, make_pieces(piece), piece, player)