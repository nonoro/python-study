d = dict(one = list(range(1, 11)), two = list(range(11, 23)), three = list(range(23, 51)))

for x in d:
    print(f"key : '{x}' has values {d[x]} -> total : {len(d[x])}")