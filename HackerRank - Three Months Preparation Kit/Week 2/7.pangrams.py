"""
HackerRank: Pangrams
Link: https://www.hackerrank.com/challenges/three-month-preparation-kit-pangrams/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-two

문제:
    해당 문제는 주어진 문자열에 포함 되어 있는 문자가 모든 alphabet 을 포함 하고 있는지 확인 하는 문제 입니다.
"""

import os


#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
    # Write your code here
    s = s.lower()
    letters = [ascii_code for ascii_code in range(97, 122)]
    for char in s:
        if ord(char) in letters:
            letters.remove(ord(char))

    if len(letters) > 0:
        return "not pangram"
    return "pangram"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
