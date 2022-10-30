# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000436140/000000000068c509
# https://www.youtube.com/watch?v=0lNdd_myTEc&t=1081s

def get_ans(hor,vert):
    if hor==1 or vert==1:
        return 0
    ans = min(hor, vert//2)
    ans -= 1
    ans += min(vert, hor//2)
    ans -= 1
    return ans
    

t = int(input())
tc = 0  # test case

while t > 0:
    r, c = map(int, input().split())
    
    matrix = []
    up = []
    down = []
    right = []
    left = []
    for _ in range(r):
        matrix.append(list(map(int,input().split())))
        up.append([0 for i in range(c)])
        down.append([0 for i in range(c)])
        left.append([0 for i in range(c)])
        right.append([0 for i in range(c)])

    for j in range(c):
        for i in range(r):
            if not(matrix[i][j]):
                continue
            down[i][j] = 1
            if i > 0:
                down[i][j] += down[i-1][j]
    for j in range(c):
        for i in range(r-1, -1, -1):
            if not(matrix[i][j]):
                continue
            up[i][j] = 1
            if i+1 < r:
                up[i][j] += up[i+1][j]
    for i in range(r):
        for j in range(c):
            if not(matrix[i][j]):
                continue
            right[i][j] = 1
            if j > 0:
                right[i][j] += right[i][j-1]
    for i in range(r):
        for j in range(c-1,-1,-1):
            if not(matrix[i][j]):
                continue
            left[i][j] = 1
            if j+1 < c:
                left[i][j] += left[i][j+1]
    
    ans = 0
    for i in range(r):
        for j in range(c):
            if not(matrix[i][j]):
                continue
            ans += get_ans(left[i][j], down[i][j])
            ans += get_ans(left[i][j], up[i][j])
            ans += get_ans(right[i][j], down[i][j])
            ans += get_ans(right[i][j], up[i][j])
    tc += 1
    print('Case #'+str(tc)+': '+str(ans))
    t -= 1
