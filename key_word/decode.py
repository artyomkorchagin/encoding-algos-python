# This one doesn't work if characters in KEYWORD are not unique
MESSAGE = 'ЧЕЗВ-ЛПА-ЫСПЬА-ЖВТА-РВЕ-РРОК--ТЕОТЕ'
KEYWORDS = ['ПОВОРОТ', 'КАТОРГБ', 'ПИЛОТ'] # CHANGED КАТОРГА TO КАТОРГБ TO PREVENT COLLISION
Y = 5
if __name__ == '__main__':
    for keyword in KEYWORDS:
        matrix = {char: [] for char in sorted(keyword)}
        decoded = ''
        cursor = 0
        x = len(keyword)
        message = MESSAGE + (x * Y - len(MESSAGE)) * ' '

        for j in range(Y):
            for i in range(x):
                matrix[sorted(keyword)[i]].append(message[cursor])
                cursor += 1

        for i in range(x):
            for j in range(Y):
                decoded += matrix[keyword[i]][j]

        print(decoded)