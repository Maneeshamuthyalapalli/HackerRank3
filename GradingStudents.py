#!/bin/python3

def gradingStudents(grades):
    rounded_grades = []
    for grade in grades:
        if grade < 38:
            rounded_grades.append(grade)
        else:
            next_multiple_of_5 = ((grade // 5) + 1) * 5
            if next_multiple_of_5 - grade < 3:
                rounded_grades.append(next_multiple_of_5)
            else:
                rounded_grades.append(grade)
    return rounded_grades
if __name__ == "__main__":
    n = int(input().strip())
    grades = []
    for _ in range(n):
        grade = int(input().strip())
        grades.append(grade) 
    rounded_grades = gradingStudents(grades)
    for grade in rounded_grades:
        print(grade)    
                                
