# 49, 7, 7, 23
# 49, 13, 33, 44

def local_global_variable_test(x, y):
    global a
    a = 49
    x, y = y, x
    b = 53
    b = 7
    c = 135

    print('Step: ', a, b, x, y)

a, b, x, y = 8, 13, 33, 44

local_global_variable_test(23, 7)

print('Step2: ', a, b, x, y)
