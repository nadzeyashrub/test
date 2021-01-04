deposit = int(input())
i = 0

while deposit <= 700000:
    deposit *= 1.071
    i += 1
print(i)
