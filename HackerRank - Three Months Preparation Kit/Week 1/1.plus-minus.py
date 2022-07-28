"""
HackerRank: Plus Minus
Link: https://www.hackerrank.com/challenges/three-month-preparation-kit-plus-minus/problem?h_l=interview&isFullScreen=true&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-one

문제:
    정수 배열이 주어지면 양수, 음수 및 0인 요소의 비율을 계산하십시오.
    각 분수의 소수 값을 새 줄에 소수 뒤에 있는 6자리로 출력합니다.
"""


#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    length = len(arr)
    positive = 0
    negative = 0
    zero = 0
    for num in arr:
        if num > 0:
            positive += 1
        elif num < 0:
            negative += 1
        else:
            zero += 1

    print("{:.6f}".format(round(positive / length, 6)))
    print("{:.6f}".format(round(negative / length, 6)))
    print("{:.6f}".format(round(zero / length, 6)))


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
