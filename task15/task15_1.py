import re


def get_ip_from_cfg(filename):
    regex = r'(\d+\.\d+\.\d+\.\d+ \d+\.\d+\.\d+\.\d+)'
    result = []
    with open(filename) as f:
        for line in f:
            match = re.search(regex, line)
            if match:
                match = tuple((match.group()).split(' '))
                result.append(match)
    return result
print(get_ip_from_cfg('config_r1.txt'))