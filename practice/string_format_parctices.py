

x = 10
y = 20
serialno = 308276567
n = 'Kim'

# 출력 1
ex1 = 'n = %s, s = %d, sum = %d' % (n, serialno, (x + y))
print(ex1)

# 출력 2
ex2 = 'n = {n}, s = {serialno}, sum = {sum}'.format(n=n, serialno=serialno, sum=x + y)
print(ex2)

# 출력 3
ex3 = f'n = {n}, s = {serialno}, sum = {x + y}'
print(ex3)

# 출력 4
from string import Template
ex4 = 'n = $n, s = %serialno, sum = $sum'

t = Template(ex4)
print (t.substitute(n=n, serialno=serialno, sum=x + y))

# 출력 5(다양한 f-string 연습)

# (2진수: b, 8진수: o, 16진수: x|X)

k = 77

print(f"k 2: {k:b}, k 8: {k:o}, k 16: {k:x}")