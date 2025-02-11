import os

# 예제 1
def read_text_file1(filepath):
    output = []

    for file in os.listdir(filepath):
        # print(file)
        if file.endswith(".txt"):
            target_path = f"{filepath}/{file}"
            print(target_path)
            with open(target_path, "r") as f:
                output.append(f.read().strip('\n'))
    return output

# print(read_text_file1('../source/27-1'))

# 예제 2
import glob

def read_text_file2(filepath):
    output = []

    for file in glob.glob(filepath + "/*.txt"):
        with open(file, "r") as f:
            output.append(f.read().strip('\n'))
    return output

print(read_text_file2('../source/27-1'))