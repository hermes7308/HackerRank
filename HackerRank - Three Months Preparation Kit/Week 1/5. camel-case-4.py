"""
HackerRank: Camel Case 4
Link: https://www.hackerrank.com/challenges/three-month-preparation-kit-camel-case/problem?h_l=interview&h_r%5B%5D=next-challenge&h_r%5B%5D=next-challenge&h_r%5B%5D%5B%5D%5B%5D=next-challenge&h_r%5B%5D%5B%5D%5B%5D=next-challenge&h_v%5B%5D=zen&h_v%5B%5D=zen&h_v%5B%5D%5B%5D%5B%5D=zen&h_v%5B%5D%5B%5D%5B%5D=zen&isFullScreen=true&playlist_slugs%5B%5D%5B%5D%5B%5D%5B%5D=preparation-kits&playlist_slugs%5B%5D%5B%5D%5B%5D%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D%5B%5D%5B%5D%5B%5D=three-month-week-one

문제:
    카멜 케이스(Camel Case)는 많은 프로그래밍 언어에서 일반적으로 사용되는 이름 지정 스타일이다.
    자바에서 메서드 및 변수 이름은 일반적으로 소문자로 시작하며, 이후 모든 단어는 대문자로 시작한다(예: startThread).
    클래스 이름은 대문자로 시작하는 것을 제외하고 동일한 패턴을 따릅니다(예: BlueCar).
    Camel Case 변수, 메서드 및 클래스 이름을 만들거나 분할하는 프로그램을 작성하는 것이 당신의 작업입니다.
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys


def index_uppercase(str, start_index=0):
    if start_index >= len(str):
        return None

    for index in range(start_index, len(str)):
        char_unit = str[index]
        if char_unit.isupper():
            return index

    return None


if __name__ == '__main__':
    command_input = sys.stdin.read()
    command_lines = command_input.split("\n")
    for command_line in command_lines:
        command_split_line = command_line.rstrip().split(";")
        if command_split_line[0] == "S":
            # split
            previous_index = 0
            current_index = index_uppercase(command_split_line[2], 1)
            name_unit = []
            while True:
                if current_index == None:
                    name_unit.append(command_split_line[2][previous_index:].lower())
                    break
                name_unit.append(command_split_line[2][previous_index:current_index].lower())
                previous_index = current_index
                current_index = index_uppercase(command_split_line[2], current_index + 1)

            if command_split_line[1] == "M":  # method:
                name_unit[len(name_unit) - 1] = name_unit[len(name_unit) - 1][:-2]
            if command_split_line[1] == "C":  # class:
                pass
            if command_split_line[1] == "V":  # variable:
                pass
            print(" ".join(name_unit))

        else:
            # combine
            name_unit = command_split_line[2].split(" ")
            for index in range(len(name_unit)):
                name_unit[index] = name_unit[index][0].upper() + name_unit[index][1:]

            if command_split_line[1] == "M":  # method:
                name_unit[0] = name_unit[0][0].lower() + name_unit[0][1:]
                name_unit[len(name_unit) - 1] = name_unit[len(name_unit) - 1] + "()"
            if command_split_line[1] == "C":  # class:
                pass
            if command_split_line[1] == "V":  # variable:
                name_unit[0] = name_unit[0][0].lower() + name_unit[0][1:]

            print("".join(name_unit))
