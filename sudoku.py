#sudoku



Sbox = [[1, 2, 3, 4, 5, 6, 7, 8, 0],
        [2, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]]

def test_row(row, guess):
    for i in range(9):
        print("guess: ", guess, "pos: ", Sbox[row][i])
        if guess==Sbox[i][row]:
            return False
        return True

#        def test_collumn(index, guess)
#        def test_subsquare(index, guess)
#        def test_nextsquare

#print("testing row ", Sbox[0])
#for guess in range(9):
#    print("testing guess ", guess)
    if (test_row(0, guess)):
        print ("possibruh")
    else:
        print("collision")
