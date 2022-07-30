"""
HackerRank: Counting Valleys
Link: https://www.hackerrank.com/challenges/three-month-preparation-kit-counting-valleys/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-two

문제:
    계곡 아래로 내려 갔다가 올라올 때 sea level 에 도달한 횟수를 계산 하시오.
"""

import os


#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    high_level = 0
    num_of_valleys = 0
    for step in range(steps):
        if path[step] == "U":
            high_level += 1
            if high_level == 0:
                num_of_valleys += 1
        else:
            high_level -= 1

    return num_of_valleys


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
