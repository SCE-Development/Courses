import os

inputdir = "../input3"
dirpath, dirs, files = next(os.walk(inputdir))
for file in files:
    print(file)
    with open(inputdir+"/"+file, "r") as f:
        n = int(f.readline())
        N = [int(i) for i in f.readline().split()]
        count = {}
        for num in N:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        odd = 0
        even = 0
        for key, value in count.items():
            if value&1:
                odd += key
            else:
                even += key
        ans = abs(odd - even)
    outputdir = inputdir.replace("input", "output")
    if not os.path.exists(outputdir):
        os.makedirs(outputdir)
    outputfilename = (inputdir+"/"+file).replace("input", "output")
    with open(outputfilename, "w") as f:
        f.write(str(ans)+"\n")