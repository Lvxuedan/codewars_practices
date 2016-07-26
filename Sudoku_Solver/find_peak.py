'''
pick peaks
'''

import numpy as np
def _pick_peaks(arr):
    print arr
    a = {}
    a["pos"] = []
    a["peaks"] = []
    for i in range(1,len(arr)-1):
        if arr[i]>arr[i-1]:
            if arr[i]>arr[i+1]:
                a["pos"].append(i)
                a["peaks"].append(arr[i])
            if arr[i]==arr[i+1]:
                smaller = []
                biger = []
                for j in range(i, len(arr)):
                    if arr[i]>arr[j]:
                        smaller.append(j)
                    if arr[i]<arr[j]:
                        biger.append(j)
                print i, smaller, biger
                if not smaller:
                    smaller.append(len(arr)+1)
                if not biger:
                    biger.append(len(arr)+1)
                if min(smaller) < min(biger):
                    a["pos"].append(i)
                    a["peaks"].append(arr[i])
                        
    indexes = np.unique(a["pos"], return_index=True)[1]
    a["pos"] = [a["pos"][index] for index in sorted(indexes)]
    print a





def pick_peaks(arr):
    pos = []
    prob_peak = False
    for i in range(1, len(arr)):
        if arr[i] > arr[i-1]:
            prob_peak = i
        elif arr[i] < arr[i-1] and prob_peak:
            pos.append(prob_peak)
            prob_peak = False
    print {'pos':pos, 'peaks':[arr[i] for i in pos]}



# pick_peaks([1, 2, 5, 4, 3, 2, 3, 6, 4, 1, 2, 3, 3, 4, 5, 3, 2, 1, 2, 3, 5, 5, 4, 3])   #{'pos': [2, 7, 14, 20], 'peaks': [5, 6, 5, 5]}
pick_peaks([1, 2, 5, 5, 5, 3])   #{'pos': [2, 7, 14, 20], 'peaks': [5, 6, 5, 5]}

