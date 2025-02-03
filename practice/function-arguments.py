# 함수의 인자값에 인한 에러발생을 막는 법

"""
 1. 모든 인자가 디폴트 값이 존재하는 경우
 2. 모든 인자가 디폴트 값이 존재하지 않는 경우
 3. 디폴트 값이 존재하는 인자들이 뒤쪽에 있는 경우

문제: 에러가 발생하는 함수가 주어졌을때 에러를 없애보기
def greet(msg = "Good morning!", name):
    return "Hi! " + name + ', ' + msg

print(greet("Kim"))
print(greet("Park", "How do you do?"))
"""

# 예제 1
def greet1(name, msg = "Good morning!", *b):
    return f"Hi! {name}, {msg} and {b}"

def greet2(msg = "Good morning!", name = "Roh"):
    return f"Hi! {name}, {msg}"

def greet3(msg = "Good morning!", name = "Roh"):
    return f"Hi! {name}, {msg}"

print("예제 1")
print(greet1("Kim", 'sorry', 'i', 'like', 'you'))
print(greet2("Kim"))
print(greet3("Kim"))
print(greet2(name = "Kim"))
print(greet2(msg = "Nice to meet you!"))

# 예제 2
def add(*d):
    return sum(d)

print("\n예제 2")
print(add(*(i for i in range(1, 11))))
print(*(i for i in range(1, 11)))

# 예제 3
def func(a, b="Hello", *args, c, **kwargs):
    print("\n예제 3")
    print(f"a: {a}")
    print(f"b: {b}")
    print(f"args: {args}")
    print(f"c: {c}")
    print(f"kwargs: {kwargs}")

params = {"d": 100, "e": 200}

func(1, "bye", 1, 2, 3, 4, c = 50, **params)
func(1, "bye", 1, 2, 3, 4, c = 50, d = 100, e = 200)

