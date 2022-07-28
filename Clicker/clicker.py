import threading
import time

from pynput.keyboard import Listener, KeyCode
from pynput.mouse import Button, Controller

# KeyCode to control Clicker
start_and_stop_key_code = KeyCode(char='s')
exit_key_code = KeyCode(char='q')
# Setting for details
delay = 0.001
num_of_clicking = 10


class Clicker(threading.Thread):
    def __init__(self):
        super(Clicker, self).__init__()
        self.running = False
        self.program_running = True
        self.clicked_cnt = 0

    def start_clicking(self):
        print("Start clicking...")
        self.running = True
        self.clicked_cnt = 0

    def stop_clicking(self):
        print("Stopped clicking!")
        self.running = False

    def exit(self):
        self.stop_clicking()
        print("Exit Clicker!")
        self.program_running = False

    def run(self) -> None:
        while self.program_running:
            while self.running and self.clicked_cnt < num_of_clicking:
                mouse.click(Button.left)
                time.sleep(delay)
                self.clicked_cnt += 1

                if self.clicked_cnt == num_of_clicking:
                    self.stop_clicking()
            time.sleep(0.1)


mouse = Controller()
clicker = Clicker()
clicker.start()


def on_press(key):
    if key == start_and_stop_key_code:
        if clicker.running:
            clicker.stop_clicking()
        else:
            clicker.start_clicking()
    elif key == exit_key_code:
        clicker.exit()
        listener.stop()


with Listener(on_press=on_press) as listener:
    listener.join()
