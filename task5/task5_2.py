str = input('')
str.split('/')
ip = str.split('/')[0].split('.')
mask_10 = str.split('/')[1]
mask_2 = '1' * int(mask_10) + '0' * (32 - int(mask_10))
oct1 = mask_2[0:8]
oct2 = mask_2[8:16]
oct3 = mask_2[16:24]
oct4 = mask_2[24:32]

print(f'''
Network:
{ip[0]:<8} {ip[1]:<8} {ip[2]:<8} {ip[3]:<8}
{int(ip[0]):08b} {int(ip[1]):08b} {int(ip[2]):08b} {int(ip[3]):08b}

Mask:
/{mask_10}
{int(oct1, 2):<8} {int(oct2, 2):<8} {int(oct3, 2):<8} {int(oct4, 2):<8}
{oct1:<8} {oct2:<8} {oct3:<8} {oct4:<8}
''')