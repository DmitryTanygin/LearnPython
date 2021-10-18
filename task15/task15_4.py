import re


def get_ints_without_description(filename):
    result = []
    interface = ''
    with open(filename) as f:
        for line in f:
            if line.startswith('interface'):
                interface = re.search(r'interface (\S+)', line).group(1)
            elif line.startswith(' description'):
                interface = ''
            elif line.startswith('!') and interface != '':
                result.append(interface)
                interface = ''
        return result


if __name__ == "__main__":
    print(get_ints_without_description('config_r1.txt'))
