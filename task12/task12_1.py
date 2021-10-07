import subprocess
from tabulate import tabulate
from pprint import pprint


def ping_ip_addresses(ip_addresses):
    result_true = []
    result_false = []
    for ip_address in ip_addresses:
        reply = subprocess.run(['ping', '-c', '3', '-n', ip_address],
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE,
                               encoding='utf-8')
        if reply.returncode == 0:
            result_true.append(ip_address)
        else:
            result_false.append(ip_address)
    return result_true, result_false


if __name__ == '__main__':
    pprint(ping_ip_addresses('10.10.0.135', '8.8.8.8', '10.1.14.5'))
