numbers = [1, 28, 4, 7, 9, 11, 12, 18, 19, 21, 23]
count = 0


for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        count += 1

print(count)