import csv
import re


def write_dhcp_snooping_to_csv(filename, output):
    switch = re.search(r'\S[^\_]+', filename).group()
    with open(filename) as f, open(output, 'w') as g:
        writer = csv.writer(g)
        regex = r'^\w+\:'
        for line in f:
            match = re.search(regex, line)
            line = line.split()
            if line[0] == 'MacAddress':
                line[0] = 'switch'
                writer.writerow(line)
            elif match:
                line[0] = switch
                writer.writerow(line)


if __name__ == '__main__':
    write_dhcp_snooping_to_csv('sw1_dhcp_snooping.txt', 'output.csv')
