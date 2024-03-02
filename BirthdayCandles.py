#!/bin/python3

def birthday_cake_candles(candles):
    max_height = max(candles)
    count = candles.count(max_height)
    return count
if __name__ == "__main__":
    n = int(input().strip())
    candles = list(map(int, input().strip().split()))
    result = birthday_cake_candles(candles) 
    print(result)  
