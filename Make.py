

def make_pieces(number):
    if (number == "0"):
        return " "
    elif (number == "1"):
        return "X"
    elif (number == "2"):
        return "+"
    elif (number == "3"):
        return "o"
    elif (number == "4"):
        return "O"
    else:
        return

class Piece_Type:
    def __init__(self, Player, piece):
        self.player = Player
        self.piece = piece
