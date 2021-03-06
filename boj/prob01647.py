# 출처: https://www.acmicpc.net/problem/1647
# 문제: 도시 분할 계획


import sys
from heapq import *

read = sys.stdin.readline

v, e = map(int, read().split())
graph = {i: [] for i in range(1, v+1)}
for _ in range(e):
    v1, v2, w = map(int, read().split())
    graph[v1].append((w, v2))
    graph[v2].append((w, v1))

mst_weight = 0
max_weight = -1
connected = set([1])
need_connected = graph[1]
heapify(need_connected)
while need_connected:
    w, vertex = heappop(need_connected)
    if vertex not in connected:
        connected.add(vertex)
        mst_weight += w
        max_weight = max(max_weight, w)
        for next_w, next_v in graph[vertex]:
            if next_v not in connected:
                heappush(need_connected, (next_w, next_v))
print(mst_weight-max_weight)
