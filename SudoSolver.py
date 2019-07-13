
# Kendall Nicley
# SudoSolver
import math
import copy
import json
from pprint import pprint

"""

"""
class SudoSolver:
    def __init__(self, board):
        self.board = board
        self.solution = [[]]
    
    """
    scan the board and return if it's completed
    returns boolean
    """
    def _complete(self):
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                if self.board[row][col] == 0:
                    return False
        return True

    """
    Check the 3x3 matrix block for the given number
    Param: row, columns, and number to compare
    Returns: boolean
    """
    def _blockCheck(self, row, col, number):
        blocks = self._chunkGrid()
        # Map each of the row,column to the 3x3 matrix location
        maping = {}
        for i in range(9):
            maping[(int(i/3)),i%3] = i

        # If the number exists within the 3x3 matrix return true
        if number in blocks[maping[math.floor(row/3),math.floor(col/3)]]:
            return True
        else:
            return False

    """
    Will take the board and return the 9 3x3 grids as a list
    Return: nested list of each 3x3 grid in order [UL, UM, UR, ML, MM, MR, LL, LM, LR]
    """
    def _chunkGrid(self):
        ret = []

        for row in range(3):
            for col in range(3):
                block = []
                for i in range(3):
                    for j in range(3):
                        block.append(self.board[3*row + i][3*col + j])
                ret.append(block)
        return ret

    # Returns true if number is in given row
    def _numInRow(self, num, row):
        return True if num in row else False

    # will transpose the board turning column into rows for easy check
    def _transposeBoard(self):
        return [[self.board[j][i] for j in range(len(self.board))] for i in range(len(self.board[0]))]

    def solve(self):
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                # If the locations is empty
                if self.board[row][col] == 0:
                    # Loop through 1-9 to get possible values
                    for i in range(1, 10):
                        # Check the rows, columns, and 3x3 grid
                        inRow = self._numInRow(i, self.board[row])
                        inCol = self._numInRow(i, self._transposeBoard()[col])
                        inBlock = self._blockCheck(row, col, i)

                        # If it doesn't exist in all three
                        if ((not inRow) and (not inCol) and (not inBlock)):
                            # Assign value
                            self.board[row][col] = i
                            
                            #If we're done assign solution
                            if self._complete():
                                self.solution = copy.deepcopy(self.board)
                                return self.board
                            ret = self.solve()
                    
                        self.board[row][col] = 0

                    if self.board[row][col] == 0:
                        return self.board
        return self.board
