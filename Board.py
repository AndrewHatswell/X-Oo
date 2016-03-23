table = [[" "] * 4 for i in range(4)]

def print_table(whole_table):
    for row in whole_table:
        print row

print_table(table)
# 0 = empty
# 1 = X
# 2 = +
# 3 + o
# 4 = O

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

print "Type in the number of the peice you want to select: '\n 1 = X \n 2 = + \n 3 = o \n 4 = O"
print "Type the coordinates (originating from the top left) of the box you want to put your piece into in the format \'x y\' (e.g. 4 2)"
piece = raw_input('\n'"Choose your piece: ")
move = raw_input("Choose where you want to go: ")

if len(move) == 3:
    if 1 <= int(move[0]) <= 4 and 1 <= int(move[2]) <= 4: #Check the user has entered valid coordinates
        if table[int(move[0]) - 1][int(move[2]) -1] == " ": #Check the box is empty
            table[int(move[0]) - 1][int(move[2]) -1] = make_pieces(piece) #Places the piece in chosen spot
            print_table(table)
        else:
            print "You can't do that1!"
else:
    print "You can't do that!"