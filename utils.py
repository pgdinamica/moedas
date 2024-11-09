import requests

CURRENCY_NAMES = {
    "USD": "Dólares dos Estados Unidos da América",
    "BRL": "Real"
}

EXCHANGE_RATES = {
    "USD": {
        "BRL": 5.80,
        "EUR": 0.85,
    },
    "BRL" : {
        "USD": 1 / 5.8,
        "EUR": 1 / 6.15
    }
}

def get_exchange_rate(from_code, to_code, kind='ask'):
    url = 'https://economia.awesomeapi.com.br/last/{}-{}'
    r = requests.get(url.format(from_code, to_code))
    # assumir cuidadosamente (kkk) que sempre da certo
    rate = r.json()[f'{from_code}{to_code}'][kind]
    return float(rate)
