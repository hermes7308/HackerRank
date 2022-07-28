"""
HackerRank: Mini-Max Sum
Link: https://www.hackerrank.com/challenges/three-month-preparation-kit-mini-max-sum/problem?h_l=interview&isFullScreen=true&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-one&h_r=next-challenge&h_v=zen

문제:
    5개의 양의 정수가 주어지면, 5개의 정수 중 정확히 네 개의 정수를 합하여 계산할 수 있는 최소값과 최대값을 구하라.
    그런 다음 각 최소값과 최대값을 공백으로 구분된 두 개의 긴 정수의 단일 줄로 출력합니다.
"""


#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    arr.sort()
    min_value = sum(arr[:4])
    max_value = sum(arr[1:])

    print(min_value, max_value)


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
