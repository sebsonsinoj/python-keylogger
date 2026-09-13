# python keylogger

a simple educational keylogger written in python that records keyboard input along with timestamps.

## features

* monitors keyboard input using the `pynput` library
* records the time each key is pressed
* records normal and special keys separately
* saves recorded key presses to a text file
* displays recorded key presses in the console
* stops recording when the Escape key is pressed
* uses a `.pyw` file so the program can run without opening a standard console window

## how it works

the program uses the `pynput` library to listen for keyboard events.

when a key is pressed, the program records the current date and time and writes the key press to `keylog.txt`.

normal keys such as letters and numbers are recorded using their character value, while special keys such as Shift, Enter and Escape are recorded separately.

pressing the Escape key stops the keyboard listener and ends the keylogging process.

## files

* `keylogger.pyw` — the main Python program
* `keylog.txt` — stores the recorded keyboard input and timestamps

## technologies used

* python
* `pynput`
* `datetime`
* file handling

## what i learned

this project helped me understand event-driven programming and how keyboard events can be detected and handled in python.

i also practised using functions, exception handling, file handling, timestamps and external python libraries.

## how to run

1. install Python
2. install the `pynput` library
3. open `keylogger.pyw`
4. the program will begin listening for keyboard input
5. press the Escape key to stop the keylogger

## example output

```text
[2026-09-13 14:30:12] Key h pressed
[2026-09-13 14:30:13] Key i pressed
[2026-09-13 14:30:15] Special key Key.space pressed
```

## disclaimer

this project is for educational purposes only. a keylogger should only be used on systems where you have permission to monitor keyboard input. do not use it to collect passwords, personal information or other sensitive data from other people.
