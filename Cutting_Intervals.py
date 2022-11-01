# explanation : https://youtu.be/e3u3TH2xTEo
# problem statement : https://codingcompetitions.withgoogle.com/kickstart/round/00000000004361e3/000000000082b933

for test in range(1,int(input())+1):
    n, c = map(int, input().split())
    a = [tuple(map(int, input().split())) for _ in range(n)]
    edges = []
    # print(a)
    for l, r in a:
        if l + 1 <= r - 1:
            edges.append((l + 1, 0))
            edges.append((r - 1, 1))
    # [(2, 0), (10, 1), (2, 0), (5, 1), (2, 0), (5, 1), (5, 0), (8, 1)]
    edges.sort()
    # [(2, 0), (2, 0), (2, 0), (5, 0), (5, 1), (5, 1), (8, 1), (10, 1)]
    balance = 0
    prev = ()
    possibilities = []
    for edge, edge_type in edges:
        if any(prev) and prev != (edge, edge_type):
            left = prev[0] + prev[1]
            right = edge - (1 - edge_type)
            if left <= right:
                possibilities.append((left, right, balance))
        if edge_type == 0:
            balance += 1
        else:
            balance -= 1
        prev = (edge, edge_type)
    # [(2, 4, 3), (5, 5, 4), (6, 8, 2), (9, 10, 1)]
    possibilities = sorted([(z, y - x + 1) for x, y, z in possibilities], reverse=True)
    # [(4, 1), (3, 3), (2, 3), (1, 2)]

    answer = len(a)
    for num, cnt in possibilities:
        if c <= cnt:
            answer += num * c 
            break
        answer += num * cnt
        c -= cnt
    print(f'Case #{test}: {answer}')
