data = {
    "address": "0x544444444444",
    "count_txs": 2,
    "ETH": {
        "balance": 444,
        "totalIn": 444,
        "totalOut": 4
    },
    "tokens": [
        {
            "fst_token_info": {
                "address": "0x44444",
                "name": "fdf",
                "decimals": 0,
                "symbol": "dsfdsf",
                "total_supply": "3228562189",
                "owner": "0x44444",
                "last_updated": 1519022607901,
                "issuances_count": 0,
                "holders_count": 137528,
                "price": False
            },
            "balance": 5000,
            "totalIn": 0,
            "total_out": 0
        },
        {
            "sec_token_info": {
                "address": "0x44444",
                "name": "ggg",
                "decimals": "2",
                "symbol": "fff",
                "total_supply": "250000000000",
                "owner": "0x44444",
                "last_updated": 1520452201,
                "issuances_count": 0,
                "holders_count": 20707,
                "price": False
            },
            "balance": 500,
            "totalIn": 0,
            "total_out": 0
        }
    ]
}

# print(data)
for i in data:
    # print('{0} {1}'.format(i, data.get(i)))
    # print('-----------------------------------------')
    if type(data[i]) != dict and type(data[i]) != list:
        print('{0} = {1}'.format(i, data.get(i)))
    elif type(data[i]) == dict:
        print('\033[31m#{0}: \033[0m'.format(i))
        for j in data[i]:
            print('{0} = {1}'.format(j, data.get(i).get(j)))
    elif type(data[i]) == list:
        print('\033[31m#{0}: \033[0m'.format(i))
        for j in data[i]:
            # print('ALL ', j)
            for z in j:
                if type(j[z]) != dict:
                    print('!= dict {0} = {1}'.format(z, j[z]))
                elif type(j[z]) == dict:
                    print('\033[31m## {0}: \033[0m'.format(z))
                    for k in j[z]:
                        print('{0} = {1}'.format(k, j[z][k]))

data['ETH'].update({'total_diff': 100})
data['tokens'][0]['fst_token_info']['name'] = 'doge'
data['ETH']['total_out'] = data['tokens'][1].pop('total_out')
data['tokens'][1]['sec_token_info'].update({'total_price': data['tokens'][1]['sec_token_info'].pop('price')})

print('-----------------------------------------')
for i in data:
    print('{0} {1}'.format(i, data.get(i)))
