from sys import argv

ignore = ["duplex", "alias", "configuration"]
with open(argv[1]) as f, open(argv[2], 'w') as r:
    for line in f:
        if not line.startswith('!'):
            if not ignore[0] in line.split(' ') and \
                    not ignore[1] in line.split(' ') and \
                    not ignore[2] in line.split(' '):
                r.write(line)
