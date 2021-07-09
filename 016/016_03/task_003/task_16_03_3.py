packet = int(input('Кол-во пакетов: '))

packet_list = []
bad_packet = 0
decode_packet = []

for i_packet in range(packet):
    print("Пакет номер ", i_packet + 1)
    for i in range(4):
        print(i + 1, 'Бит: ', end='')
        bit = int(input())
        packet_list.append(bit)

    if packet_list.count(-1) > 1:
        print('Много ошибок в пакете.')
        bad_packet += 1
    else:
        decode_packet.extend(packet_list)
    packet_list = []
    print()



print('Полученное сообщение: ', decode_packet)
print("Кол-во ошибок в сообщении: ", decode_packet.count(-1))
print('Кол-во потерянных пакетов: ', bad_packet)
