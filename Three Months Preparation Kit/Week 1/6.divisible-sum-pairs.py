"""
HackerRank: Divisible Sum Pairs
Link: https://www.hackerrank.com/challenges/three-month-preparation-kit-divisible-sum-pairs/problem?h_l=interview&h_r=next-challenge&h_r%5B%5D%5B%5D=next-challenge&h_r%5B%5D%5B%5D=next-challenge&h_r%5B%5D%5B%5D%5B%5D%5B%5D=next-challenge&h_r%5B%5D%5B%5D%5B%5D%5B%5D=next-challenge&h_v=zen&h_v%5B%5D%5B%5D=zen&h_v%5B%5D%5B%5D=zen&h_v%5B%5D%5B%5D%5B%5D%5B%5D=zen&h_v%5B%5D%5B%5D%5B%5D%5B%5D=zen&isFullScreen=true&playlist_slugs%5B%5D%5B%5D%5B%5D%5B%5D%5B%5D=preparation-kits&playlist_slugs%5B%5D%5B%5D%5B%5D%5B%5D%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D%5B%5D%5B%5D%5B%5D%5B%5D=three-month-week-one

문제: 정수 k와 양의 정수의 배열이 주어지면, i < j와 array[i] + array[j]가 k로 나누어지는 (i, j) 쌍의 수를 결정한다.
"""

import os


#
# Complete the 'divisibleSumPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY ar
#

def divisibleSumPairs(n, k, ar):
    # Write your code here
    num_of_pairs = 0
    length_of_ar = len(ar)
    for i in range(length_of_ar):
        for j in range(i + 1, length_of_ar):
            if (ar[i] + ar[j]) % k == 0:
                print(i, j)
                num_of_pairs += 1
    return num_of_pairs


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
