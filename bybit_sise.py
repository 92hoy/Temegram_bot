from pybit import HTTP
import webbrowser
import time

api_key=''
api_secret=''
import datetime
import datetime as pydatetime

def get_now():
    """
        현재 시스템 시간을 datetime형으로 반환
    """
    return pydatetime.datetime.now()-datetime.timedelta(minutes=1)

def get_now_timestamp():
    """
        현재 시스템 시간을 POSIX timestamp float형으로 반환
    """
    return get_now().timestamp()

# -------------key값 정리
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


session = HTTP(
endpoint=url_rest_bybit,
api_key=api_key,
api_secret=api_secret)

while True:
    # price=session.latest_information_for_symbol(symbol='APEUSDT')['result'][0]['last_price']
    price=session.query_kline( symbol="BTCUSD",
    interval="1",
    from_time=round(get_now_timestamp()))['result'][0]['volume']

    print("Bybit Bitcoin BTCUSD Price: ",price)

    time.sleep(60)

