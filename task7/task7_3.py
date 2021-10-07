result = {}
with open('CAM_table.txt') as f:
    for line in f:
        if line == '\n':
            continue
        line = line.split()
        if line[0].isdigit():
            print(f'{line[0]:>10} {line[1]} {line[3]}')
