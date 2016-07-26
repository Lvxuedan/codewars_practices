# Sudoku Solver

Description:


Write a function that will solve a 9x9 Sudoku puzzle. The function will take one argument consisting of the 2D puzzle array, with the value 0 representing an unknown square.

The Sudokus tested against your function will be "easy" (i.e. determinable; there will be no need to assume and test possibilities on unknowns) and can be solved with a brute-force approach.

For Sudoku rules, see the Wikipedia article.

puzzle = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]

sudoku(puzzle)
# Should return
# [[5,3,4,6,7,8,9,1,2],
#  [6,7,2,1,9,5,3,4,8],
#  [1,9,8,3,4,2,5,6,7],
#  [8,5,9,7,6,1,4,2,3],
#  [4,2,6,8,5,3,7,9,1],
#  [7,1,3,9,2,4,8,5,6],
#  [9,6,1,5,3,7,2,8,4],
#  [2,8,7,4,1,9,6,3,5],
#  [3,4,5,2,8,6,1,7,9]]






# Hard Sudoku Solver

Description:


This kata is a harder version of http://www.codewars.com/kata/sudoku-solver/python made by @pineappleclock

Write a function that will solve a 9x9 Sudoku puzzle. The function will take one argument consisting of the 2D puzzle array, with the value 0 representing an unknown square.

The Sudokus tested against your function will be "insane" and can have multiple solutions. It will probably require some sort of brute force.

Consider applying algorithm with

    Hidden Candidates http://www.sudokuwiki.org/Hidden_Candidates
    Naked-pairs/triples/quads http://www.sudokuwiki.org/Naked_Candidates
    Intersection removal http://www.sudokuwiki.org/Intersection_Removal
    Brute Force

For Sudoku rules, see the Wikipedia : http://www.wikiwand.com/en/Sudoku

Used puzzle from : http://www.extremesudoku.info/sudoku.html

puzzle = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]

solve(puzzle)


