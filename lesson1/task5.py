"""Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать
результаты из байтовового в строковый (предварительно определив кодировку выводимых сообщений)."""

import chardet   # необходима предварительная инсталляция!
import subprocess
import platform
import locale


default_encoding = locale.getpreferredencoding()
print(f'default: {default_encoding}')

sites = ['yandex.ru', 'youtube.com']

def func(sites):
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    for site in sites:
        args = ['ping', param, '2', site]
        result = subprocess.Popen(args, stdout=subprocess.PIPE)
        for line in result.stdout:
            result = chardet.detect(line)
            line = line.decode(result['encoding']).encode('utf-8')
            print(line.decode('utf-8'))

func(sites)