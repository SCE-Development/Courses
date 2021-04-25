n = int(input())
N = [int(i) for i in input().split()]
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
print(abs(odd - even))