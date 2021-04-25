import heapq

applications = []
total_skill_level = 0
while True:
    try:
        line = input()
    except:
        break

    if line == "Hire!":
        skill_level = heapq.heappop(applications)
        total_skill_level -= skill_level
    else:
        name, skill_level = line.split()
        skill_level = -int(skill_level)
        heapq.heappush(applications, skill_level)
print(total_skill_level)