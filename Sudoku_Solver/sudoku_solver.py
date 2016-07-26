# -*- coding: utf-8 -*-

def validSolution(board):
  br = len(board)
  sq = int(br ** .5)
 
  a = []
  for x in range(1, br, sq):
    for y in range(1, br, sq):
      b = []
      for m in range(x, x+sq):
        for n in range(y, y+sq):
          b.append([m-1, n-1, board[m-1][n-1]])
      a.append(b)
  return a


def sudoku_1(puzzle):
  L = [1,2,3,4,5,6,7,8,9]
  A = validSolution(puzzle)
  for i in range(len(puzzle)):
    for j in range(len(puzzle[i])):
      for m in A:
        for n in m:
          if i==n[0] and j==n[1] and puzzle[i][j]==0:
            a = set(puzzle[i]+[x[j] for x in puzzle]+[k[2] for k in m])
            b = [v for v in a]
            b.remove(0)
            c = list(set(L)^set(b))
            print i, j, puzzle[i][j], b,c

            if len(c) == 1:
              puzzle[i][j] = c[0]
  print puzzle
  return puzzle


def sudoku(puzzle):
  for i in puzzle:
    for j in i:
      if j==0:
        puzzle_ = sudoku_1(puzzle)
        sudoku(puzzle_)

puzzle = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]

solution = [[5,3,4,6,7,8,9,1,2],
            [6,7,2,1,9,5,3,4,8],
            [1,9,8,3,4,2,5,6,7],
            [8,5,9,7,6,1,4,2,3],
            [4,2,6,8,5,3,7,9,1],
            [7,1,3,9,2,4,8,5,6],
            [9,6,1,5,3,7,2,8,4],
            [2,8,7,4,1,9,6,3,5],
            [3,4,5,2,8,6,1,7,9]]

sudoku(puzzle)

# validSolution(puzzle)





