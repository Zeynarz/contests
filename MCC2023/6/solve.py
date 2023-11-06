from itertools import combinations
n,k = tuple([int(a) for a in input().split()])
arr = [int(a) for a in input().split()]
mod = 998244353

subsetSums = []
for i in range(1,n+1):
    subsets = list(combinations(arr,i))
    subsets = [sum(a) for a in subsets]
    subsetSums += subsets

ans = 0
for s in subsetSums:
    ans += pow(s,k)
    ans %= 998244353

print(ans)
