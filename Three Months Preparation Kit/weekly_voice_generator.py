from common.voice_generator import VoiceGenerator

inventories = {
    "week1": {
        "plus-minus": {
            "problem": {
                "filename": "[HackerRank] 3 Months Preparation Kit, Week 1, Plus-Minus problem",
                "message": """
                    문제, Plus Minus.
                        정수 배열이 주어지면 양수, 음수 및 0인 요소의 비율을 계산하십시오.
                        각 분수의 소수 값을 새 줄에 소수 뒤에 있는 6자리로 출력합니다.
                """
            },
        },
        "min-max-sum": {
            "problem": {
                "filename": "[HackerRank] 3 Months Preparation Kit, Week 1, Min-Max Sum problem",
                "message": """
                    문제, Mini-Max Sum.
                        5개의 양의 정수가 주어지면, 5개의 정수 중 정확히 네 개의 정수를 합하여 계산할 수 있는 최소값과 최대값을 구하라.
                        그런 다음 각 최소값과 최대값을 공백으로 구분된 두 개의 긴 정수의 단일 줄로 출력합니다.
                """
            }
        },
        "time-conversion": {
            "problem": {
                "filename": "[HackerRank] 3 Months Preparation Kit, Week 1, Time Conversion problem",
                "message": """
                    문제, - Time Conversion.
                        지정된 12시간(AM/PM)을 24시간으로 변환합니다.
                    참고. 
                        - 12시간 시계의 12:00:00AM은 24시간 시계의 00:00:00입니다. 
                        - 12시간 시계의 12:00:00PM은 24시간 시계의 12:00:00입니다.
                """
            }
        },
        "breaking-the-records": {
            "problem": {
                "filename": "[HackerRank] 3 Months Preparation Kit, Week 1, Breaking the Records problem",
                "message": """
                    문제, Breaking the Records.
                        마리아는 대학 농구를 하고 프로가 되고 싶어 한다.
                        매 시즌마다 그녀는 자신의 경기 기록을 유지한다.
                        그녀는 한 경기에서 가장 많은 득점과 가장 적은 득점에 대한 자신의 시즌 기록을 깨는 횟수를 집계한다.
                        첫 경기에서 득점한 득점은 시즌 기록을 세우고, 그녀는 거기서부터 세기 시작한다.
                """
            }
        },
        "camel-case-4": {
            "problem": {
                "filename": "[HackerRank] 3 Months Preparation Kit, Week 1, Camel Case 4 problem",
                "message": """
                    문제, Camel Case 4.
                        카멜 케이스는 많은 프로그래밍 언어에서 일반적으로 사용되는 이름 지정 스타일이다.
                        자바에서 메서드 및 변수 이름은 일반적으로 소문자로 시작하며, 이후 모든 단어는 대문자로 시작한다.
                        클래스 이름은 대문자로 시작하는 것을 제외하고 동일한 패턴을 따릅니다.
                        Camel Case 변수, 메서드 및 클래스 이름을 만들거나 분할하는 프로그램을 작성하는 것이 당신의 작업입니다.
                """
            }
        },
        "divisible-sum-pairs": {
            "problem": {
                "filename": "[HackerRank] 3 Months Preparation Kit, Week 1, Divisible Sum Pairs problem",
                "message": """
                    문제, Divisible Sum Pairs.
                        정수 k와 양의 정수의 배열이 주어지면, i가 j보다 작고, 배열 i + 배열 j 가 k로 나누어지는 (i, j) 쌍의 수를 찾아라.
                """
            }
        },
        "sparse-arrays": {
            "problem": {
                "filename": "[HackerRank] 3 Months Preparation Kit, Week 1, Sparse Arrays problem",
                "message": """
                    문제, Sparse Arrays.
                        입력 문자열 모음과 쿼리 문자열 모음이 있습니다. 
                        각 쿼리 문자열에 대해 입력 문자열 목록에서 발생하는 횟수를 결정합니다. 
                        결과 배열을 반환합니다.
                """
            }
        }
    }
}

# target = inventories["week1"]["plus-minus"]["problem"]
# target = inventories["week1"]["min-max-sum"]["problem"]
# target = inventories["week1"]["time-conversion"]["problem"]
# target = inventories["week1"]["breaking-the-records"]["problem"]
# target = inventories["week1"]["camel-case-4"]["problem"]
# target = inventories["week1"]["divisible-sum-pairs"]["problem"]
target = inventories["week1"]["sparse-arrays"]["problem"]

if __name__ == '__main__':
    filename = target["filename"]
    text = target["message"]
    voice_generator = VoiceGenerator()
    voice_generator.generate(text=text, filename=filename)
