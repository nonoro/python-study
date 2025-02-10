our_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# 예제 1
def split_n_list(split_size: int) -> list:
    split_list = list()

    for i in range(0, len(our_list), split_size):
        split_list.append(our_list[i:i + split_size])
    return split_list

print(split_n_list(3))
print(split_n_list(5))
print(split_n_list(7))

# 예제 2
def split_n_list2(split_size: int) -> list:
    return [our_list[i:i + split_size] for i in range(0, len(our_list), split_size)]

print(split_n_list2(3))
print(split_n_list2(5))
print(split_n_list2(7))