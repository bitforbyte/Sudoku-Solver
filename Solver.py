import math
import copy
import json
from pprint import pprint

ret = [[]]
def setRet(value):
    global ret
    ret = value

def getRet():
    return ret

def numInRow(number, row):
    if (number in row):
        return True
    else:
        return False

def blockCheck(board, row, col, number):
    blocks = findBlock(board)
    # TODO Fix nastyness
    maping = {}
    maping[(0,0)] = 0
    maping[(0,1)] = 1
    maping[(0,2)] = 2
    maping[(1,0)] = 3
    maping[(1,1)] = 4
    maping[(1,2)] = 5
    maping[(2,0)] = 6
    maping[(2,1)] = 7
    maping[(2,2)] = 8
    #print(maping[row,col])
    if number in blocks[maping[math.floor(row/3),math.floor(col/3)]]:
        return True
    else:
        return False

# Transpose so check row
def transposeBoard(board):
    return [[board[j][i] for j in range(len(board))] for i in range(len(board[0]))]

# TODO rename
def findBlock(board):
    ret = []
    for row in range(3):
        for col in range(3):
            block = []
            for i in range(3):
                for j in range(3):
                    block.append(board[3*row + i][3*col + j])
            ret.append(block)
    return ret

def complete(board):
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == 0:
                return False
    return True

def solveSudoku(board):
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == 0:
                for i in range(1, 10):
                    
                    inRow = numInRow(i, board[row])
                    inCol = numInRow(i, transposeBoard(board)[col])
                    inBlock = blockCheck(board, row, col, i)
                    
                    if ((not inRow) and (not inCol) and (not inBlock)):
                        board[row][col] = i
                        if complete(board):
                            setRet(copy.deepcopy(board))
                        ret = solveSudoku(board)
                    
                    board[row][col] = 0

                if board[row][col] == 0:
                    return board
    return board


def main():
    with open('Example.json') as f:
        data = json.load(f)

    board = solveSudoku(data["Problem"])
    pprint(ret)
    print (ret == data["Solution"])

if __name__ == "__main__":
    main()