import os
from random import randint
maxCase = 20
inputdir = "../input4"
if not os.path.exists(inputdir):
    os.makedirs(inputdir)
for case in range(maxCase):
    print(case)
    n = randint(1, 10**5)
    m = randint(1, 10**5)
    a = randint(1,n)
    b = randint(1,n)
    while a == b:
        b = randint(1,n)
    edges = []
    used = set()
    for _ in range(m):
        while True:
            f,t = randint(1,n), randint(1,n)
            if f == t:
                continue
            string = str(f) + " " + str(t)
            rstring = str(t) + " " + str(f)
            if string in used or rstring in used:
                continue
            edges.append((f,t))
            used.add(string)
            used.add(rstring)
            break

    with open(inputdir+"/input"+("0"*(len(str(maxCase)) - len(str(case))))+str(case)+".txt", "w") as file:
        file.write(str(n)+" "+str(m)+"\n")
        file.write(str(a)+" "+str(b)+"\n")
        for f,t in edges:
            file.write(str(f)+" "+str(t)+"\n")