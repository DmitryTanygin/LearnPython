import re


def parse_sh_ip_int_br(filename):
    result = []
    regex = r'(\S+) +([\d.]+|unassigned+) +\w+ +\w+ +(up|down|administratively down) +(up|down)'
    with open(filename) as f:
        for line in f:
            for match in re.finditer(regex, line):
                result.append(match.groups())
            # [result.append(match.groups()) for match in re.finditer(regex, line)]
        return result


print(parse_sh_ip_int_br('sh_ip_int_br.txt'))
