import re


def generate_description_from_cdp(filename):
    result = {}
    with open(filename) as f:
        for line in f:
            match = re.search(r'(\S+) +'
                              r'(\S+\s+\S+) +'
                              r'(\d+) +'
                              r'(\S+\s+\S+\s+\S+) +'
                              r'(\d+) +'
                              r'(\S+\s+\S+)', line)
            if match:
                interface = match.group(2)
                result[interface] = f'description Connected to {match.group(1)} port {match.group(6)}'
        return result


if __name__ == "__main__":
    print(generate_description_from_cdp('sh_cdp_n_sw1.txt'))
