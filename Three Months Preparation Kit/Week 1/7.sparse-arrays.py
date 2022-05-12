"""
HackerRank: Sparse Arrays
Link: https://www.hackerrank.com/challenges/three-month-preparation-kit-sparse-arrays/problem

문제: 입력 문자열 모음과 쿼리 문자열 모음이 있습니다. 각 쿼리 문자열에 대해 입력 문자열 목록에서 발생하는 횟수를 결정합니다. 결과 배열을 반환합니다.
"""

import os


#
# Complete the 'matchingStrings' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY strings
#  2. STRING_ARRAY queries
#

def matchingStrings(strings, queries):
    # Write your code here
    matching_list = []
    for query in queries:
        cnt = 0
        for string in strings:
            if query == string:
                cnt += 1
        matching_list.append(str(cnt))

    return matching_list


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    strings_count = int(input().strip())

    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(strings, queries)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
