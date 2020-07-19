# sudoku

Sbox = [[0, 0, 6, 8, 0, 2, 9, 0, 7],
        [1, 0, 0, 9, 0, 4, 0, 0, 0],
        [2, 0, 0, 7, 0, 0, 0, 5, 0],
        [0, 3, 1, 0, 0, 8, 7, 0, 2],
        [9, 6, 0, 0, 7, 0, 0, 8, 0],
        [7, 2, 0, 0, 0, 5, 0, 4, 0],
        [0, 0, 2, 4, 0, 0, 0, 0, 5],
        [0, 1, 0, 0, 2, 9, 8, 0, 4],
        [6, 0, 0, 1, 8, 0, 0, 0, 0]]


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


def is_full(s_box):
    for i in range(9):
        for j in range(9):
            if s_box[i][j] == 0:
                return False
    return True

def is_valid(s,i,j,k):
    for a in range(9):
        if s[i][a] == k or s[a][j] == k:
            return False
    qi = i//3
    qj = j//3
    for a in range(qi*3,qi*3+3):
        for b in range(qj*3, qj*3+3):
            if s[a][b] == k:
                return False
    return True


def find_nonempty(s):
    for i in range(9):
        for j in range(9):
            if s[i][j] == 0:
                return (i,j)
    print("error in find_nonempty")

def solve(s):
    if is_full(s):
        return True
    else:
        (i,j)=find_nonempty(s)
    for k in range(1,10):
        if is_valid(s,i,j,k):
            s[i][j] = k
            if solve(s):
                return True
    return False


#print(is_valid(Sbox, 1,7,9))
#output = is_full(Sbox)
output = find_nonempty(Sbox)

print (output)