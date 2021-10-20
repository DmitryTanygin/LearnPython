import csv
import re


def write_dhcp_snooping_to_csv(filenames, output):
    result = []
    headers = []
    for filename in filenames:
        switch = re.search(r'\S[^\_]+', filename).group()
        with open(filename) as f:
            regex = r'^\w+\:'
            for line in f:
                match = re.search(regex, line)
                line = line.split()
                if line[0] == 'MacAddress' and headers == []:
                    line[0] = 'switch'
                    headers = line
                elif match:
                    line[0] = switch
                    result.append(line)
    with open(output, 'w') as g:
        writer = csv.writer(g)
        writer.writerow(headers)
        writer.writerows(result)


if __name__ == '__main__':
    write_dhcp_snooping_to_csv(['sw1_dhcp_snooping.txt', 'sw2_dhcp_snooping.txt', 'sw3_dhcp_snooping.txt'],
                               'output.csv')
