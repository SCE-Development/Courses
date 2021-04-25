n,k,t = map(int, input().split())
N = [int(i) for i in input().split()]
possible = set()
for i in range(n-k+1):
    sums = sum(N[i:i+k])
    possible.add(sums)
lst = list(possible)
lst.sort()
print(lst[t-1])