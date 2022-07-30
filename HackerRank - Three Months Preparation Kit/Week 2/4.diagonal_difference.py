"""
HackerRank: Diagonal Difference
Link: https://www.hackerrank.com/challenges/three-month-preparation-kit-diagonal-difference/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-two

문제:
    주어진 정사각형 matrix 의 대각선을 계산하는 문제입니다.
    왼쪽에서 오른쪽 대각선의 합과 오른쪽에서 왼쪽 대각선의 합의 차를 구해야합니다.
    값은 절대값으로 반환합니다.
"""

import os


#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    length = len(arr)

    left_to_right = 0
    for i in range(length):
        left_to_right += arr[i][i]

    right_to_left = 0
    for j in range(length):
        right_to_left += arr[length - j - 1][j]

    return abs(left_to_right - right_to_left)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
