n,k = map(int, input().split())
N = [int(i) for i in input().split()]
N.sort()
print(N[k-1])