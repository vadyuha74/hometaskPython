# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

def rle_encode(data):
    encoding = ''
    prev_char = ''
    count = 1
    if not data: return ''
    for char in data:
        if char != prev_char:
            if prev_char:
                encoding += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        encoding += str(count) + prev_char
        return encoding

def rle_decode(data):
    decode = ''
    count = ''
    for char in data:
        if char.isdigit():
            count += char
        else:
            decode += char * int(count)
            count = ''
    return decode

path = 'tasks_lesson_5/fail4.txt'
with open(path, 'r') as d:
    data = d.read()
print(f'дана строка {data}')
print(f'полученая строка {rle_encode(data)}\nбудет сохранена в файл "Encodefail"')
path = 'tasks_lesson_5/Encodfail.txt'
with open(path, 'w') as d:
    d.write(rle_encode(data))