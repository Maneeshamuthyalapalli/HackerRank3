#!/bin/python3
def bonAppetit(bill, k, b):
    total_bill = sum(bill)
    anna_share = (total_bill - bill[k]) // 2
    if anna_share == b:
        print("Bon Appetit")
    else:
        print(b - anna_share)
n, k = map(int, input().split())
bill = list(map(int, input().split()))
b = int(input())
bonAppetit(bill, k, b)
