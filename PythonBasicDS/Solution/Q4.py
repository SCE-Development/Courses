from collections import deque

n,m = map(int, input().split())
a,b = map(lambda x: int(x)-1, input().split())
graph = {i:set() for i in range(n)}
for _ in range(m):
    f,t = [int(i)-1 for i in input().split()]
    graph[f].add(t)
    graph[t].add(f)

que = deque([a])
seen = {a}
minimum_step = [-1]*n
minimum_step[a] = 0
while que:
    node = que.popleft()
    for n in graph[node]:
        if n not in seen:
            que.append(n)
            seen.add(n)
            minimum_step[n] = minimum_step[node] + 1
print(minimum_step[b])