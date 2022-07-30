"""
HackerRank: Flipping bits
Link: https://www.hackerrank.com/challenges/three-month-preparation-kit-flipping-bits/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-two

문제:
    주어진, 32 비트 unsigned integer 를 flip 하시오. (1 -> 0 and 0 -> 1)
    그 결과를 unsigned integer 로 반환하시오.
"""

import os


#
# Complete the 'flippingBits' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def flippingBits(n):
    # Write your code here
    binary = "{:032b}".format(n)
    result = ""
    for index in range(len(binary)):
        if binary[index] == '1':
            result += '0'
        else:
            result += '1'

    return int(result, 2)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = flippingBits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
