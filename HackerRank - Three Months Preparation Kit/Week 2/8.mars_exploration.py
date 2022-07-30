"""
HackerRank: Mars Exploration
Link: https://www.hackerrank.com/challenges/three-month-preparation-kit-mars-exploration/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-two

문제:
    지구로 보내는 SOS 신호를 확인 하고, 그 신호가 얼마나 변형 되었는지 계산 하시오.
"""

import os


#
# Complete the 'marsExploration' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def marsExploration(s):
    # Write your code here
    num_of_sos = int(len(s) / 3)
    num_of_transmission = 0
    for index in range(num_of_sos):
        if s[index * 3 + 0] != "S":
            num_of_transmission += 1
        if s[index * 3 + 1] != "O":
            num_of_transmission += 1
        if s[index * 3 + 2] != "S":
            num_of_transmission += 1

    return num_of_transmission


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
