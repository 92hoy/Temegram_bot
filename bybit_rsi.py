
from pybit import HTTP
import webbrowser
import time
import pandas as pd
from pybit import HTTP
import requests
from datetime import datetime
import calendar

with open('apikey_url_bybit.txt', encoding='utf8') as f:
    count_line=0
    for line in f:
        count_line+=1
        if count_line == 1: # bybit API key 
            api_key = line.rstrip('\n')        
        elif count_line == 2: # bybit secret key 
            api_secret = line.rstrip('\n')
        elif count_line == 3: # bybit REST url for both Inverse Perpetual and USDT Perpetual,
            url_rest_bybit = line.rstrip('\n') # not used in this python code. 
        elif count_line == 4: # bybit websocket url for Inverse Perpetual,  BTCUSD , etc
            url_ws_inverse_bybit = line.rstrip('\n')
        elif count_line == 5: # bybit websocket public url for USDT Perpetual,  BTCUSDT, etc 
            url_ws_usdt_public_bybit = line.rstrip('\n')
        elif count_line == 6: # bybit websocket private url for USDT Perpetual,  BTCUSDT, etc 
            url_ws_usdt_private_bybit = line.rstrip('\n')
            break; 
    print('OK : read file apikey_url_bybit.txt')

from pybit import HTTP
import pandas as pd
import time
from datetime import datetime
import calendar

session = HTTP(
    endpoint='https://api.bybit.com', 
)

#rsi_bybit(분)
#15m,60m,240m-분봉기준 rsi 출력
def rsi_bybit(itv, symbol='BTCUSD'):
    now = datetime.utcnow()
    unixtime = calendar.timegm(now.utctimetuple())
    since = unixtime-itv*60*200;
    response=session.query_kline(symbol='BTCUSD',interval=str(itv),**{'from':since})['result']
    df = pd.DataFrame(response)
    rsi=rsi_calc(df,14).iloc[-1]
    print(rsi)

def rsi_calc(ohlc: pd.DataFrame, period: int = 14):
    ohlc = ohlc['close'].astype(float)
    delta = ohlc.diff()
    gains, declines = delta.copy(), delta.copy()
    gains[gains < 0] = 0
    declines[declines > 0] = 0

    _gain = gains.ewm(com=(period-1), min_periods=period).mean()
    _loss = declines.abs().ewm(com=(period-1), min_periods=period).mean()

    RS = _gain / _loss
    return pd.Series(100-(100/(1+RS)), name="RSI")

# test
while True:
    rsi_bybit(15)
    rsi_bybit(60)    
    rsi_bybit(240)

    time.sleep(1)
