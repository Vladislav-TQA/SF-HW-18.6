import requests
import json
from config import keys


class APIException(Exception):
    pass


class CryptoConverter:
    @staticmethod
    def get_price(base: str, quote: str, amount: str):

        try:
            base_ticker = keys[base]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {base}')
        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {quote}')
        if quote == base:
            raise APIException(f'Введены одинаковые валюты: {base}.')

        try:
            amount = float(amount)


        except ValueError:
            raise APIException(f'Не удалось обработать количество {amount}')
        if amount < 0:
            raise APIException(f'Введено отрицательное количество валюты')
        if amount == float('inf'):
            raise APIException(f'Введено недопустимо значение')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={base_ticker}&tsyms={quote_ticker}')
        total_base = json.loads(r.content)[keys[quote]]
        total_base = total_base * amount

        return total_base
