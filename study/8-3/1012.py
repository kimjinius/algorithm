import sys 
input = sys.stdin.readline
sys.setrecursionlimit(10000)

T = int(input())

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < m) and (0 <= ny < n):
            if matrix[ny][nx] == 1:
                matrix[ny][nx] = -1 
                dfs(nx, ny)

for i in range(T):
    m, n, k = map(int, input().split())
    matrix = [[0]*m for _ in range(n)]
    cnt=0
    
    for j in range(k):
        a, b = map(int, input().split())
        matrix[b][a] = 1
        
    for k in range(n):
        for g in range(m):
            if matrix[k][g] == 1:
                dfs(g, k)
                cnt+=1
    print(cnt) 
                
