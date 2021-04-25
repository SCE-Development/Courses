import os

inputdir = "../input2"
dirpath, dirs, files = next(os.walk(inputdir))
for file in files:
    print(file)
    with open(inputdir+"/"+file, "r") as f:
        n,k,t = map(int, f.readline().split())
        N = [int(i) for i in f.readline().split()]
        possible = set()
        for i in range(n-k+1):
            sums = sum(N[i:i+k])
            possible.add(sums)
        lst = list(possible)
        lst.sort()
        ans = lst[t-1]

    outputdir = inputdir.replace("input", "output")
    if not os.path.exists(outputdir):
        os.makedirs(outputdir)
    outputfilename = (inputdir+"/"+file).replace("input", "output")
    with open(outputfilename, "w") as f:
        f.write(str(ans)+"\n")