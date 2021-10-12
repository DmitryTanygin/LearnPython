import re


def convert_ios_nat_to_asa(file_nat, file_asa):
    regex = r'[\S +]+ (?P<intf>inside|outside) \S+ \S+ \S+ (?P<ip>[\d.]+) (?P<port1>\d+) \S+ \S+ (?P<port2>\d+)'
    with open(file_nat) as f, open(file_asa, 'w') as r:
        for line in f:
            match = re.search(regex, line)
            r.write(f"object network LOCAL_{match.group('ip')}\n"
                    f" host {match.group('ip')}\n"
                    f" nat {match.group('intf')} static interface service tcp {match.group('port1')} {match.group('port2')}\n")


convert_ios_nat_to_asa('cisco_nat_config.txt', 'asa_config.txt')
