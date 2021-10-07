from sys import argv
with open(argv[1]) as f:
    for line in f:
        if not line.startswith('!'):
            print(line.rstrip())