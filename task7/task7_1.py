with open('ospf.txt') as f:
    for line in f:
        line = line.split()
        print('{:<20} {:<10}'.format('Prefix', line[0]))
        print('{:<20} {:<10}'.format('AD/Metric', line[1]))
        print('{:<20} {:<10}'.format('Next-Hop', line[3]))
        print('{:<20} {:<10}'.format('Last update', line[4]))
        print('{:<20} {:<10}'.format('Outbound Interface', line[5]))
        print('\n' + '-' * 30)
