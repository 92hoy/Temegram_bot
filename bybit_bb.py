from pybit import HTTP
import pandas as pd
import time
from datetime import datetime
import calendar

session = HTTP(
    endpoint='https://api.bybit.com', 
)

price=session.latest_information_for_symbol(symbol='ZILUSDT')['result'][0]
print(price)

# def rsi_bybit(itv, symbol='BTCUSD'):
#     now = datetime.utcnow()
#     unixtime = calendar.timegm(now.utctimetuple())
#     since = unixtime-itv*60*200;
#     response=session.query_kline(symbol='BTCUSD',interval=str(itv),**{'from':since})['result']
#     df = pd.DataFrame(response)
#     rsi=rsi_calc(df,14).iloc[-1]
#     print(rsi)

# def rsi_calc(ohlc: pd.DataFrame, period: int = 14):
#     ohlc = ohlc['close'].astype(float)
#     delta = ohlc.diff()
#     gains, declines = delta.copy(), delta.copy()
#     gains[gains < 0] = 0
#     declines[declines > 0] = 0

#     _gain = gains.ewm(com=(period-1), min_periods=period).mean()
#     _loss = declines.abs().ewm(com=(period-1), min_periods=period).mean()

#     RS = _gain / _loss
#     return pd.Series(100-(100/(1+RS)), name="RSI")

# # test
# while True:
#     rsi_bybit(15)
#     rsi_bybit(60)    
#     rsi_bybit(240)

#     time.sleep(1)
