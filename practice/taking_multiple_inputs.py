# 방법 1
x = int(input('숫자를 입력하시오: '))
y = int(input('숫자를 입력하시오: '))
z = int(input('숫자를 입력하시오: '))

print((x + y + z) / 3)

# 방법 2
x, y, z = input("숫자를 입력하세요: ").split(",")

print((int(x) + int(y) + int(z)) / 3)

# 방법 3
l = list(map(int, input('숫자를 입력하세요: ').split()))
print(round(sum(l) / len(l), 2))