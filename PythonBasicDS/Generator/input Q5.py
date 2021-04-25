import os
from random import randint
maxCase = 20
inputdir = "../input5"
if not os.path.exists(inputdir):
    os.makedirs(inputdir)
for case in range(maxCase):
    print(case)
    commands = []
    N = randint(5, 10**5)
    na = 0
    for _ in range(N):
        cmd = randint(1,4)
        if cmd == 1:
            if na == 0:
                name_len = randint(1,10)
                name = "".join([chr(ord("a")+randint(0,25)) for i in range(name_len)])
                skill_lvl = randint(0,10**5)
                commands.append(name+" "+str(skill_lvl))
                na += 1
            commands.append("Hire!")
            na -= 1
        else:
            name_len = randint(1,10)
            name = "".join([chr(ord("a")+randint(0,25)) for i in range(name_len)])
            skill_lvl = randint(0,10**5)
            commands.append(name+" "+str(skill_lvl))
            na += 1

    with open(inputdir+"/input"+("0"*(len(str(maxCase)) - len(str(case))))+str(case)+".txt", "w") as file:
        for cmd in commands:
            file.write(cmd+"\n")