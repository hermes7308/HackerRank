"""
HackerRank: Breaking the Records
Link: https://www.hackerrank.com/challenges/three-month-preparation-kit-breaking-best-and-worst-records/problem?h_l=interview&h_r=next-challenge&h_r%5B%5D%5B%5D=next-challenge&h_r%5B%5D%5B%5D=next-challenge&h_v=zen&h_v%5B%5D%5B%5D=zen&h_v%5B%5D%5B%5D=zen&isFullScreen=true&playlist_slugs%5B%5D%5B%5D%5B%5D=preparation-kits&playlist_slugs%5B%5D%5B%5D%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D%5B%5D%5B%5D=three-month-week-one

문제:
    마리아는 대학 농구를 하고 프로가 되고 싶어 한다.
    매 시즌마다 그녀는 자신의 경기 기록을 유지한다.
    그녀는 한 경기에서 가장 많은 득점과 가장 적은 득점에 대한 자신의 시즌 기록을 깨는 횟수를 집계한다.
    첫 경기에서 득점한 득점은 시즌 기록을 세우고, 그녀는 거기서부터 세기 시작한다.
"""

import os


#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    max_value = scores[0]
    min_value = scores[0]
    max_cnt = 0
    min_cnt = 0

    for score in scores[1:]:
        if score > max_value:
            max_value = score
            max_cnt += 1
        if score < min_value:
            min_value = score
            min_cnt += 1

    return max_cnt, min_cnt


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
