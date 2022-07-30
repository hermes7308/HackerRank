"""
HackerRank: Grading Students
Link: https://www.hackerrank.com/challenges/three-month-preparation-kit-grading/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-two

문제:

"""

import math
import os


#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    for index in range(len(grades)):
        grade = grades[index]
        if grade < 38:
            continue

        quotient = math.floor(grade / 5)
        if grade % 5 != 0:
            quotient += 1

        rounded_grade = quotient * 5
        if rounded_grade - grade < 3:
            grades[index] = rounded_grade
        else:
            continue

    return grades


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
