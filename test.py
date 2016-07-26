'''罗马数字'''

def _solution(n):
    help = {"I":1, "II":2, "III":3, "IV":4, "V":5, "VI":6, "VII":7, "VIII":8, "IX":9, 
            "X":10, "XX":20, "XXX":30, "XL":40, "L":50, "LX":60, "LXX":70, "LXX":80, "XC":90, 
            "C":100, "CC":200, "CCC":300, "CD":400, "D":500, "DC":600, "DCC":700, "DCCC":800, "CM":900,
            "M":1000, "":0}
    number = str(n)
    wait_cal = [help.keys()[help.values().index(int(number[i])*(10**(len(number)-i-1)))] for i in range(len(number))]
    a = ''
    # for j in wait_cal:
    #     a+=j
    return a



vals = zip(('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I'),
           (1000, 900, 500,  400, 100,  90,   50,  40,   10,  9,    5,   4,    1))

def solution(n):
    if n == 0: return ""
    return next(c + solution(n-v) for c,v in vals if v <= n)

print solution(1990)




