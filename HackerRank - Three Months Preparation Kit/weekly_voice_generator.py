from common.voice_generator import VoiceGenerator

inventories = {
    # common
    "common": {
        "insertion": {
            "read_and_analyze": {
                "filename": "[Common] Read and analyze the problem carefully.",
                "message": "영상을 잠시 정지하고 문제를 잘 읽고 분석해보세요."
            },
            "run_code": {
                "filename": "[Common] Run code",
                "message": "코드를 실행합니다."
            },
            "completion_run_code": {
                "filename": "[Common] Completion run code",
                "message": "모든 샘플테스트 데이터가 성공적으로 완료된 것을 확인할 수 있습니다."
            },
            "submit_code": {
                "filename": "[Common] Submit code",
                "message": "코드를 제출합니다."
            },
            "completion_submit_code": {
                "filename": "[Common] Completion submit code",
                "message": "모든 테스트 케이스가 완료된 것을 확인할 수 있습니다."
            },
        },
    },
    # week1
    "week1": {
        "plus_minus": {
            "problem": {
                "filename": "[HackerRank] 3 Months Preparation Kit, Week 1, Plus-Minus problem",
                "message": """
                    문제, Plus Minus.
                        정수 배열이 주어지면 양수, 음수 및 0인 요소의 비율을 계산하십시오.
                        각 분수의 소수 값을 소수 뒤에 있는 6자리로 출력합니다.
                """
            },
            "00_00_25": {
                "filename": "[HackerRank] 3 Months Preparation Kit, Week 1, Plus-Minus 00_00_25",
                "message": """
                    먼저, 양수, 음수, 0의 갯수를 저장할 변수를 생성하고 초기값을 0으로 초기화 합니다.
                """
            },
            "00_00_41": {
                "filename": "[HackerRank] 3 Months Preparation Kit, Week 1, Plus-Minus 00_00_41",
                "message": """
                    배열 안에 있는 정수를 한개씩 가져옵니다.
                """
            },
            "00_00_48": {
                "filename": "[HackerRank] 3 Months Preparation Kit, Week 1, Plus-Minus 00_00_48",
                "message": """
                    해당 값이 양수 또는 음수 또는 0 인지 판단하여 이전에 생성한 변수에 카운트를 증가시킵니다.
                """
            },
            "00_01_19": {
                "filename": "[HackerRank] 3 Months Preparation Kit, Week 1, Plus-Minus 00_01_19",
                "message": """
                    마지막으로 카운팅이 완료된 변수의 비율을 출력합니다.
                    출력시 결과값은 소수점 6자리까지 출력합니다.
                """
            },

        },
        "min_max_sum": {
            "problem": {
                "filename": "[HackerRank] 3 Months Preparation Kit, Week 1, Min-Max Sum problem",
                "message": """
                    문제, Mini-Max Sum.
                        5개의 양의 정수가 주어지면, 5개의 정수 중 정확히 네 개의 정수를 합하여 계산할 수 있는 최소값과 최대값을 구하라.
                """
            },
            "00_03_33": {
                "filename": "[HackerRank] 3 Months Preparation Kit, Week 1, Min-Max Sum 00_03_33",
                "message": """
                    먼저, 배열을 정렬 합니다.
                """
            },
            "00_03_38": {
                "filename": "[HackerRank] 3 Months Preparation Kit, Week 1, Min-Max Sum 00_03_38",
                "message": """
                    최소값은 배열 첫번째 변수부터 마지막 전 (즉, 네번째) 변수까지의 합이고,
                    최대값은 배열 두번째 변수부터 마지막 변수까지의 합 입니다.
                """
            },
            "00_04_08": {
                "filename": "[HackerRank] 3 Months Preparation Kit, Week 1, Min-Max Sum 00_04_08",
                "message": """
                    방금 전 구한 최소값과 최대값을 출력합니다.
                """
            },
        },
        "time_conversion": {
            "problem": {
                "filename": "[HackerRank] 3 Months Preparation Kit, Week 1, Time Conversion problem",
                "message": """
                    문제, - Time Conversion.
                        지정된 12시간(AM/PM)을 24시간으로 변환합니다.
                    참고. 
                        - 12시간 시계의 12:00:00AM은 24시간 시계의 00:00:00입니다. 
                        - 12시간 시계의 12:00:00PM은 24시간 시계의 12:00:00입니다.
                """
            },
            "00_05_22": {
                "filename": "[HackerRank] 3 Months Preparation Kit, Week 1, Time Conversion 00_05_22",
                "message": """
                    먼저, 입력 받은 문자열 시간에서 hour를 변수로 저장합니다.
                """
            },
            "00_05_34": {
                "filename": "[HackerRank] 3 Months Preparation Kit, Week 1, Time Conversion 00_05_34",
                "message": """
                    만약, 입력받은 문자열에 PM이 포함되어 있으면, hour가 12가 아닐때, hour 변수에 12를 더해줍니다.
                """
            },
            "00_05_55": {
                "filename": "[HackerRank] 3 Months Preparation Kit, Week 1, Time Conversion 00_05_55",
                "message": """
                    만약, 입력받은 문자열에 AM이 포함되어 있으면, hour가 12 일때, hour 변수를 0으로 설정합니다.
                """
            },
            "00_06_12": {
                "filename": "[HackerRank] 3 Months Preparation Kit, Week 1, Time Conversion 00_06_12",
                "message": """
                    마지막으로 변경된 hour변수를 이용하여 문자열 형태로 변경하여 반환해줍니다.
                """
            },

        },
        "breaking_the_records": {
            "problem": {
                "filename": "[HackerRank] 3 Months Preparation Kit, Week 1, Breaking the Records problem",
                "message": """
                    문제, Breaking the Records.
                        마리아는 대학 농구를 하고 프로가 되고 싶어 한다.
                        매 시즌마다 그녀는 자신의 경기 기록을 유지한다.
                        그녀는 한 경기에서 가장 많은 득점과 가장 적은 득점에 대한 자신의 시즌 기록을 깨는 횟수를 집계한다.
                        첫 경기에서 득점한 득점은 시즌 기록을 세우고, 그녀는 거기서부터 세기 시작한다.
                """
            },
            "00_07_47": {
                "filename": "[HackerRank] 3 Months Preparation Kit, Week 1, Breaking the Records 00_07_47",
                "message": """
                    max value 변수와 min value 변수를 배열의 첫번째 변수로 초기화를 하고, 
                    max count 변수와 min count 변수를 0으로 초기화 합니다.
                """
            },
            "00_08_15": {
                "filename": "[HackerRank] 3 Months Preparation Kit, Week 1, Breaking the Records 00_08_01",
                "message": """
                    그리고, 기록되는 max value 보다 더 좋은 성적을 받았을 경우, 
                    max value 를 새로운 값으로 설정하고, max count를 1 증가시킵니다.
                    반대로, 기록되는 min value 보다 더  낮은 성적을 받았을 경우,
                    min value 를 새로운 값으로 설정하고, min count를 1 증가시킵니다.
                """
            },
            "00_09_15": {
                "filename": "[HackerRank] 3 Months Preparation Kit, Week 1, Breaking the Records 00_09_15",
                "message": """
                    방금 구한 max count 변수와 min count 변수를 반환합니다.
                """
            },
        },
        "camel_case_4": {
            "problem": {
                "filename": "[HackerRank] 3 Months Preparation Kit, Week 1, Camel Case 4 problem",
                "message": """
                    문제, Camel Case 4.
                        카멜 케이스는 많은 프로그래밍 언어에서 일반적으로 사용되는 이름 지정 스타일이다.
                        자바에서 메서드 및 변수 이름은 일반적으로 소문자로 시작하며, 이후 모든 단어는 대문자로 시작한다.
                        클래스 이름은 대문자로 시작하는 것을 제외하고 동일한 패턴을 따릅니다.
                        Camel Case 변수, 메서드 및 클래스 이름을 만들거나 분할하는 프로그램을 작성하는 것이 당신의 작업입니다.
                """
            },
            "00_10_33": {
                "filename": "[HackerRank] 3 Months Preparation Kit, Week 1, Camel Case 4 00_10_33",
                "message": """
                    먼저, Python 실행 main 구문을 작성합니다.
                """
            },
            "00_10_44": {
                "filename": "[HackerRank] 3 Months Preparation Kit, Week 1, Camel Case 4 00_10_44",
                "message": """
                    다음으로, 입력 데이터를 읽어와 뉴라인 별로 나누어 저장합니다.
                """
            },
            "00_11_40": {
                "filename": "[HackerRank] 3 Months Preparation Kit, Week 1, Camel Case 4 00_11_40",
                "message": """
                    그 후, 새미콜론으로 결합되어 있는 입력 데이터를 분할 합니다.
                    명령어는 Split 또는 Combine, 
                    요청타입은 Method 또는 Variable 또는 Class가 있습니다.
                """
            },
            "00_12_07": {
                "filename": "[HackerRank] 3 Months Preparation Kit, Week 1, Camel Case 4 00_12_07",
                "message": """
                    해당 명령어가 Split 일 경우, Combine 된 이름을 분리하는 것이기 때문에, 
                    이름의 각 대문자 위치를 찾아서 나눈 후, 소문자로 변경하여 리스트에 저장합니다.
                """
            },
            "00_17_43": {
                "filename": "[HackerRank] 3 Months Preparation Kit, Week 1, Camel Case 4 00_17_43",
                "message": """
                    요청타입이 Method 인 경우, 괄호를 제외하고,
                    요청타입이 Class 또는 Variable 인 경우, Pass 합니다. 
                """
            },
            "00_19_32": {
                "filename": "[HackerRank] 3 Months Preparation Kit, Week 1, Camel Case 4 00_19_32",
                "message": """
                    리스트를 크기 1인 공백으로 Join해서 결과로 출력해줍니다.
                """
            },
            "00_19_46": {
                "filename": "[HackerRank] 3 Months Preparation Kit, Week 1, Camel Case 4 00_19_46",
                "message": """
                    제가 import 하지 않았군요.
                    상단에 import 를 추가해줍니다.
                """
            },
            "00_20_02": {
                "filename": "[HackerRank] 3 Months Preparation Kit, Week 1, Camel Case 4 00_20_02",
                "message": """
                    해당 명령어가 Combine 일 경우, Split 된 이름을 결합하는 것이기 때문에, 
                    이름을 공백 별로 나누고,
                    각 첫 자리 문자를 대문자화 하여 리스트에 저장을 합니다.
                """
            },
            "00_21_33": {
                "filename": "[HackerRank] 3 Months Preparation Kit, Week 1, Camel Case 4 00_21_33",
                "message": """
                    요청타입이 Method 인 경우, 리스트의 첫번째 변수의 첫 글자를 소문자로 변경하고, 
                    뒤에 괄호를 추가해줍니다.
                """
            },
            "00_23_10": {
                "filename": "[HackerRank] 3 Months Preparation Kit, Week 1, Camel Case 4 00_23_10",
                "message": """
                    요청타입이 Class 인 경우, 변경 사항은 없습니다.
                """
            },
            "00_23_24": {
                "filename": "[HackerRank] 3 Months Preparation Kit, Week 1, Camel Case 4 00_23_24",
                "message": """
                    요청타입이 Variable 인 경우, 리스트의 첫번째 변수의 첫 글자를 소문자로 변경합니다.
                    리스트를 Join해서 결과로 출력해 줍니다.
                """
            },
            "00_24_23": {
                "filename": "[HackerRank] 3 Months Preparation Kit, Week 1, Camel Case 4 00_24_23",
                "message": """
                    에러가 발생했네요. 무엇이 문제 인지 확인해 볼까요?
                """
            },
            "00_24_39": {
                "filename": "[HackerRank] 3 Months Preparation Kit, Week 1, Camel Case 4 00_24_39",
                "message": """
                    앗!! 제가 29번째 줄에 괄호를 잘못 넣었습니다. 수정해줍니다.
                """
            },
        },
        "divisible_sum_pairs": {
            "problem": {
                "filename": "[HackerRank] 3 Months Preparation Kit, Week 1, Divisible Sum Pairs problem",
                "message": """
                    문제, Divisible Sum Pairs.
                        정수 k와 양의 정수의 배열이 주어지면, i가 j보다 작고, 배열 i + 배열 j 가 k로 나누어지는 (i, j) 쌍의 수를 찾아라.
                """
            },
            "00_25_39": {
                "filename": "[HackerRank] 3 Months Preparation Kit, Week 1, Divisible Sum Pairs 00_25_39",
                "message": """
                    먼저, i, j 쌍수의 갯수를 저장할 변수와, 
                    배열의 길이를 저장할 변수를 생성합니다.
                """
            },
            "00_26_00": {
                "filename": "[HackerRank] 3 Months Preparation Kit, Week 1, Divisible Sum Pairs 00_26_00",
                "message": """
                    모든 i와, i보다 큰 j가 저장되어 있는 변수의 합을 k로 나누어, 
                    0으로 나누어 떨어지는 쌍수가 있을 경우, 
                    쌍수 갯수를 저장하는 변수를 증가시킵니다. 
                """
            },
            "00_27_09": {
                "filename": "[HackerRank] 3 Months Preparation Kit, Week 1, Divisible Sum Pairs 00_27_09",
                "message": """
                    마지막으로, 쌍수 갯수를 저장한 변수를 반환합니다. 
                """
            },
        },
        "sparse_arrays": {
            "problem": {
                "filename": "[HackerRank] 3 Months Preparation Kit, Week 1, Sparse Arrays problem",
                "message": """
                    문제, Sparse Arrays.
                        입력 문자열 모음과 쿼리 문자열 모음이 있습니다. 
                        각 쿼리 문자열에 대해 입력 문자열 목록에서 발생하는 횟수를 결정합니다.
                """
            },
            "00_28_09": {
                "filename": "[HackerRank] 3 Months Preparation Kit, Week 1, Sparse Arrays 00_28_09",
                "message": """
                    먼저, 빈 리스트를 생성합니다.
                """
            },
            "00_28_15": {
                "filename": "[HackerRank] 3 Months Preparation Kit, Week 1, Sparse Arrays 00_28_15",
                "message": """
                    반복문을 사용하여 queries 안에 있는 query를 가져옵니다.
                """
            },
            "00_28_23": {
                "filename": "[HackerRank] 3 Months Preparation Kit, Week 1, Sparse Arrays 00_28_23",
                "message": """
                    해당 query의 count를 초기화 하고,
                    반목문을 사용하여 strings 안에 있는 string을 가져옵니다.
                """
            },
            "00_28_34": {
                "filename": "[HackerRank] 3 Months Preparation Kit, Week 1, Sparse Arrays 00_28_34",
                "message": """
                    만약, query와 string이 같을 경우 count를 증가시킵니다.
                """
            },
            "00_28_47": {
                "filename": "[HackerRank] 3 Months Preparation Kit, Week 1, Sparse Arrays 00_28_47",
                "message": """
                    query와 strings의 비교과 완료되면, 
                    처음에 생성한 빈 리스트에 넣어 줍니다.
                """
            },
            "00_28_59": {
                "filename": "[HackerRank] 3 Months Preparation Kit, Week 1, Sparse Arrays 00_28_59",
                "message": """
                    마지막으로, 해당 리스트를 반환합니다.
                """
            },
        }
    }
}

