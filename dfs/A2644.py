# 입력받기 (전체사람수, 촌수 계산 대상, 촌수 개수, 각 촌수들)
n = int(input())
a, b = map(int, input().split())
m = int(input())

# 배열, 거리 변수 초기화
graph = [[] for _ in range(n+1)]
distance = [-1] * (n+1)

for _ in range(m):
    c, d = map(int, input().split())
    graph[c].append(d)
    graph[d].append(c)

# dfs 함수. 돌면서 거리 계산
def dfs(arr, node, distance, depth):
    distance[node] = depth
    for next_node in arr[node]:
       if distance[next_node] == -1:
           dfs(arr, next_node, distance, depth+1)
        
# target기준으로 촌수 계산
dfs(graph, a, distance, 1)

# 출력
if distance[b] != 0:
    print(distance[b]-1)
else:
    print(-1)