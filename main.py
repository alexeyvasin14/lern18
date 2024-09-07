import random


def a():
    b = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    c = random.choice(b)
    return c


n = a()
print(n)
num1 = list(range(1, n + 1))
num2 = list(range(1, n + 1))
result = []
result2 = ''
for i in num1:
    for j in num2:

        if i >= j:
            continue
        else:
            kr = n % (i + j)
            if kr == 0:
                result.append([i, j])
                result2 = result2 + str(i) + str(j)

print(result)
print(result2)
