from lolzapi import LolzteamApi
import time

api = LolzteamApi('TOKEN', 11111)
comment = int(time.time())
amount = 100

print('Send money to https://zelenka.guru/alegor')
print('- Amount:', amount)
print('- Comment:', comment)

while True:
    input('I paid, check payment...')
    if api.market_payments(type_='income', pmin=amount, pmax=amount, comment=comment)['payments']:
        print('Payment was found!')
        break
    else:
        print('Payment not found!')
