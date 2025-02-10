import os

filenames = ["A", "B", "C", "D", "E", "F"]
contents1 = ['Python', 'Java', 'PHP', 'Javascript', 'Rust', 'Go']
contents2 = [['Python', 'Java', 'PHP', 'Javascript', 'Rust', 'Go'], ['Python', 'Java', 'PHP', 'Javascript', 'Rust', 'Go'], ['Python', 'Java', 'PHP', 'Javascript', 'Rust', 'Go'], ['Python', 'Java', 'PHP', 'Javascript', 'Rust', 'Go'], ['Python', 'Java', 'PHP', 'Javascript', 'Rust', 'Go'], ['Python', 'Java', 'PHP', 'Javascript', 'Rust', 'Go']]

def write_contents1(filepath):
    if not os.path.exists(filepath):
        os.makedirs(filepath)

    for filename, content in zip(filenames, contents1):
        with open(f"{filepath}/{filename}.txt", "w") as file:
            file.write(content)

write_contents1('../source/26-1')

def write_contents2(filepath):
    if not os.path.exists(filepath):
        os.makedirs(filepath)

    for filename, content in zip(filenames, contents2):
        with open(f"{filepath}/{filename}.txt", "w") as file:
            file.writelines(content + "\n" for content in content)

write_contents2('../source/26-2')
