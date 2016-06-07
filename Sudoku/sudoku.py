# -*- coding: utf-8 -*-

def validSolution(board):
    br = len(board)
    sq = int(br ** .5)

    if br == sq ** 2:
        for i in board: 
            if len(i) != br:
                return False

        list_column = board 
        list_row = [[m[i] for m in board] for i in range(br)]
        if not check_legal(list_column+list_row, br):
            return False

        list_grid = []
        for x in range(1, br, sq):
            for y in range(1, br, sq):
                a = []
                for m in range(x, x+sq):
                    for n in range(y, y+sq):
                        a.append(board[m-1][n-1])
                list_grid.append(a)

        if not check_legal(list_grid, br):
            return False

        return True

    else:
        return False

def check_legal(list_all, br):
    format_list = [i for i in range(1,br+1)]
    for i in list_all:
        if format_list != sorted(i):
            return False
            
    return True

print validSolution([
            [5, 3, 4, 6, 7, 8, 9, 1, 2], 
            [6, 7, 2, 1, 9, 5, 3, 4, 8],
            [1, 9, 8, 3, 4, 2, 5, 6, 7],
            [8, 5, 9, 7, 6, 1, 4, 2, 3],
            [4, 2, 6, 8, 5, 3, 7, 9, 1],
            [7, 1, 3, 9, 2, 4, 8, 5, 6],
            [9, 6, 1, 5, 3, 7, 2, 8, 4],
            [2, 8, 7, 4, 1, 9, 6, 3, 5],
            [3, 4, 5, 2, 8, 6, 1, 7, 9]])

print validSolution([[5, 3, 4, 6, 7, 8, 9, 1, 2], 
             [6, 7, 2, 1, 9, 0, 3, 4, 9],
             [1, 0, 0, 3, 4, 2, 5, 6, 0],
             [8, 5, 9, 7, 6, 1, 0, 2, 0],
             [4, 2, 6, 8, 5, 3, 7, 9, 1],
             [7, 1, 3, 9, 2, 4, 8, 5, 6],
             [9, 0, 1, 5, 3, 7, 2, 1, 4],
             [2, 8, 7, 4, 1, 9, 6, 3, 5],
             [3, 0, 0, 4, 8, 1, 1, 7, 9]])