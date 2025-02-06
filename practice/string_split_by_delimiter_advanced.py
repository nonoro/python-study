# 예제1
def cnt_word1(filepath) -> int:
    with open(filepath, "r") as file:
        txt = file.read()
        txt = txt.replace(",", " ")
        print(txt)

        txt_list = txt.split(" ")
        print(txt_list)
        return len(txt_list)

# print(cnt_word1("../source/22-1.txt"))

# 예제2
import re

def cnt_word2(filepath) -> int:
    with open(filepath, "r") as file:
        txt = file.read()

        txt_list = re.split("[ ,]", txt)
        print(txt_list)
        return len(txt_list)

print(cnt_word2("../source/22-1.txt"))