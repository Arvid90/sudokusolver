# sudoku
import matplotlib.pyplot as plt
import numpy as np


def sdraw(fig, ones, l):
    plt.clf()
    ax = fig.add_subplot(111)
    ax.matshow(ones)
    for i in range(9):
        for j in range(9):
            if int(l[i, j]) == 0:
                ax.text(i, j, " ", ha="center", va="center", color="w")
            else:
                ax.text(i, j, int(l[i, j]), ha="center", va="center", color="w")
    plt.draw()
    plt.pause(0.01)

#for i in range(0, N):
#    lattice[i][i] = i+1
#    ax = fig.add_subplot(111)
#    ax.matshow(ones)
#    ax.text(i, i, int(lattice[i, i]), ha="center", va="center", color="w")
#    plt.draw()
#    plt.pause(0.5)




Sbox = [[0, 0, 6, 8, 0, 2, 9, 0, 7],
        [1, 0, 0, 9, 0, 4, 0, 0, 0],
        [2, 0, 0, 7, 0, 0, 0, 5, 0],

        [0, 3, 1, 0, 0, 8, 7, 0, 2],
        [9, 6, 0, 0, 7, 0, 0, 8, 0],
        [7, 2, 0, 0, 0, 5, 0, 4, 0],

        [0, 0, 2, 4, 0, 0, 0, 0, 5],
        [0, 1, 0, 0, 2, 9, 8, 0, 4],
        [6, 0, 0, 1, 8, 0, 0, 0, 0]]

s_solution = \
        [[8, 1, 2, 4, 9, 7, 3, 6, 5],
        [7, 5, 4, 6, 3, 1, 8, 9, 2],
        [6, 9, 3, 2, 5, 8, 1, 7, 4],

        [2, 8, 7, 9, 1, 6, 4, 5, 3],
        [4, 3, 1, 5, 7, 2, 6, 8, 9],
        [9, 6, 5, 8, 4, 3, 2, 1, 7],

        [3, 7, 8, 1, 2, 5, 9, 4, 6],
        [5, 4, 6, 3, 8, 9, 7, 2, 1],
        [1, 2, 9, 7, 6, 4, 5, 3, 8]]

s = \
       [[0, 0, 0, 4, 9, 7, 3, 6, 5],
        [0, 0, 0, 6, 3, 1, 8, 9, 2],
        [0, 0, 0, 2, 5, 8, 1, 7, 4],

        [2, 8, 7, 9, 1, 0, 4, 5, 3],
        [4, 3, 1, 5, 7, 2, 6, 8, 9],
        [9, 6, 5, 0, 4, 3, 2, 1, 7],

        [3, 7, 8, 1, 2, 5, 9, 4, 6],
        [5, 4, 6, 3, 8, 9, 7, 2, 1],
        [1, 2, 9, 7, 6, 4, 5, 3, 8]]



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
            if s[j][i] == 0:
                return (j, i)
    print("error in find_nonempty")

def solve(s):
#    for l in range(9):
#        print(s[l])
#    print()
    if is_full(s):
        plt.pause(5)
        return True
    else:
        (i, j) = find_nonempty(s)
    for k in range(1, 10):
        if is_valid(s, i, j, k):
            s[i][j] = k
            for ii in range(9):
                for jj in range(9):
                    lattice[ii][jj] = s[ii][jj]
            sdraw(fig, ones, lattice)
            if solve(s):
                return True
#    print(s)
    s[i][j] = 0
    return False


#print(is_valid(Sbox, 1,7,9))
#output = is_full(Sbox)
#output = find_nonempty(Sbox)
#print (output)

N = 9
lattice = np.ones([N, N])
ones = np.ones([N, N])
plt.ion() #turns on interactive mode
fig = plt.figure()
ax = fig.add_subplot(111)
output = solve(Sbox)
