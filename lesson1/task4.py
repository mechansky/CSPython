"""4. Преобразовать слова «разработка», «администрирование»,
«protocol», «standard» из строкового представления
в байтовое и выполнить обратное преобразование (используя методы encode и decode)."""

l1 = ["разработка", "администрирование", "protocol", "standard"]

def func(arg):
    encoding_list = []
    decoding_list = []
    for i in arg:
        encoding_list.append(i.encode('utf-8'))
    for i in encoding_list:
        decoding_list.append(i.decode('utf-8'))
    print(f'encoding list:\n{encoding_list}')
    print(f'decoding_list:\n{decoding_list}')


func(l1)
