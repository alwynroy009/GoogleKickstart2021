t = int(input())
tc = 0  # test case
while t > 0:
    n, k = map(int, input().split())
    a = input().strip()
    total_unequal = 0
    I = n//2
    for i in range(I):
        if a[i] != a[n-i-1]:
            total_unequal += 1
    ans = k - total_unequal
    if ans < 0 : ans = -1 * ans
    tc += 1
    print('Case #'+str(tc)+': '+str(ans))
    t -= 1
