from pynput.keyboard import Key, Controller
import keyboard as kb
import time

keyboard = Controller()

# Here you will type the hotkey you will use for the phrase, followed by the phrase in the examples' formats
chats = {
    '-': "This is a custom chat!",
    '=': "This is another custom chat!"



    # Key.f1: "HiHi"
    # As of right now, there is no way to bind chats to function keys or special keys like shift, space, enter, esc, etc.
}

# --------------- You don't need to edit anything below this comment ---------------

last_send_time = 0
min_send_interval = 0.2           # Minimum interval to send chats to prevent double sending

# Types phrase in chat very quickly, simulating a quick chat
def say(phrase):
    global last_send_time
    current_time = time.time()

    if current_time - last_send_time >= min_send_interval:
        keyboard.press('/')           # <-- if '/' isn't your chat button, change it to your chat button
        keyboard.release('/')
        time.sleep(0.001)             # <-- time sleep to wait for the chatbox to open in game
        keyboard.type(f" {phrase}")   # <-- have to add whitespace before the phrase variable or it will cut off first letter (idk why)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

        last_send_time = current_time


while True:
    for key, phrase in chats.items():
        if kb.is_pressed(key):
            say(phrase)
