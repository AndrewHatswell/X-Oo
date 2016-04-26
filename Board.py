table = [[" "] * 4 for i in range(4)]

def print_table(whole_table):
    for y in range(4):
        row = " "
        for x in range(4):
            if whole_table[x][y] != " ":
                row += "'" + whole_table[x][y] + "', "
            else:
                row += "' ', "
        print(row)
