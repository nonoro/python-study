# 예제 1
a = 20

def local_variable1():
    a = 35
    return a

print('step1: ', a)

a = 100

print('step2: ', a)
print('step3: ', local_variable1())

# 예제 2
a = 20

def local_variable_test2():
    global a
    print(f"ex3 결과: {a}")

    a = 35

    return a

print(f"ex1 결과: {a}")

a = 100

print(f"ex2 결과: {a}")
print(f"ex4 결과: {local_variable_test2()}")
print(f"ex5 결과: {a}")
