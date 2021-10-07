ip = input('Введите IP-адреса в формате 10.0.1.1: ')
while True:
    is_correct = True
    for ip_item in ip.split('.'):
        if 0 <= int(ip_item) <= 255:
            pass
        else:
            is_correct = False
            break
        break
    if len(ip.split('.')) != 4 or \
            not ''.join(ip.split('.')).isdigit():
        print('Ошибка формата')
    elif not is_correct:
        print('Ошибка формата')
    else:
        print("Введеный IP-адрес {}".format(ip))
        break
    ip = input('Введите IP-адреса еще раз в формате 10.0.1.1: ')

ip_list = ip.split('.')
if 1 <= int(ip_list[0]) <= 223:
    print('unicast')
elif 224 <= int(ip_list[0]) <= 239:
    print('multicast')
elif '.'.join(ip_list) == '255.255.255.255':
    print('local broadcast')
elif '.'.join(ip_list) == '0.0.0.0':
    print('unassigned')
else:
    print('unused')
