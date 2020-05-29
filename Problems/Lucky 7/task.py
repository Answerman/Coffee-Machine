iterations = int(input())
in_number = []
for i in range(0, iterations):
    in_number.append(int(input()))

for i in range(0, iterations):
    if in_number[i] % 7 == 0:
        print(in_number[i]*in_number[i])
