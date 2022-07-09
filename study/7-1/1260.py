# 백준 1260번 문제
from collections import deque
# deque를 import하여 bfs 사용 시 que로 이용
import sys
read = sys.stdin.readline
# 여러줄의 데이터를 받아올 경우 사용

n, m, v = map(int, read().split())

graph = [[0] * (n + 1) for _ in range(n + 1)] 
visit_list = [0] * (n + 1)
visit_list2 = [0] * (n + 1)

for _ in range(m):
  a, b = map(int, read().split())
  graph[a][b] = graph[b][a] = 1

def bfs(v):
  q = deque()
  q.append(v)
  # 오른쪽으로 넣고
  visit_list[v] = 1   
  while q:
    v = q.popleft()
    #왼쪽으로 빼기
    print(v, end = " ")
    for i in range(1, n + 1):
      if visit_list[i] == 0 and graph[v][i] == 1:
        q.append(i)
        visit_list[i] = 1

def dfs(v):
  visit_list2[v] = 1        
  print(v, end = " ")
  for i in range(1, n + 1):
    if visit_list2[i] == 0 and graph[v][i] == 1:
      dfs(i)
      #재귀함수를 이용하여 탐색

dfs(v)
print()
bfs(v)
