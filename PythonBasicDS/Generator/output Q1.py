import os

inputdir = "../input1"
dirpath, dirs, files = next(os.walk(inputdir))
for file in files:
    print(file)
    with open(inputdir+"/"+file, "r") as f:
        n,k = map(int, f.readline().split())
        N = [int(i) for i in f.readline().split()]
        N.sort()
        ans = N[k-1]
    outputfilename = (inputdir+"/"+file).replace("input", "output")
    with open(outputfilename, "w") as f:
        f.write(str(ans)+"\n")