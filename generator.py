def all_variants(string):
    for i in range(len(string) + 1):
        for j in range(i):
            yield string[j:i]


av = all_variants('PythonGenerator')
for v in av:
    print(v)