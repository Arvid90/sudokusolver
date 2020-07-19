# sudoku

Sbox = [[1, 2, 3, 3, 5, 6, 7, 8, 0],
        [2, 0, 0, 0, 0, 0, 0, 0, 0],
        [3, 0, 3, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]]


def test_row(row, guess):
    for i in range(9):
        print("guess: ", guess, "pos: ", Sbox[row][i])
        if guess == Sbox[row][i]:
            print("collision")
            return False
    print("possibruh")
    return True


def test_column(column, guess):
    for i in range(9):
        print("Guess: ", guess, "At pos: ", Sbox[i][column])
        if guess == Sbox[i][column]:
            print("collision")
            return False
    print("possibruh")
    return True


def test_subsquare(row, col, guess):
    #solve with math instead of branching?
    if row < 3:
        #1
    elif row < 6:
        ##2
    else:
        #3

#        def test_next

#print("testing col ", Sbox[][0])
test_col = [0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in range(9):
    test_col[i] = Sbox[i][0]
print("testing column: ", test_col)
test_column(0, 4)
#for guess in range(9):
#    print("testing guess: ", guess+1)
#    test_row(0, guess+1)
