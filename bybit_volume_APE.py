from pybit import HTTP
import pandas as pd
import time
from datetime import datetime
import calendar
import datetime
import datetime as pydatetime
# ######################
import telegram
bot = telegram.Bot(token='5380746174:AAH9Gt2rr--yl65-t9ueZ32XLq23A-l3kEQ')
chat_id =5000365041 
# ######################
session = HTTP(
    endpoint='https://api.bybit.com', 
)
# ######################
symbol = "APEUSDT"
set_time=60
# ######################
def get_1_min_timestamp():
    time_1m = pydatetime.datetime.now()-datetime.timedelta(minutes=1)
    return round(time_1m.timestamp())
def get_2_min_timestamp():
    time_2m = pydatetime.datetime.now()-datetime.timedelta(minutes=2)
    return round(time_2m.timestamp())
    

while True:
    try:
        volume_1=session.query_kline( symbol=symbol, interval="1", from_time=get_1_min_timestamp())['result'][0]['volume']
        volume_2=session.query_kline( symbol=symbol, interval="1", from_time=get_2_min_timestamp())['result'][0]['volume']
        volume2_1=volume_2 - volume_1
        change_1m=(volume2_1/volume_1)*100
        # print("volume2_1",volume2_1)
        # print("1분 거래량 변화 >  ",change_1m,"%")
        # print("1분 거래량 변화 >  ",round(change_1m),"%")
        # print("volume_1=>",volume_1)
        # print("volume_2=>",volume_2)
        # msg = ""+symbol+"-"+str(set_time)+"s 동안 "+str(round(change_1m))+"% 변동"
        # bot.sendMessage(chat_id=chat_id, text=msg)
        if (change_1m >1000):
            print("거래량 급등 알림-",abs(change_1m))
            msg = ""+symbol+"-"+str(set_time)+"s 동안 "+str(round(change_1m))+"% 상승"
            bot.sendMessage(chat_id=chat_id, text=msg)
            
        time.sleep(set_time)
    except Exception as e :
        print("exception e=>",e)