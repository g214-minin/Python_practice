import random

'''

Ключ генерируется по основной
плоскости Unicode:
Основная латиница: (33, 126)

'''


def encrypt(text, log=None):
    bintext = []
    binkey = []
    result = []
    for i in text:
        bintext.append(bin(ord(i)))  # ['0b1000001', '0b1010000'...APPLE
        binkey.append(bin(random.randint(33, 126)))  # ['0bxxxxxxx'...N
    for i, j in zip(bintext, binkey):
        result.append(chr(int(i, 2) ^ int(j, 2)))  # ['r', '\x11', 'm'...
        binkey.append(chr(int(j, 2)))  # ['0b110011', 'A'...
    del binkey[:-len(text)]
    s = ''.join(binkey)
    s1 = ''.join(result)
    print(f"Зашифрованное сообщения: {s1}\nКлюч: {s}")

    def record():
        with open("log.txt", "a") as file:
            file.write(f"\n------\n"
                       f"Зашифрованное сообщения: {s1}"
                       f"\nКлюч: {s}"
                       f"\n------")
        print("Лог файл успешно создан")
    if log == "l":
        record()


def decipher(text, key):
    result = []
    for i, j in zip(text, key):
        result.append(chr(int(bin(ord(i)), 2) ^ int(bin(ord(j)), 2)))
    s0 = ''.join(result)
    print(s0)
