str = input('Введите IP адрес в формате 10.0.1.1/24: ').split('/')
list_host_ip = str[0].split('.')
bin_ip_1 = format(int(list_host_ip[0]), '08b')
bin_ip_2 = format(int(list_host_ip[1]), '08b')
bin_ip_3 = format(int(list_host_ip[2]), '08b')
bin_ip_4 = format(int(list_host_ip[3]), '08b')
str_bin_ip = bin_ip_1 + bin_ip_2 + bin_ip_3 + bin_ip_4
bin_mask = '1' * int(str[1]) + '0' * (32 - int(str[1]))
mask = 32 - int(str[1])
bin_ip_network = str_bin_ip[0:int(str[1])] + '0' * mask
bin_ip_network = bin_ip_network[0:8] + ' ' + bin_ip_network[8:16] + ' ' \
                   + bin_ip_network[16:24] + ' ' + bin_ip_network[24:32]
list_bin_mask = bin_ip_network.split(' ')

oct1 = bin_mask[0:8]
oct2 = bin_mask[8:16]
oct3 = bin_mask[16:24]
oct4 = bin_mask[24:32]

print(f'''
Network:
{int(list_bin_mask[0], 2):<8} {int(list_bin_mask[1], 2):<8} {int(list_bin_mask[2], 2):<8} {int(list_bin_mask[3], 2):<8}
{list_bin_mask[0]:<8} {list_bin_mask[1]:<8} {list_bin_mask[2]:<8} {list_bin_mask[3]:<8}

Mask:
/{str[1]}
{int(oct1, 2):<8} {int(oct2, 2):<8} {int(oct3, 2):<8} {int(oct4, 2):<8}
{oct1:<8} {oct2:<8} {oct3:<8} {oct4:<8}
''')