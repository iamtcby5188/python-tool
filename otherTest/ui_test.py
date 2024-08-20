# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import uiautomation as autoto
import _thread
import time
import pythoncom


def doUIA(threadName, delay):
    try:
        print(f'{threadName} begin..')
        pythoncom.CoInitialize()

        _uia = autoto.GetRootControl()

        print(f'{threadName} end..')
    except Exception as a:
        print(a)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    try:

        _thread.start_new_thread(doUIA, ("Thread-1", 2,))
        time.sleep(10)
        _thread.start_new_thread(doUIA, ("Thread-2", 4,))
        time.sleep(10)
        _thread.start_new_thread(doUIA, ("Thread-3", 5,))
        time.sleep(10)
    except Exception as a:
        print(a)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
