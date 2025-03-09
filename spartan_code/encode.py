message = 'ПЕРЕСТАНОВКАСКЛЮЧЕВЫМСЛОВОМ'
SHIFT = 6 + 1
y = SHIFT
x = len(message)//y + 1
if __name__ == '__main__':
    encoded = ''
    message += (x*y-len(message))*' '
    matrix = {}
    cursor = 0
    for j in range(y):
        for i in range(x):
            matrix[i, j] = message[cursor]
            cursor += 1
    for i in range(x):
        for j in range(y):
            if matrix[i, j] != ' ': encoded += matrix[i, j]
    print(encoded)
