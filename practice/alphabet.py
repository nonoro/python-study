# 예제 1
def write_file1(filepath: str):
    with open(filepath, "w") as file:
        for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            file.write(letter + " ")

def read_file(filepath: str):
    with open(filepath, "r") as file:
        print(file.read())

write_file1('../source/23-1.txt')
read_file('../source/23-1.txt')

#예제 2
import string

def write_file2(filepath: str):
    with open(filepath, "w") as file:
        for letter in string.ascii_uppercase:
            file.write(letter + '\n')

write_file2('../source/23-2.txt')
read_file(filepath='../source/23-2.txt')