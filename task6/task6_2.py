ip = input('Введите IP-адреса в формате 10.0.1.1: ')
if 1 <= int(ip.split('.')[0]) <= 223:
    print('unicast')
elif 224 <= int(ip.split('.')[0]) <= 239:
    print('multicast')
elif ip == '255.255.255.255':
    print('local broadcast')
elif ip == '0.0.0.0':
    print('unassigned')
else:
    print('unused')
