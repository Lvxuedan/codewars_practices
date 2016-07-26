# -*- coding: utf-8 -*-

def get_lines(list_, width):
    if len(list_) == 1:
        return [list_]
    for i in range(len(list_)+1):
        additionLen = sum([len(j) for j in list_[0:i+1]]) + len(list_[0:i+1]) - 1
        additionLen1 = sum([len(j) for j in list_[0:i]]) + len(list_[0:i]) - 1
        # print i,'aa',additionLen 
        if additionLen > width and width >= additionLen1:
            break 
    a =  list_[0:i]
    if not list_[0:i]:
        return []
    else:
        return [a] + [get_lines([x for x in list_ if x not in a],  width)][0]


def get_res(data, width):
    a = ''
    for i in range(len(data)):
        if not data[i][1]:
            a+= '%s\n'%data[i][0][0] + ' ' if data[i][0][0] else ' '*(width - len(data[i][0][0])) + data[i][0][0]+'\n'
        else:
            A = [data[i][0][j] + ' ' if i == len(data)-1 else data[i][0][j] + data[i][1][j]*' ' for j in range(len(data[i][1])) ] + [data[i][0][len(data[i][0])-1]]
            B = ''
            for i in A:
                B+=i
            a+= '%s\n'%B
    return a


def justify(text, width):
    width = width-1
    a = text.split(' ')
    if len(a) <= 1:
        return '%s\n'%text
    else: 
        results = []
        lines =  get_lines(a, width)
        for line in lines:
            I = (width - sum([len(i) for i in line])) / (len(line) - 1) if len(line) > 1 else 1
            J = (width - sum([len(i) for i in line])) % (len(line) - 1) if len(line) > 1 else 0
            L = [I for a in range(len(line)-1)] 
            A = [1  if m < J else 0 for m in range(len(line)-1)]
            B = [L[n]+A[n] for n in range(len(line)-1)]
            results.append([line,B]) 
        return get_res(results, width)


line = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum sagittis dolor mauris, at elementum ligula tempor eget. In quis rhoncus nunc, at aliquet orci. Fusce at dolor sit amet felis suscipit tristique.'
# print justify(line, 36)
print justify('123 45 6', 7)
print  '123 45\n6'
