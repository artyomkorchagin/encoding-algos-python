# This one doesn't work if characters in KEYWORD are not unique
MESSAGE = 'ЧЕЗВ-ЛПА-ЫСПЬА-ЖВТА-РВЕ-РРОК- -ТЕОТ'
KEYWORDS = ['ПОВОРОТ', 'КАТОРГА', 'ПИЛОТ']
Y = 5
if __name__ == '__main__':
    for keyword in KEYWORDS:
        matrix = {char: [] for char in sorted(keyword)}
        decoded = ''
        cursor = 0
        x = len(keyword)
        message = MESSAGE + (x * Y - len(MESSAGE)) * ' '

        for i in range(x):
            for J in range(Y):
                matrix[sorted(keyword)[i]].append(message[cursor])
                cursor += 1

        for i in range(Y):
            for j in range(x):
                decoded += matrix[keyword[j]][i]

        print(decoded)