# This one doesn't work if characters in KEYWORD are not unique
MESSAGE = 'ПЕРЕСТАНОВКА С КЛЮЧЕВЫМ СЛОВОМ'
KEYWORD = 'СИНДРОМ'
X = len(KEYWORD)
Y = 5
if __name__ == '__main__':
    matrix = {char: [] for char in KEYWORD}
    encoded = ''
    cursor = 0

    message = MESSAGE + (X * Y - len(MESSAGE)) * ' '

    for i in range(X):
        for J in range(Y):
            matrix[KEYWORD[i]].append(message[cursor])
            cursor += 1

    for i in range(Y):
        for j in range(X):
            encoded += matrix[sorted(KEYWORD)[j]][i]

    print(encoded)