targets = [
    # common
    # inventories["common"]["insertion"]["read_and_analyze"],
    # inventories["common"]["insertion"]["run_code"],
    # inventories["common"]["insertion"]["completion_run_code"],
    # inventories["common"]["insertion"]["submit_code"],
    # inventories["common"]["insertion"]["completion_submit_code"],
    # week1
    # Plus Minus
    # inventories["week1"]["plus_minus"]["problem"],
    # inventories["week1"]["plus_minus"]["00_00_25"],
    # inventories["week1"]["plus_minus"]["00_00_41"],
    # inventories["week1"]["plus_minus"]["00_00_48"],
    # inventories["week1"]["plus_minus"]["00_01_19"],
    # Mini-Max Sum
    # inventories["week1"]["min_max_sum"]["problem"],
    # inventories["week1"]["min_max_sum"]["00_03_33"],
    # inventories["week1"]["min_max_sum"]["00_03_38"],
    # inventories["week1"]["min_max_sum"]["00_04_08"],
    # Time Conversion
    # inventories["week1"]["time_conversion"]["problem"],
    # inventories["week1"]["time_conversion"]["00_05_22"],
    # inventories["week1"]["time_conversion"]["00_05_34"],
    # inventories["week1"]["time_conversion"]["00_05_55"],
    # inventories["week1"]["time_conversion"]["00_06_12"],
    # Breaking the records
    # inventories["week1"]["breaking_the_records"]["problem"],
    # inventories["week1"]["breaking_the_records"]["00_07_47"],
    # inventories["week1"]["breaking_the_records"]["00_08_15"],
    # inventories["week1"]["breaking_the_records"]["00_09_15"],
    # Camel Case 4
    # inventories["week1"]["camel_case_4"]["problem"],
    # inventories["week1"]["camel_case_4"]["00_10_33"],
    # inventories["week1"]["camel_case_4"]["00_10_44"],
    # inventories["week1"]["camel_case_4"]["00_11_20"],
    # inventories["week1"]["camel_case_4"]["00_12_20"],
    # inventories["week1"]["camel_case_4"]["00_17_56"],
    # inventories["week1"]["camel_case_4"]["00_19_32"],
    # inventories["week1"]["camel_case_4"]["00_19_46"],
    # inventories["week1"]["camel_case_4"]["00_20_02"],
    # inventories["week1"]["camel_case_4"]["00_21_56"],
    # inventories["week1"]["camel_case_4"]["00_23_34"],
    # inventories["week1"]["camel_case_4"]["00_23_47"],
    # inventories["week1"]["camel_case_4"]["00_24_47"],
    # inventories["week1"]["camel_case_4"]["00_25_01"],
    # Divisible sum pairs
    # inventories["week1"]["divisible_sum_pairs"]["problem"],
    # inventories["week1"]["divisible_sum_pairs"]["00_25_39"],
    # inventories["week1"]["divisible_sum_pairs"]["00_26_00"],
    # inventories["week1"]["divisible_sum_pairs"]["00_27_09"],
    # Sparse Arrays
    # inventories["week1"]["sparse_arrays"]["problem"],
    inventories["week1"]["sparse_arrays"]["00_28_09"],
    inventories["week1"]["sparse_arrays"]["00_28_15"],
    inventories["week1"]["sparse_arrays"]["00_28_23"],
    inventories["week1"]["sparse_arrays"]["00_28_34"],
    inventories["week1"]["sparse_arrays"]["00_28_47"],
    inventories["week1"]["sparse_arrays"]["00_28_59"],
]
if __name__ == '__main__':
    voice_generator = VoiceGenerator()

    for target in targets:
        filename = target["filename"]
        text = target["message"]
        voice_generator.generate(text=text, filename=filename)
