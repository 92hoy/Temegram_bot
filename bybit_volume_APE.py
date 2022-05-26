from pybit import HTTP
import pandas as pd
import time
from datetime import datetime
import calendar

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
# ######################
a=0
volume_24h=0
volume_24h_2=0

volume_24h=session.latest_information_for_symbol(symbol=symbol)['result'][0]['volume_24h']
a=volume_24h
time.sleep(10)
volume_1m_before=0
print("-----start------")

while True:
    try:
        volume_24h_2=session.latest_information_for_symbol(symbol=symbol)['result'][0]['volume_24h']

        # 직전 1분 거래량
        volume_1m= (volume_24h)-(volume_24h_2)
    
        # print("직전1분거래량",abs(volume_1m_before))
        # print("이후1분거래량",abs(volume_1m))
        if(volume_1m==0 or volume_1m_before==0):
            pass
        else:
            change_1m=(abs(volume_1m_before) - abs(volume_1m))/abs(volume_1m_before)*100
            # print("1분 거래량 변화 >  ",abs(change_1m),"%")
            if (change_1m >500):
                print("거래량 급등 알림!!!",abs(change_1m))
                # bot.sendMessage(chat_id=chat_id, text="보낼 메세지")
            
        volume_24h=volume_24h_2
        volume_1m_before = volume_1m
        
        time.sleep(10)
    except Exception as e :
        print("exception e=>",e)
    