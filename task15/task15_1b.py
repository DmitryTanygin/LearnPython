import re


def get_ip_from_cfg(filename):
    result = {}
    with open(filename) as f:
        for line in f:
            if line.startswith('interface'):
                interface = re.search(r'interface (\S+)', line).group(1)
                ip_result = []
            elif line.startswith(' ip address'):
                ip = re.search(r'ip address (\S+\s+\S+)', line).group(1)
                ip_result.append(tuple(ip.split(' ')))
                result[interface] = ip_result
    return result


if __name__ == "__main__":
    print(get_ip_from_cfg('config_r2.txt'))
