ALPHABET = 'АБВГДЕЖЗИКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯАБВГДЕЖЗИКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯ'
MESSAGE = 'ШИФР ОБРАТИМОЕ ПРЕОБРАЗОВАНИЕ ОТКРЫТОГО ТЕКСТА'
SHIFT = 6

if __name__ == '__main__':
    encoded = ''
    shifted_alphabet = ALPHABET[slice(SHIFT, 31+SHIFT)]
    for letter in MESSAGE:
        if letter == ' ':
            encoded += ' '
            continue
        encoded += shifted_alphabet[ALPHABET.index(letter)]
    print(encoded)


