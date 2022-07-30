"""
HackerRank: Lonely Integer
Link: https://www.hackerrank.com/challenges/three-month-preparation-kit-lonely-integer/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-two

문제:
    주어진 정수형 배열에서 unique 한 변수를 찾는 algorithm 을 작성하시오.
"""

import os


#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    # Write your code here
    cnt_map = {}

    for num in a:
        if num in cnt_map.keys():
            cnt_map[num] += 1
        else:
            cnt_map[num] = 1

    for num in cnt_map.keys():
        if cnt_map[num] == 1:
            return num

    return None


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()
