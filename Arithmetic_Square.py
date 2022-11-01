# Explanation :  https://youtu.be/1DHxSpcbSGs

import numpy as np

tests = int(input())
test_case = 1
while tests > 0:
    arr = np.array(list(map(int,input().split())))
    arr = np.append(arr, list(map(int,input().split())))
    arr = np.insert(arr,4,0)
    arr = np.append(arr, list(map(int,input().split())))
    arr.shape = (3,3)
    
    # Find all the possible values (4 series -> center row, center column, diagonal, sec diagonal)
    possible = set()
    
    if (arr[1,0]+arr[1,2])%2==0:
        possible.add((arr[1,0]+arr[1,2])//2)
    if (arr[0,1]+arr[2,1])%2==0:
        possible.add((arr[0,1]+arr[2,1])//2)
    if (arr[0,0]+arr[2,2])%2==0:
        possible.add((arr[0,0]+arr[2,2])//2)
    if (arr[0,2]+arr[2,0])%2==0:
        possible.add((arr[0,2]+arr[2,0])//2)
    
    ans = 0
    for pos in possible:
        arr[1,1] = pos
        cnt=0
        for x,y,z in (arr[0],arr[1],arr[2], \
        arr[:,0],arr[:,1],arr[:,2], \
        np.diagonal(arr),np.diagonal(np.fliplr(arr))):
            if x + z == 2 *y:
                cnt += 1
        if cnt>ans:
            ans =cnt
            

    print(f'Case #{test_case}: {ans}')
    test_case += 1
    tests -= 1

