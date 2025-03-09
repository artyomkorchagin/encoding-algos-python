message = 'НОР_ГСА_АПОЕЧОЦЯ_МАПИТВЬЛЕИО_'
SHIFTS =  [2,7]


if __name__ == '__main__':
    for shift in range(SHIFTS[0],SHIFTS[1]+1):
        y = shift+1
        x = len(message) // y + 1
        message += (x * y - len(message)) * ' '
        decoded = ''
        matrix = {}
        cursor = 0
        for j in range(y):
            for i in range(x):
                matrix[i, j] = message[cursor]
                cursor += 1
        for i in range(x):
            for j in range(y):
                if matrix[i, j] != ' ': decoded += matrix[i, j]
        print(decoded)
