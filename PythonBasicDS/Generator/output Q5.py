import os
import heapq

inputdir = "../input5"
dirpath, dirs, files = next(os.walk(inputdir))
for file in files:
    print(file)
    with open(inputdir+"/"+file, "r") as f:
        applications = []
        total_skill_level = 0
        while True:
            try:
                line = f.readline().strip()
                if not line:
                    break
            except:
                break

            if line.strip() == "Hire!":
                skill_level = heapq.heappop(applications)
                total_skill_level -= skill_level
            else:
                name, skill_level = line.split()
                skill_level = -int(skill_level)
                heapq.heappush(applications, skill_level)
        ans = total_skill_level

    outputdir = inputdir.replace("input", "output")
    if not os.path.exists(outputdir):
        os.makedirs(outputdir)
    outputfilename = (inputdir+"/"+file).replace("input", "output")
    with open(outputfilename, "w") as f:
        f.write(str(ans)+"\n")