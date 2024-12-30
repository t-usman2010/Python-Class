import pyautogui
import time

def auto_type(file_path):
    with open(file_path, 'r') as f:
        text = f.read()

    time.sleep(1)  # Wait for 5 seconds before starting

    for char in text:
        pyautogui.press(char)
        time.sleep(0.1)  # Adjust the delay as needed

# Example usage:
auto_type('message.txt')