import os
from random import randint
maxCase = 20
inputdir = "../input2"
if not os.path.exists(inputdir):
    os.makedirs(inputdir)
for case in range(maxCase):
    print(case)
    n = randint(1,10**4)
    k = randint(1,n)
    t = randint(1,n-k)
    N = [randint(-10**9, 10**9) for i in range(n)]
    with open(inputdir+"/input"+("0"*(len(str(maxCase)) - len(str(case))))+str(case)+".txt", "w") as file:
        file.write(str(n)+" "+str(k)+" "+str(t)+"\n")
        file.write(" ".join(map(str, N)))