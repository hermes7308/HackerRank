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
            "go_to_next_problem": {
                "filename": "[Common] Go to a next problem",
                "message": "다음 문제로 넘어가 볼까요?"
            },
        },
    },
    # introduction
    "introduction": {
        "00_00_04": {
            "filename": "[HackerRank] 3 Months Preparation Kit, Introduction, 00_00_04",
            "message": """
                안녕하세요. 비비빅 TV에 비기 입니다.
                저에 대해서 간단히 설명하자면, 저는 한국에서 2년 정도 개발자로 일을 했습니다.
                그 후, 미국으로 이민오게 되었고, 미국에 있는 한국회사에서 2년 정도 일을 하게되었습니다.
                될 수 있으면, 미국에 있는 한국회사는 절대 가지 마세요.
                거의 대부분의 미국에 있는 한국 회사는 배울것도 없고, 개발자의 미래에 크게 도움이 되지 않습니다.
                한국에서 유명한 S 기업이나 L 기업이라고 해도 별반 다르지 않습니다.
                개발자로 4년 정도 일을 해오면서, 거의 모든 프로젝트들이 웹 기반으로 하는 Front end, Back end 시스템을 개발해왔는데, 
                해당 일이 너무 지겨워 졌습니다.
                Database에 데이터를 넣었다 뺐다, 복잡하게 굴러가는 시스템, 분석하고 개발하는 일 더이상 하기 싫어졌습니다.
                그 회사에서 하는 일이 도저히 저와 맞지 않아, 회사를 그만두고, Los Angeles 근처이 있는 대학원에 다니면서, 구직활동을 하다,
                몇일 뒤부터 미국회사에서 일을 하게 되었습니다.
            """
        },
        "00_01_14": {
            "filename": "[HackerRank] 3 Months Preparation Kit, Introduction, 00_01_14",
            "message": """
                개발자로 일을 하면서, Algorithm을 잘 안다고 생각했습니다.
                막상, 인터뷰 및 코딩 테스트를 진행하면서, 부족한 점을 많이 느끼게 되었고, Algorithm 공부를 다시 해야겠다고 생각하게되었습니다.
                모든 개발자들이 저와 같지 않겠지만, 저와 유사한 환경에 있으신 분들, 구직활동을 준비하시는 분들에게,
                조금이나마 도움이 되었으면 하는 마음에 해당 영상을 제작하게 되었습니다.
            """
        },
        "00_01_47": {
            "filename": "[HackerRank] 3 Months Preparation Kit, Introduction, 00_01_47",
            "message": """
                지금 화면에 보이는 회사들은 한국에서도 한번쯤 들어보셨을 회사들이죠?
                해당 회사들은 저의 선호도에 따라 나눈 회사입니다.
                시청자 분들도, 본인만의 목표하는 회사를 설정해두고, 공부하시는 것은 어떨까요?
                회사마다 선호하는 인터뷰 스킬이나 알고리즘 문제들이 있기 때문에, 
                목표를 설정해 두고, 거기에 Focus 해서 준비를 하면 도움이 될것 같습니다.
            """
        },
        "00_02_16": {
            "filename": "[HackerRank] 3 Months Preparation Kit, Introduction, 00_02_16",
            "message": """
                제가 미국에서 구직활동을 하면서, 배우게 된 것은, 
                Amazon이나 Tesla 등 에서는 HackerRank 또는 이와 유사한 시스템을 이용해서, 코딩 테스트를 진행합니다.
            """
        },
        "00_02_31": {
            "filename": "[HackerRank] 3 Months Preparation Kit, Introduction, 00_02_31",
            "message": """
                HackerRank 에서는 다양한 알고리즘 문제들을 제공합니다.
                앞으로 영상에서는 주어진 Topic 에대한 설명 및 풀이를 할 예정입니다.
                구성은 13주로 나누어져 있습니다.
                해당 영상이 공부 또는 취업 하시는데, 도움이 되었으면 합니다.
                많이 부족하지만 좋게 봐주세요.
                감사합니다.
            """
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
    },
    "week2": {
        "lonely_integer": {
            "free_talking": {
                "filename": "[HackerRank] 3 Months Preparation Kit, Week 2, Lonely Integer free_talking",
                "message": """
                    Hacker Rank, 3 개월 과정 두번째 주 입니다.
                    그럼, 시작해볼까요?
                """
            },
            "problem": {
                "filename": "[HackerRank] 3 Months Preparation Kit, Week 2, Lonely Integer problem",
                "message": """
                    문제, Lonely Integer
                """
            },
            "summary": {
                "filename": "[HackerRank] 3 Months Preparation Kit, Week 2, Lonely Integer summary",
                "message": """
                    주어진 정수형 배열에서 unique 한 변수를 찾는 algorithm 을 작성하시오.
                """
            },
            "00_00_33": {
                "filename": "[HackerRank] 3 Months Preparation Kit, Week 2, Lonely Integer 00_00_33",
                "message": """
                    먼저, 주어진 배열 안에 있는 값을 계산할 map 또는 dictionary 을 만듭니다. 
                """
            },
            "00_00_40": {
                "filename": "[HackerRank] 3 Months Preparation Kit, Week 2, Lonely Integer 00_00_40",
                "message": """
                    배열 안에 있는 값을 하나씩 가져와, map 에 넣어 줍니다.
                    만약, map 에 이미 존재할 경우, count 갯수를 1 증가 시키고,
                    없을 경우 해당 key 에 1을 넣어 줍니다.
                """
            },
            "00_01_07": {
                "filename": "[HackerRank] 3 Months Preparation Kit, Week 2, Lonely Integer 00_01_07",
                "message": """
                    count map 에서 값이 1 인 숫자를 찾습니다.
                    해당 값이 1 인 경우, unique한 변수 입니다.
                """
            },
            "00_01_34": {
                "filename": "[HackerRank] 3 Months Preparation Kit, Week 2, Lonely Integer 00_01_34",
                "message": """
                    만약, unique 변수가 없다면, None 을 반환합니다.
                """
            },
        },
        "grading_students": {
            "problem": {
                "filename": "[HackerRank] 3 Months Preparation Kit, Week 2, Grading Students problem",
                "message": """
                    문제, Grading Students
                """
            },
            "summary": {
                "filename": "[HackerRank] 3 Months Preparation Kit, Week 2, Grading Students summary",
                "message": """
                    학생의 성적을 계산하는 문제입니다.
                    점수가 40 보다 크고, 성적을 5로 나누었을때, 나머지가 2 이하인 경우 반올림 합니다..
                    점수가 40 보다 작으면, 40 을 반환 합니다.
                """
            },
            "00_03_00": {
                "filename": "[HackerRank] 3 Months Preparation Kit, Week 2, Grading Students 00_03_00",
                "message": """
                    먼저, 성적이 저장되어 있는 배열의 Index 를 가져옵니다.
                    그 후, 해당 Index 를 이용하여 grade 를 가져옵니다.
                    만약, grade 가 38 보다 작으면, 그 성적에 수정이 필요하지 않습니다.
                    그리고, grade 를 5로 나눈 몫을 구하고, 
                    만약, grade 가 5로 나누어 떨어지지 않으면, 몫에 1을 추가합니다.
                    마지막으로, 몫에 5를 곱한 값을 rounded grade 변수에 저장을 하고, 
                    그 변수 값과 기존의 변수 값의 차이가 3 보다 작으면, 
                    반올림된 값으로 성적을 수정합니다.
                    그리고, 변경된 성적 배열을 반환합니다.
                """
            },
            "00_04_37": {
                "filename": "[HackerRank] 3 Months Preparation Kit, Week 2, Grading Students 00_04_37",
                "message": """
                    그리고, 변경된 성적 배열을 반환합니다.
                """
            },
        },
        "flipping_bits": {
            "problem": {
                "filename": "[HackerRank] 3 Months Preparation Kit, Week 2, Flipping bits problem",
                "message": """
                    문제, Flipping bits
                """
            },
            "summary": {
                "filename": "[HackerRank] 3 Months Preparation Kit, Week 2, Flipping bits summary",
                "message": """
                    주어진 32 비트 unsigned integer 를 flip 하시오. (1 -> 0 and 0 -> 1)
                    그리고, 그 결과를 unsigned integer 로 반환하시오.
                """
            },
            "00_05_39": {
                "filename": "[HackerRank] 3 Months Preparation Kit, Week 2, Flipping bits 00_05_39",
                "message": """
                    먼저, 정수를 binary 문자열로 변경해줍니다.
                """
            },
            "00_05_53": {
                "filename": "[HackerRank] 3 Months Preparation Kit, Week 2, Flipping bits 00_05_53",
                "message": """
                    결과를 반환할 빈 문자열을 만들어 줍니다.
                """
            },
            "00_05_58": {
                "filename": "[HackerRank] 3 Months Preparation Kit, Week 2, Flipping bits 00_05_58",
                "message": """
                    각 비트의 값을 가져와, 만약 1이면, 결과값에 0을 추가하고, 반대의 경우 1을 추가합니다.
                """
            },
            "00_06_52": {
                "filename": "[HackerRank] 3 Months Preparation Kit, Week 2, Flipping bits 00_06_52",
                "message": """
                    마지막으로, 결과값을 반환할 때, 문자열 binary 를 정수로 변환합니다.
                """
            },
        },
        "diagonal_difference": {
            "problem": {
                "filename": "[HackerRank] 3 Months Preparation Kit, Week 2, Diagonal Difference problem",
                "message": """
                    문제, Diagonal Difference
                """
            },
            "summary": {
                "filename": "[HackerRank] 3 Months Preparation Kit, Week 2, Diagonal Difference summary",
                "message": """
                    주어진 정사각형 matrix 의 대각선을 계산하는 문제입니다.
                    왼쪽에서 오른쪽 대각선의 합과 오른쪽에서 왼쪽 대각선의 합의 차를 구해야합니다.
                    값은 절대값으로 반환합니다.
                """
            },
            "00_07_48": {
                "filename": "[HackerRank] 3 Months Preparation Kit, Week 2, Diagonal Difference 00_07_48",
                "message": """
                    먼저, 왼쪽 상단에서 오른쪽 하단으로 내려가는 대각선의 합을 저장할 변수를 초기화 합니다. 
                """
            },
            "00_07_55": {
                "filename": "[HackerRank] 3 Months Preparation Kit, Week 2, Diagonal Difference 00_07_55",
                "message": """
                    그리고, matrix 에서 해당 변수를 가져와 더해줍니다.
                """
            },
            "00_08_27": {
                "filename": "[HackerRank] 3 Months Preparation Kit, Week 2, Diagonal Difference 00_08_27",
                "message": """
                    이전과 같이 오른쪽 상단에서 왼쪽 하단으로 내려가는 대각선의 합을 저장할 변수를 초기화 합니다. 
                """
            },
            "00_08_35": {
                "filename": "[HackerRank] 3 Months Preparation Kit, Week 2, Diagonal Difference 00_08_35",
                "message": """
                    그리고, matrix 에서 해당 변수를 가져와 더해줍니다.
                """
            },
            "00_09_04": {
                "filename": "[HackerRank] 3 Months Preparation Kit, Week 2, Diagonal Difference 00_09_04",
                "message": """
                    마지막으로, 이전에 계산한 두 합 변수 차의 절대값을 반환합니다.
                """
            },
        },
        "counting_sort_1": {
            "problem": {
                "filename": "[HackerRank] 3 Months Preparation Kit, Week 2, Counting Sort 1 problem",
                "message": """
                    문제, Counting Sort 1
                """
            },
            "summary": {
                "filename": "[HackerRank] 3 Months Preparation Kit, Week 2, Counting Sort 1 summary",
                "message": """
                    Comparison 이 없는 sorting 알고리즘을 작성하시오.
                    즉, CountingSort 를 개발해야 합니다.
                """
            },
            "00_10_09": {
                "filename": "[HackerRank] 3 Months Preparation Kit, Week 2, Counting Sort 1 00_10_09",
                "message": """
                    먼저, Counting Sort 에 사용할 배열을 0으로 초기화 합니다.
                    숫자는 100이하로 정해져 있으니 배열 크기를 100으로 생성합니다. 
                """
            },
            "00_10_38": {
                "filename": "[HackerRank] 3 Months Preparation Kit, Week 2, Counting Sort 1 00_10_38",
                "message": """
                    입력 받은 배열의 값은 결과값의 Index 에 해당합니다.
                    따라서, 각 배열 변수의 값을 이용하여 Index 에 값을 계산합니다.
                """
            },
            "00_11_10": {
                "filename": "[HackerRank] 3 Months Preparation Kit, Week 2, Counting Sort 1 00_11_10",
                "message": """
                    마지막으로 계산이 완료된 결과값을 반환합니다.
                """
            },
        },
        "counting_valleys": {
            "problem": {
                "filename": "[HackerRank] 3 Months Preparation Kit, Week 2, Counting Valleys problem",
                "message": """
                    문제, Counting Valleys
                """
            },
            "summary": {
                "filename": "[HackerRank] 3 Months Preparation Kit, Week 2, Counting Valleys summary",
                "message": """
                    계곡 아래로 내려 갔다가 올라올 때, sea level 에 도달한 횟수를 계산 하시오.
                """
            },
            "00_12_00": {
                "filename": "[HackerRank] 3 Months Preparation Kit, Week 2, Counting Valleys 00_12_00",
                "message": """
                    먼저, 현재 level 과 계곡 갯수를 초기화 합니다.
                """
            },
            "00_12_15": {
                "filename": "[HackerRank] 3 Months Preparation Kit, Week 2, Counting Valleys 00_12_15",
                "message": """
                    그리고, 만약 각 step 이 "U" 이면, 현재 level 을 1 증가시키고, 
                    증가된 값이 sea level, 즉, 0 이면, 계곡 갯수를 1 증가시킵니다.
                """
            },
            "00_13_19": {
                "filename": "[HackerRank] 3 Months Preparation Kit, Week 2, Counting Valleys 00_13_19",
                "message": """
                    반대의 경우, 각 step 이 "D" 이면, 현재 level 을 1 감소시킵니다.
                """
            },
            "00_13_33": {
                "filename": "[HackerRank] 3 Months Preparation Kit, Week 2, Counting Valleys 00_13_33",
                "message": """
                    마지막으로 계산된 계곡 갯수를 반환합니다.
                """
            },
        },
        "pangrams": {
            "problem": {
                "filename": "[HackerRank] 3 Months Preparation Kit, Week 2, Pangrams problem",
                "message": """
                    문제, Pangrams
                """
            },
            "summary": {
                "filename": "[HackerRank] 3 Months Preparation Kit, Week 2, Pangrams summary",
                "message": """
                    해당 문제는 주어진 문자열에 포함 되어 있는 문자가 모든 alphabet 을 포함 하고 있는지 확인 하는 문제 입니다.
                """
            },
            "00_14_42": {
                "filename": "[HackerRank] 3 Months Preparation Kit, Week 2, Pangrams 00_14_42",
                "message": """
                    먼저, alphabet ASCII 코드 배열을 생성합니다.
                """
            },
            "00_15_25": {
                "filename": "[HackerRank] 3 Months Preparation Kit, Week 2, Pangrams 00_15_25",
                "message": """
                    그리고, 문자열에서 각 문자를 가져와 
                    그 문자의 ASCII 코드가 alphabet 배열에 포함되어 있으면,
                    해당 문자를 배열에서 제거합니다.
                """
            },
            "00_16_04": {
                "filename": "[HackerRank] 3 Months Preparation Kit, Week 2, Pangrams 00_16_04",
                "message": """
                    마지막으로 alphabet 배열의 길이가 0보다 크면,
                    문자열 "not pangram" 을 반환하고,
                    0이면, "pangram" 을 반환합니다.
                """
            },
            "00_16_34": {
                "filename": "[HackerRank] 3 Months Preparation Kit, Week 2, Pangrams 00_16_34",
                "message": """
                    앗! 문제가 생겼습니다.
                    그 이유는 대문자 alphabet 과 소문자 alphabet 의 ASCII 코드는 다르기 때문입니다.
                    입력 받은 문자열을 소문자로 변경해야합니다.
                """
            },
        },
        "mars_exploration": {
            "problem": {
                "filename": "[HackerRank] 3 Months Preparation Kit, Week 2, Mars Exploration problem",
                "message": """
                    문제, Mars Exploration
                """
            },
            "summary": {
                "filename": "[HackerRank] 3 Months Preparation Kit, Week 2, Mars Exploration summary",
                "message": """
                    지구로 보내는 SOS 신호를 확인 하고, 그 신호가 얼마나 변형 되었는지 계산하는 문제입니다.
                """
            },
            "00_18_11": {
                "filename": "[HackerRank] 3 Months Preparation Kit, Week 2, Mars Exploration 00_18_11",
                "message": """
                    먼저, 전체 문자열의 SOS 갯수를 구합니다.
                    SOS 의 크기는 3 이기 때문에, 전체 문자열 길이를 3으로 나누어 줍니다.
                """
            },
            "00_18_28": {
                "filename": "[HackerRank] 3 Months Preparation Kit, Week 2, Mars Exploration 00_18_28",
                "message": """
                    그리고, 변형된 문자의 갯수를 저장할 변수를 초기화 합니다.
                """
            },
            "00_18_36": {
                "filename": "[HackerRank] 3 Months Preparation Kit, Week 2, Mars Exploration 00_18_36",
                "message": """
                    이전에 구한 전체 SOS 갯수 만큼 반복하여 변형된 문자를 찾습니다.
                    SOS 문자열의 0 index 는 첫번째 "S" 문자,
                    1 index 는 "O" 문자이고, 2 index 는 마지막 "S" 문자입니다.
                    각 문자를 비교하여 같지 않을 경우, 
                    변형된 문자 갯수를 저장하는 변수의 값을 1 증가 시킵니다.
                """
            },
            "00_19_50": {
                "filename": "[HackerRank] 3 Months Preparation Kit, Week 2, Mars Exploration 00_19_50",
                "message": """
                    마지막으로 계산이 완료된 변형 문자 갯수를 반환합니다.
                """
            },
            "00_20_27": {
                "filename": "[HackerRank] 3 Months Preparation Kit, Week 2, Mars Exploration 00_20_27",
                "message": """
                    지금까지 시청해주셔서 감사합니다.
                    앞으로 더 좋은 영상으로 찾아뵙겠습니다.
                """
            },
        }
    }
}

targets = [
    # week2
    # inventories["week2"]["pangrams"]["00_16_04"],
    # inventories["week2"]["pangrams"]["00_16_34"],
    # inventories["week2"]["mars_exploration"]["problem"],
    # inventories["week2"]["mars_exploration"]["summary"],
    # inventories["week2"]["mars_exploration"]["00_18_11"],
    # inventories["week2"]["mars_exploration"]["00_18_28"],
    # inventories["week2"]["mars_exploration"]["00_18_36"],
    # inventories["week2"]["mars_exploration"]["00_19_50"],
    inventories["week2"]["mars_exploration"]["00_20_27"],
]
if __name__ == '__main__':
    voice_generator = VoiceGenerator()

    for target in targets:
        filename = target["filename"]
        text = target["message"]
        voice_generator.generate(text=text, filename=filename)
