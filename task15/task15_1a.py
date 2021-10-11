import re


def get_ip_from_cfg(filename):
    regex = (r'interface (?P<interface>\S+)'
             r'|ip address (?P<ip>\S+)\s+(?P<mask>\S+)')
    result = {}
    with open(filename) as f:
        for line in f:
            if line.startswith('interface'):
                interface = re.search(r'interface (\S+)', line).group(1)
            elif line.startswith(' ip address'):
                ip = re.search(r'ip address (\S+\s+\S+)', line).group(1)
                result[interface] = tuple(ip.split(' '))
    return result


print(get_ip_from_cfg('config_r1.txt'))
