import asyncio 
import websockets
import json

import time
import hmac
import ssl

def get_args_secret(_api_key, _api_secrete):
        expires = str(int(round(time.time())+5000))+"000"
        _val = 'GET/realtime' + expires
        signature = str(hmac.new(bytes(_api_secrete, "utf-8"), bytes(_val, "utf-8"), digestmod="sha256").hexdigest())
        auth = {}
        auth["op"] = "auth"
        auth["args"] = [_api_key, expires, signature]
        args_secret = json.dumps(auth)

        return  args_secret

####################### for bybit Inverse .  BTCUSD, ETHUSD, EOSUSD, XRPUSD

async def my_loop_WebSocket_bybit():

    async with websockets.connect(url_ws_inverse_bybit,ssl=ssl_context) as websocket:
        if secure:
            ssl_context = ssl._create_unverified_context()
        await websocket.send(get_args_secret(api_key, api_secret)); # secret 
        print("Connected to bybit WebSocket with secret key");

        await websocket.send('{"op":"subscribe","args":["trade.BTCUSD"]}');
        await websocket.send('{"op":"subscribe","args":["trade.ETHUSD"]}');
        await websocket.send('{"op":"subscribe","args":["trade.EOSUSD"]}');
        await websocket.send('{"op":"subscribe","args":["trade.XRPUSD"]}');
        
        while True:
            data_rcv_strjson = await websocket.recv(); 
            print(data_rcv_strjson)
            



######################## for bybit USDT : BTCUSDT, ETHUSDT, LTCUSDT, LINKUSDT, XTZUSDT

async def my_loop_WebSocket_usdt_public_bybit():
    async with websockets.connect( url_ws_usdt_public_bybit ) as ws_usdt_public:
        
        print("Connected to bybit USDT WebSocket Public");

        await ws_usdt_public.send('{"op": "subscribe", "args": ["trade.BTCUSDT"]}');
        await ws_usdt_public.send('{"op": "subscribe", "args": ["trade.ETHUSDT"]}');
        await ws_usdt_public.send('{"op": "subscribe", "args": ["trade.LTCUSDT"]}');
        await ws_usdt_public.send('{"op": "subscribe", "args": ["trade.LINKUSDT"]}');
        await ws_usdt_public.send('{"op": "subscribe", "args": ["trade.XTZUSDT"]}');

        while True:
            data_rcv_strjson = await ws_usdt_public.recv(); 
            print('USDT from bybit public: ' + data_rcv_strjson)


async def my_loop_WebSocket_usdt_private_bybit():
    async with websockets.connect(url_ws_usdt_private_bybit) as ws_usdt_private:
        await ws_usdt_private.send(get_args_secret(api_key, api_secret)); # secret 
        print("Connected to bybit USDT WebSocket Private with secret key");

        while True:
            data_rcv_strjson = await ws_usdt_private.recv(); 
            print('USDT from bybit private: ' + data_rcv_strjson)
           

##### main exec 
#### 파일 apikey_url.txt 읽어서 api key 와 url 정보 변수에 받아두기. 
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


my_loop = asyncio.get_event_loop();  
my_loop.run_until_complete(asyncio.gather(*[my_loop_WebSocket_bybit(),my_loop_WebSocket_usdt_private_bybit(),my_loop_WebSocket_usdt_public_bybit()]));
my_loop.close(); 

