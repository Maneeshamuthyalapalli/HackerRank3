#!/bin/python3

def divisibleSumPairs(n, ar, k):
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if (ar[i] + ar[j]) % k == 0:
                count += 1
    return count
n, k = map(int, input().split())
ar = list(map(int, input().split()))
result = divisibleSumPairs(n, ar, k)
print(result)                
