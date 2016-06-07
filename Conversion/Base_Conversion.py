# -*- coding: utf-8 -*-

# def convert(input, source, target):
#     """BEGIN"""
#     print input, source, target
#     before = input 
#     after_dec = source_to_dec(before, source)
#     print 'after_dec:',after_dec 
#     ss = dec_to_target(int(after_dec), target)
#     print ss
#     return ss

# def source_to_dec(before, source):
#     count_dec = 0
#     for i in range(len(before)):
#         index = source.index(before[i])
#         count_dec += (index)* len(source)**(len(before)-i-1)
#     return  count_dec 

# def get_yushu(all_count, len_target):
#     if all_count%len_target == 0:
#         return 30
#     for i in range(30):
#         if all_count <= len_target**i and all_count >= len_target**(i-1):
#             return i

# def dec_to_target(after_dec, target):
#     print 'into ----dec_to_target'
#     len_target = len(target)
#     i = get_yushu(after_dec, len_target)

#     print '======i=',i
#     a_list = []
#     for j in reversed(range(0,i)):
#         print '======j=',j
#         print (after_dec, len(target), j)
#         yushu = (after_dec - after_dec % (len(target)**(j)))/ len(target)**(j) #if j>0 else (after_dec % (len(target)**i))
#         a_list.append((len(target), j, yushu%len(target))) 
#     print a_list 
#     count = 0
#     str = ''
#     for i in a_list:
#         count += (i[0]**i[1])*i[2]
#         str += target[i[2]]
#     str = str.lstrip(target[i[1]]) if str.lstrip(target[i[1]]) else target[i[1]]
#     return str

def convert(input, source, target):
    base_in = len(source)
    base_out = len(target)
    acc = 0
    out = ''
    for d in input:
        print d
        acc *= base_in
        print '%s*=%s'%(acc, base_in)
        acc += source.index(d)
        print '%s += %s'%(acc, source.index(d))

    while acc != 0:
        d = target[acc%base_out]
        acc = acc/base_out
        out = d+out
    print out if out else target[0] 



bin='01'
oct='01234567'
dec='0123456789'
hex='0123456789abcdef'
allow='abcdefghijklmnopqrstuvwxyz'
allup='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alpha='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphanum='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

convert("100100110010110000000101101001", bin, dec)




