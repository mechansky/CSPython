
import os
import signal
import stat
import subprocess
import sys
import time
from time import sleep


PYTHON_PATH = sys.executable
BASE_PATH = os.path.dirname(os.path.abspath(__file__))
CLIENTS_COUNT = 1


def get_subprocess(file_name, args=''):

    time.sleep(0.5)
    file_full_path = f"{BASE_PATH}/{file_name}"

    with open("start_node.command", "w") as f:
        f.write(f'#!/bin/sh\npython3 "{file_full_path}" {args}')
    os.chmod("start_node.command", stat.S_IRWXU)
    return subprocess.Popen(['/usr/bin/open', '-n', '-a', 'Terminal', 'start_node.command'], shell=False)


P_LIST = []
while True:
    TEXT_FOR_INPUT = f"Запустить {CLIENTS_COUNT} клиентов (s) / Закрыть клиентов (x) / Выйти (q): "
    USER = input(TEXT_FOR_INPUT)

    if USER == "q":
        break
    elif USER == "s":

        # P_LIST.append(get_subprocess("server.py"))
        time.sleep(0.5)
        for i in range(CLIENTS_COUNT):
            P_LIST.append(get_subprocess("client.py"))
            time.sleep(1)
            P_LIST.append(get_subprocess('client.py', '--mode send'))
            time.sleep(1)

        print(f'Число запущенных пар клиентских скриптов: {CLIENTS_COUNT}')

    elif USER == "x":
        while P_LIST:
            victim = P_LIST.pop()
            os.killpg(victim.pid, signal.SIGINT)
