ALPHABET = 'АБВГДЕЖЗИКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯАБВГДЕЖЗИКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯ'
MESSAGE = 'МФРТВП  РДУФВЗ  ФФРОХГ  РЕЖВЗФ'
SHIFTS = [2, 6]

if __name__ == '__main__':
    for shift in range(SHIFTS[0],SHIFTS[1]+1):
        decoded = ''
        shifted_alphabet = ALPHABET[slice(31-shift, len(ALPHABET)-shift)]
        for letter in MESSAGE:
            if letter == ' ':
                decoded += ' '
                continue
            decoded += shifted_alphabet[ALPHABET.index(letter)]
        print(decoded)