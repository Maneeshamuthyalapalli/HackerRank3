#!/bin/python3
def camelcase(s):
    word_count = 1
    for char in s[1:]:
        if char.isupper():
            word_count += 1
    return word_count
input_string = "saveChangesInTheEditor"
result = camelcase(input_string)
print(result)            
