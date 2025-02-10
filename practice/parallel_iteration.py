a = ["one", "two", "three", 'four']
b = [30, 20, 15, 75]
c = [5.2, 7.4, 3.6, 4.2]

# 예제 1
def create_dict1() -> dict:
    dictionary = {}
    for x, y ,z in zip(a, b, c):
        dictionary[x] = y * z
    return dictionary

print(create_dict1())

# 예제 2
def create_dict2() -> dict:
    return {x: y * z for x, y, z in zip(a, b, c)}

print(create_dict2())

