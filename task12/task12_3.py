from tabulate import tabulate

from task12_1 import ping_ip_addresses
from task12_2 import convert_ranges_to_ip_list

ip_addresses = ['10.10.0.135', '8.8.8.8', '10.1.14.5-7', '8.8.8.8', '8.8.8.8', '8.8.8.8', '10.1.14.5', '10.1.14.5']
reachable, unreachable = ping_ip_addresses(convert_ranges_to_ip_list(ip_addresses))
colums = ['Reachable', 'Unreachable']

result = {}


def print_ip_table(reachable, unreachable):
    result['Reachable'] = reachable
    result['Unreachable'] = unreachable
    print(tabulate(result, headers=colums))


print_ip_table(reachable, unreachable)
