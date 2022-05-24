from upbitpy import Upbitpy

upbit = Upbitpy()

markets = upbit.get_market_all()
for market in markets:
    print(market)
