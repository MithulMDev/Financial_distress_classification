# mouse_keyboard_activity.py

import random
import time
import threading
import pyautogui

# Mouse Activity
screenWidth, screenHeight = pyautogui.size()

def move_mouse():
    x = random.randint(0, screenWidth)
    y = random.randint(0, screenHeight)
    pyautogui.moveTo(x, y, duration=random.uniform(0.2, 0.5))

def random_click():
    x = random.randint(0, screenWidth)
    y = random.randint(0, screenHeight)
    pyautogui.moveTo(x, y, duration=random.uniform(0.2, 0.5))
    pyautogui.click()

def simulate_mouse_activity():
    try:
        while True:
            move_mouse()
            time.sleep(random.randint(5, 15))  # Move cursor every 5 to 15 seconds
            if random.random() < 0.3:  # 30% chance to click
                random_click()
                time.sleep(random.uniform(2, 5))  # Small delay after clicking
    except KeyboardInterrupt:
        pass

# Keyboard Activity
def type_text():
    text = ["test", "dummy", "sample"]
    pyautogui.typewrite(random.choice(text), interval=random.uniform(0.05, 0.1))

def simulate_keyboard_activity():
    try:
        while True:
            type_text()
            time.sleep(random.randint(30, 120))  # Type text every 30 to 120 seconds
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    mouse_thread = threading.Thread(target=simulate_mouse_activity)
    keyboard_thread = threading.Thread(target=simulate_keyboard_activity)

    mouse_thread.start()
    keyboard_thread.start()

    mouse_thread.join()
    keyboard_thread.join()
