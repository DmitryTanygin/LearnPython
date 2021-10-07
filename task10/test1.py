from test import check_ip


def return_correct_ip(ip_addresses):
    return [ip for ip in ip_addresses if check_ip(ip)]


print('Проверка списка IP-адресов')
ip_list = ['10.1.1.1', '8.8.8.8', '2.2.2']
correct = return_correct_ip(ip_list)
print(correct)
