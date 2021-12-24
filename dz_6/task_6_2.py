"""
*(вместо 1) Найти IP адрес спамера и количество отправленных им запросов по данным файла логов из предыдущего задания.
Примечание: спамер — это клиент, отправивший больше всех запросов; код должен работать даже с файлами, размер которых
превышает объем ОЗУ компьютера.
"""
ip_list = []
with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    for _ in f:
        ip = f.readline().split()[0]
        ip_list.append(ip)
uniq_ip = list(set(ip_list))
count_dict = {}
for i in range(len(uniq_ip)):
    count_el = ip_list.count(uniq_ip[i])
    count_dict.update({uniq_ip[i]: count_el})
spammer_count = sorted(count_dict.values(), reverse=True)[0]
for i, k in count_dict.items():
    if k == spammer_count:
        print(f'Spammer: {i}, number of requests: {k}')
        break;



