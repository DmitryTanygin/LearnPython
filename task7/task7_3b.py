line_list = []
vlan = input('Введите номер vlan: ')
with open('CAM_table.txt') as f:
    for line in f:
        if line == '\n':
            continue
        line = line.split()
        if line[0].isdigit():
            line[0] = int(line[0])
            line_list.append(line)
for l in sorted(line_list):
    if int(vlan) == l[0]:
        print(f'{l[0]:<10} {l[1]} {l[3]}')
