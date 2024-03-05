#!/bin/python3

def reverseArray(A):
    return A[::-1]
n = int(input())
A = list(map(int, input().split()))
result = reverseArray(A) 
for num in result:
    print(num, end=" ") 
