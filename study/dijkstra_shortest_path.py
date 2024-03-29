# 출발 노드 설정
# 최단 거리 테이블 초기화
# 방문하지 않은 노드 중에서 최간 거리가 가장 짧은 노드를 선택
# 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단거리 테이블을 갱신
#  3, 4 번 반복

import sys
input = sys.stdin.readline
InF = int(1e9)

n, m = map(int, input().split())
start = int(input())
graph= [[] for i in range(n+1)]
visited = [False] * (n+1)
distance = [InF] * (n+1)

for _ in range(m) :
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

# 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반
def get_smallest_node():
    min_value = InF
    index = 0
    for i in range(1, n+1) :
        if distance[i] < min_value and not visited[i] :
            min_value = distance[i]
            index = i
    return index

def dijkstra(start) :
    distance[start] = 0
    visited[start] = True
    for j in graph[start] :
        distance[j[0]] = j[1]
    for i in range(n-1) :
        now = get_smallest_node()
        visited[now] = True
        for j in graph[now] :
            cost = distance[now] + j[1]
            if cost<distance[j[0]]:
                distance[j[0]] = cost

dijstra(start)

for i in range(1, n+1) :
    if distance[i] == InF :
        print("InF")
    else:
        print(distance[i])
