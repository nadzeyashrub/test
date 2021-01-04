start = int(input())
end = int(input())
i = 0
while start >= end:
    start /= 2
    i += 1
print(i * 12)
