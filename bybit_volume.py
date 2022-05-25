from pybit import HTTP
import pandas as pd
import time
from datetime import datetime
import calendar

session = HTTP(
    endpoint='https://api.bybit.com', 
)

a=0
volume_24h=0
volume_24h_2=0

volume_24h=session.latest_information_for_symbol(symbol='ZILUSDT')['result'][0]['volume_24h']
a=volume_24h
time.sleep(60)
print("-----------")

while True:
    # volume_1m=volume_24h/1440
    volume_24h_2=session.latest_information_for_symbol(symbol='ZILUSDT')['result'][0]['volume_24h']
    b=volume_24h_2
    # 직전 1분 거래량
    volume_1m = (volume_24h_2)-(volume_24h)
    # 변화율
    change_1m=(volume_24h-volume_24h_2)/volume_24h_2*100
    print("1분 거래량 변화 >  ",change_1m)
    if (change_1m >10 ):
        print("거래량 급등 알림!!!",change_1m)
        


    volume_24h=volume_24h_2
    
    time.sleep(60)
    
    
# print(price)
# 예) 3,000이 7,000으로 변하면?  133.3333333 %
#           계산식 : (7,000-3,000)/3,000*100 = 133.3333333 %














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
