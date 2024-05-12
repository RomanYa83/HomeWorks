file = open('Byron.txt', 'r')
b = file.read()
with open('Byron.txt', mode='r') as file:
    for line in file:
        print(line, end='')