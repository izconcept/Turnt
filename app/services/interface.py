import time
import pyautogui

def typer(command):
    pyautogui.typewrite(command)
    pyautogui.typewrite('\n')


def open_valve(axis, step):
    typer("G91G0" + axis + "-" + str(step))


def close_valve(axis, step):
    typer("G91G0" + axis + str(step))


def give_me_some_white_bottle(duration):
    if duration == 0:
        return
    open_valve("X", 3)
    time.sleep(duration)
    close_valve("X", 3)


def give_me_some_green_bottle(duration):
    if duration == 0:
        return
    close_valve("Y", 3)
    time.sleep(duration)
    open_valve("Y", 3)

def give_me_some_rear_bottle(duration):
    if duration == 0:
        return
    close_valve("Z", 3)
    time.sleep(duration)
    open_valve("Z", 3)


time.sleep(5)

