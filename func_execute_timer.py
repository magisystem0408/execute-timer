import time

from libs.timer.func_execute_timer import funcExecuteTimer


@funcExecuteTimer
def main():
    print("start process")
    time.sleep(5)


if __name__ == '__main__':
    main()
