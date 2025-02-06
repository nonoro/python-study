# 전역변수

# 예제 1
x = 100

def global_variable_test1():
    return x * 10

print(f"ex1: {global_variable_test1()}")

# 예제 2
y = 10

def global_variable_test2():
    global y
    y *= 10
    return y

print(f"ex2: {global_variable_test2()}")
print(f"y: {y}")


