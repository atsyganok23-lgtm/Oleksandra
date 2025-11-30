class LimitQuery:
    def __init__(self, func):
        self.func = func
        self.count = 0
        self.limit = 5

    def __call__(self, *args, **kwargs):
        if self.count <= self.limit:
            self.count+=1
            return self.func(*args, **kwargs)
        else:
            print('Limit is reached')
            return None

def get_bitcoin_price():
    result=requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')

    print(result.status.code)

    if result.status.code == 200:
        data=result.json()
        return f'{float(data[price]):.2f}$'

print(get_bitcoin_price())