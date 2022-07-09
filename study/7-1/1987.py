# 백준 1987 문제
import sys 
from collections import deque

input=sys.stdin.readline
R,C = map(int, input().split())
arr=[list(input()) for _ in range(R)]
dx=[1,-1,0,0]
dy=[0,0,1,-1]
answer=1
def bfs(x,y):
    global answer
    queue=deque()
    queue.append([x,y,arr[x][y]])
    while queue:
        x,y,ans=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx>=0 and ny>=0 and nx<R and ny<C and arr[nx][ny] not in ans:
                queue.append([nx,ny,ans+arr[nx][ny]])
                answer=max(answer,len(ans)+1)
                
bfs(0,0)
print(answer)
