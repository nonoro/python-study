number = int(input("숫자를 입력하세요: "))

def segma_1(n):
    result1 = 0
    for x in range(1, int(n) + 1):
        result1 += x
    return result1

def segma_2(n):
    return sum(range(1, int(n) + 1))

def segma_3(n):
    return n * (n + 1) // 2

print(segma_1(number))
print(segma_2(number))
print(segma_3(number))


