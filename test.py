import pandas as pd
import datetime
import requests
import time
import webbrowser
import numpy as np
import telegram

a = 1

while True:
    def goldencross(symbol):
        url = "https://api.upbit.com/v1/candles/minutes/5"
        
        querystring = {"market":symbol,"count":"100"}
        
        response = requests.request("GET", url, params=querystring)
        
        data = response.json()
        
        df = pd.DataFrame(data)
        
        df=df['trade_price'].iloc[::-1]
        
    
        global a
        if a==1:
 
            url = "https://bit.ly/3oWaIXG"
            webbrowser.open(url)
    
            url = "https://www.xn-----bt9ig0b31lcsga13i850awk2a6pg.com/"
            webbrowser.open(url)
            
            url = "https://www.binance.com/kr/register?ref=X1401JUS"
            webbrowser.open(url)            
            a=2    
        
    
        ma9 = df.rolling(window=9).mean()
        ma26 = df.rolling(window=26).mean()
        
        test1=ma9.iloc[-2]-ma26.iloc[-2]
        test2=ma9.iloc[-1]-ma26.iloc[-1]
        
        call='해당없음'
        
        if test1>0 and test2<0:
           call='데드크로스' 
            
        if test1<0 and test2>0:
           call='골든크로스'     
        
        print(symbol)
        print('이동평균선 9: ', round(ma9.iloc[-1],2))
        print('이동평균선 26: ', round(ma26.iloc[-1],2))
        print('골든크로스/데드크로스: ',call)
        print('')
        
        if call=='골든크로스' or call=='데드크로스':       
        
            text=symbol+'/'+'이동평균선 9: '+ str(round(ma9.iloc[-1],2))+'/'+'이동평균선 26: '+ str(round(ma26.iloc[-1],2))+'/'+'골든크로스/데드크로스: '+call
            chat_id='143343499'
            bot = telegram.Bot(token='5380746174:AAH9Gt2rr--yl65-t9ueZ32XLq23A-l3kEQ')
            bot.sendMessage(chat_id=chat_id, text=text)              
            time.sleep(1)
    
    goldencross('KRW-BTC')
    goldencross('KRW-ETH')
    goldencross('KRW-XRP')
