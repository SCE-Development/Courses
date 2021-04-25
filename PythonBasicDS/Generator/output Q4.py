import os
from collections import deque

inputdir = "../input4"
dirpath, dirs, files = next(os.walk(inputdir))
for file in files:
    print(file)
    with open(inputdir+"/"+file, "r") as F:
        n,m = map(int, F.readline().split())
        a,b = map(lambda x: int(x)-1, F.readline().split())
        graph = {i:set() for i in range(n)}
        for _ in range(m):
            f,t = [int(i)-1 for i in F.readline().split()]
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
        ans = minimum_step[b]

    outputdir = inputdir.replace("input", "output")
    if not os.path.exists(outputdir):
        os.makedirs(outputdir)
    outputfilename = (inputdir+"/"+file).replace("input", "output")
    with open(outputfilename, "w") as f:
        f.write(str(ans)+"\n")