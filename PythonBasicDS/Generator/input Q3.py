import os
from random import randint
maxCase = 20
inputdir = "../input3"
if not os.path.exists(inputdir):
    os.makedirs(inputdir)
for case in range(maxCase):
    print(case)
    n = randint(1, 10**6)
    N = [randint(0, 10**6) for i in range(n)]
    with open(inputdir+"/input"+("0"*(len(str(maxCase)) - len(str(case))))+str(case)+".txt", "w") as file:
        file.write(str(n)+"\n")
        file.write(" ".join(map(str, N)))