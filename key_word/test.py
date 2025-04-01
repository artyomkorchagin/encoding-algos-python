J = input()
S = input()

jewel_set = set(J)

count = sum(1 for char in S if char in jewel_set)

print(count)