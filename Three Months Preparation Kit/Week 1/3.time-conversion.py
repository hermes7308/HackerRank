"""
HackerRank: Time Conversion
Link: https://www.hackerrank.com/challenges/three-month-preparation-kit-time-conversion/problem?h_l=interview&h_r%5B%5D=next-challenge&h_r%5B%5D=next-challenge&h_v%5B%5D=zen&h_v%5B%5D=zen&isFullScreen=true&playlist_slugs%5B%5D%5B%5D=preparation-kits&playlist_slugs%5B%5D%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D%5B%5D=three-month-week-one

문제: 지정된 12시간(AM/PM)을 24시간으로 변환합니다.
참고:
    - 12시간 시계의 12:00:00AM은 24시간 시계의 00:00:00입니다.
    - 12시간 시계의 12:00:00PM은 24시간 시계의 12:00:00입니다.
"""
import os


#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    hour = int(s[:2])
    if "PM" in s:
        if hour != 12:
            hour += 12
    else:
        if hour == 12:
            hour = 0

    return "{:02d}{}".format(hour, s[2:len(s) - 2])


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
