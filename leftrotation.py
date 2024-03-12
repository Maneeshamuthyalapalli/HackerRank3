#!/bin/python3
def rotateLeft(d, arr):
    n = len(arr)
    rotated_arr = arr[d % n:] + arr[:d % n]
    return rotated_arr
n, d = map(int, input().split())
arr = list(map(int, input().split()))
result = rotateLeft(d, arr)
print(*result) 
