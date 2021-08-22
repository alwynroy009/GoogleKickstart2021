import heapq

def add_task(co_ord, value):
    if co_ord in entry_finder:
        lst = entry_finder.pop(co_ord)
        lst[1] = (100_000_000,100_000_000)
    lst = [value, co_ord]
    heapq.heappush(priority_q, lst)
    entry_finder[co_ord] = lst

def pop_task():
    while priority_q:
        _, co_ord = heapq.heappop(priority_q)
        if co_ord != (100_000_000,100_000_000):
            del entry_finder[co_ord]
            return co_ord

dirs=[(0,1),(1,0),(-1,0),(0,-1)]

boxes = 0
for tests in range(1,int(input())+1):
    row, col = map(int,input().split())
    org_matr=[list(map(int,input().split())) for i in range(row)]
    matrix=[i[:] for i in org_matr]
    priority_q = []
    entry_finder = {}
    
    for i in range(row):
        for j in range(col):
            add_task((i,j),-org_matr[i][j])

    for _ in range(row*col):
        i, j = pop_task()
        for x,y in dirs:
            if 0<=i+x<row and 0<=j+y<col and matrix[i][j]>matrix[i+x][j+y]+1:
                matrix[i+x][j+y]=matrix[i][j]-1
                add_task((i+x,j+y),-matrix[i][j]+1)
    boxes=sum(matrix[i][j]-org_matr[i][j] 
                for i in range(row) 
                for j in range(col))
    print(f'Case #{tests}: {boxes}')
