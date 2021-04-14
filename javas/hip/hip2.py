file = './HIP1000.txt'

with open(file) as f:
    lines = f.readlines()
    for line in lines:
        items = line.split(' ')
        print(items)
