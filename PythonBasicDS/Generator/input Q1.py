from random import randint
maxCase = 20
for case in range(maxCase):
    print(case)
    n = randint(1,10**5)
    k = randint(1,n)
    N = [randint(-10**9, 10**9) for i in range(n)]
    with open("input1/input"+("0"*(len(str(maxCase)) - len(str(case))))+str(case)+".txt", "w") as file:
        file.write(str(n)+" "+str(k)+"\n")
        file.write(" ".join(map(str, N)))