from upbitpy import Upbitpy

upbit = Upbitpy()
tickers = upbit.get_ticker(['KRW-BTC', 'KRW-EOS'])
for ticker in tickers:
    print('%s trade price : %d' % (ticker['market'], ticker['trade_price']))
