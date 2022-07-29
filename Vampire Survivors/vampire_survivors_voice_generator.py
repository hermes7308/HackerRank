from common.voice_generator import VoiceGenerator

inventories = {
    "00_00_04": {
        "filename": "Vampire Survivor Gold cheat and Python Egg Clicker 00_00_04",
        "message": """
            공부만 하기 지겨우니까 우리 게임 한판 할까요?
        """
    },
    "00_00_07": {
        "filename": "Vampire Survivor Gold cheat and Python Egg Clicker 00_00_07",
        "message": """
            최근 제가 좋아하는 게임이 하나 생겼습니다.
            Steam 에서 판매하고 있는 Vampire Survivors 라는 게임입니다.
            딱, 한판만 하고 다시 공부를 하죠.
        """
    },
    "00_00_11": {
        "filename": "Vampire Survivor Gold cheat and Python Egg Clicker 00_00_11",
        "message": """
            또, 제가 컨트롤 하나는 죽여주거든요.
            손 끝에서 나오는 그 현란함.
        """
    },
    "00_00_16": {
        "filename": "Vampire Survivor Gold cheat and Python Egg Clicker 00_00_16",
        "message": """
            보이시나요? 저의 현란한 컨트롤?
        """
    },
    "00_00_23": {
        "filename": "Vampire Survivor Gold cheat and Python Egg Clicker 00_00_23",
        "message": """
            아이 씨...
        """
    },
    "00_00_26": {
        "filename": "Vampire Survivor Gold cheat and Python Egg Clicker 00_00_26",
        "message": """
            아이 X발...
        """
    },
    "00_00_30": {
        "filename": "Vampire Survivor Gold cheat and Python Egg Clicker 00_00_30",
        "message": """
            아이 니X...
        """
    },
    "00_00_32": {
        "filename": "Vampire Survivor Gold cheat and Python Egg Clicker 00_00_32",
        "message": """
            아이 X미...
        """
    },
    "00_00_39": {
        "filename": "Vampire Survivor Gold cheat and Python Egg Clicker 00_00_39",
        "message": """
            아이 X같네...
        """
    },
    "00_00_42": {
        "filename": "Vampire Survivor Gold cheat and Python Egg Clicker 00_00_42",
        "message": """
            우리는 개발자니까 개발자스럽게 놀아볼까요?
        """
    },
    "00_00_46": {
        "filename": "Vampire Survivor Gold cheat and Python Egg Clicker 00_00_46",
        "message": """
            먼저, Vampire Survivors 를 종료합니다.
            그 후, 화면에 보이는 Vampire Survivor 설정 파일을 오픈합니다.
            변경 전, 원본 파일을 백업하는 것을 잊지마세요.
        """
    },
    "00_00_49": {
        "filename": "Vampire Survivor Gold cheat and Python Egg Clicker 00_00_49",
        "message": """
            main.bundle.js 파일에서 Ctrl + F 를 사용하여 CoinGold를 검색합니다.
        """
    },
    "00_00_52": {
        "filename": "Vampire Survivor Gold cheat and Python Egg Clicker 00_00_52",
        "message": """
            검색이 되면 화면에서 보이는 value 값을 원하는 값으로 수정해 줍니다.
        """
    },
    "00_00_54": {
        "filename": "Vampire Survivor Gold cheat and Python Egg Clicker 00_00_54",
        "message": """
            저는 여기서, value 값을 100,000 으로 변경 할게요.
        """
    },
    "00_00_59": {
        "filename": "Vampire Survivor Gold cheat and Python Egg Clicker 00_00_59",
        "message": """
            다시, Vampire Survivors 를 실행합니다.
        """
    },
    "00_01_17": {
        "filename": "Vampire Survivor Gold cheat and Python Egg Clicker 00_01_17",
        "message": """
            기본 값이 1이었던 코인을 먹으면, 화면에 보이는 것과 같이 돈이 엄청나게 증가하는 것을 볼 수 있습니다.
        """
    },
    "00_01_59": {
        "filename": "Vampire Survivor Gold cheat and Python Egg Clicker 00_01_59",
        "message": """
            충분히 돈을 벌었으니, 이제 Egg 를 구매하여 캐릭터를 강화해볼까요?
        """
    },
    "00_02_11": {
        "filename": "Vampire Survivor Gold cheat and Python Egg Clicker 00_02_11",
        "message": """
            2000개 정도의 Egg 를 사려고 하는데, 클릭하기가 너무 힘드네요.
        """
    },
    "00_02_17": {
        "filename": "Vampire Survivor Gold cheat and Python Egg Clicker 00_02_17",
        "message": """
            자동으로 클릭하는 프로그램을 만들어 봅시다.
        """
    },
    "00_02_25": {
        "filename": "Vampire Survivor Gold cheat and Python Egg Clicker 00_02_25",
        "message": """
            먼저, Thread 를 사용해야 합니다.
            threading 을 import 해줍니다.
        """
    },
    "00_02_34": {
        "filename": "Vampire Survivor Gold cheat and Python Egg Clicker 00_02_34",
        "message": """
            그리고, Keyboard 입력과 Mouse 출력을 다루기 위해 Package 를 같이 추가합니다.
        """
    },
    "00_03_03": {
        "filename": "Vampire Survivor Gold cheat and Python Egg Clicker 00_03_03",
        "message": """
            Clicking 을 실행 및 정지에 사용할 Key를 설정합니다.
        """
    },
    "00_03_16": {
        "filename": "Vampire Survivor Gold cheat and Python Egg Clicker 00_03_16",
        "message": """
            저는, "s" 를 사용하겠습니다.
        """
    },
    "00_03_22": {
        "filename": "Vampire Survivor Gold cheat and Python Egg Clicker 00_03_22",
        "message": """
            Clicker 프로그램을 종료할 때 사용할 Key를 설정합니다.
        """
    },
    "00_03_27": {
        "filename": "Vampire Survivor Gold cheat and Python Egg Clicker 00_03_27",
        "message": """
            저는, "ESC" 를 사용하겠습니다.
        """
    },
    "00_03_36": {
        "filename": "Vampire Survivor Gold cheat and Python Egg Clicker 00_03_36",
        "message": """
            Mouse 클릭 사이의 간격을 delay 로 지정합니다.
            여기서, 저는 0.001 초로 설정하겠습니다.
        """
    },
    "00_03_40": {
        "filename": "Vampire Survivor Gold cheat and Python Egg Clicker 00_03_40",
        "message": """
            그리고, 마우스를 몇번을 클릭해야 하는지 값을 설정합니다.
        """
    },
    "00_03_46": {
        "filename": "Vampire Survivor Gold cheat and Python Egg Clicker 00_03_46",
        "message": """
            저는 2000번 정도 클릭할게요.
        """
    },
    "00_03_56": {
        "filename": "Vampire Survivor Gold cheat and Python Egg Clicker 00_03_56",
        "message": """
            Class 를 생성시 Thread 를 상속 받습니다.
        """
    },
    "00_04_08": {
        "filename": "Vampire Survivor Gold cheat and Python Egg Clicker 00_04_08",
        "message": """
            내부에서 사용할 변수들,
            running 은 False,
            program running 은 True,
            clicked count 는 0 으로 초기화 해줍니다.
        """
    },
    "00_04_28": {
        "filename": "Vampire Survivor Gold cheat and Python Egg Clicker 00_04_28",
        "message": """
            Clicking 을 시작하는 Method 를 생성합니다.
            Method 호출시 running 변수는 True,
            clicked count 는 0 으로 초기화 합니다.            
        """
    },
    "00_04_56": {
        "filename": "Vampire Survivor Gold cheat and Python Egg Clicker 00_04_56",
        "message": """
            Clicking 을 정지하는 Method 를 생성합니다.
            Method 호출시 running 은 False 로 값을 변경해 줍니다.
        """
    },
    "00_05_19": {
        "filename": "Vampire Survivor Gold cheat and Python Egg Clicker 00_05_19",
        "message": """
            전체 프로그램을 종료할 Method 를 생성합니다.
            내부에서는 stop clicking Method를 호출하고, 
            program running 변수를 False 로 설정합니다.
        """
    },
    "00_05_47": {
        "filename": "Vampire Survivor Gold cheat and Python Egg Clicker 00_05_47",
        "message": """
            다음은 프로그램 실행부분 입니다.
            Thread 를 상속하기 때문에, run Method에 실행 코드을 넣어주면 됩니다. 
        """
    },
    "00_05_54": {
        "filename": "Vampire Survivor Gold cheat and Python Egg Clicker 00_05_54",
        "message": """
            program running 변수가 True 일 경우 반복문을 실행합니다.
        """
    },
    "00_05_58": {
        "filename": "Vampire Survivor Gold cheat and Python Egg Clicker 00_05_58",
        "message": """
            running 변수가 True 이고 clicked count 가 목표치에 도달하지 못할 경우 반복하여 실행합니다.
        """
    },
    "00_06_21": {
        "filename": "Vampire Survivor Gold cheat and Python Egg Clicker 00_06_21",
        "message": """
            지속적으로 Mouse 왼쪽 버튼을 클릭합니다.
        """
    },
    "00_06_41": {
        "filename": "Vampire Survivor Gold cheat and Python Egg Clicker 00_06_41",
        "message": """
            위에서 설정한 delay 만큼 sleep 을 실행합니다.
        """
    },
    "00_06_47": {
        "filename": "Vampire Survivor Gold cheat and Python Egg Clicker 00_06_47",
        "message": """
            clicked count 를 1증가 시킵니다.
        """
    },
    "00_06_51": {
        "filename": "Vampire Survivor Gold cheat and Python Egg Clicker 00_06_51",
        "message": """
            만약, clicked count 가 요청치에 도달하면, clicking 을 정지 시킵니다.
        """
    },
    "00_07_09": {
        "filename": "Vampire Survivor Gold cheat and Python Egg Clicker 00_07_09",
        "message": """
            Clicker 객체를 생성합니다.
        """
    },
    "00_07_14": {
        "filename": "Vampire Survivor Gold cheat and Python Egg Clicker 00_07_14",
        "message": """
            Clicker 를 실행합니다.
        """
    },
    "00_07_18": {
        "filename": "Vampire Survivor Gold cheat and Python Egg Clicker 00_07_18",
        "message": """
            Keyboard 입력을 받을 Listener를 생성합니다.
        """
    },
    "00_07_30": {
        "filename": "Vampire Survivor Gold cheat and Python Egg Clicker 00_07_30",
        "message": """
            위에서 설정한 KeyCode 를 사용하여, 입력시 행동을 지정합니다.
        """
    },
    "00_08_45": {
        "filename": "Vampire Survivor Gold cheat and Python Egg Clicker 00_08_45",
        "message": """
            이제 프로그램을 실행해 볼까요?
        """
    },
    "00_09_02": {
        "filename": "Vampire Survivor Gold cheat and Python Egg Clicker 00_09_02",
        "message": """
            프로그램이 잘 작동하네요. 하하하.
        """
    },
    "00_09_29": {
        "filename": "Vampire Survivor Gold cheat and Python Egg Clicker 00_09_29",
        "message": """
            Egg 는 바로 적용이 되지 않기 때문에, 다시 실행합니다.
        """
    },
    "00_09_53": {
        "filename": "Vampire Survivor Gold cheat and Python Egg Clicker 00_09_53",
        "message": """
            보이시나요? 투사체의 크기, 속도, 갯수가 엄청나게 늘어났죠?
        """
    },
    "00_09_56": {
        "filename": "Vampire Survivor Gold cheat and Python Egg Clicker 00_09_56",
        "message": """
            이제 저의 컨트롤로 사냥하는 모습을 감상하시죠.
        """
    },
    "00_15_05": {
        "filename": "Vampire Survivor Gold cheat and Python Egg Clicker 00_15_05",
        "message": """
            끝까지 시청해주셔서 감사합니다.
        """
    },
}

# targets = [inventories[key] for key in inventories.keys()]
targets = [
    inventories["00_00_11"],
    # inventories["00_02_25"],
    # inventories["00_02_34"],
    # inventories["00_15_05"],
]
if __name__ == '__main__':
    voice_generator = VoiceGenerator()

    for target in targets:
        filename = target["filename"]
        text = target["message"]
        voice_generator.generate(text=text, filename=filename)
