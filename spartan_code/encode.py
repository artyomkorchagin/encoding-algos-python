message = 'ПЕРЕСТАНОВКАСКЛЮЧЕВЫМСЛОВОМ'
SHIFT = 6 + 1
x = SHIFT
if len(message) % x != 0: y = (len(message)//x + 1)
else: y = len(message)//x
if __name__ == '__main__':
    print(y,x)
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
