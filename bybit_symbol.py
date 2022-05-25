import pprint
import openpyxl
import pandas as pd
import json
from pybit import HTTP
from pandas import json_normalize

# wb = openpyxl.Workbook()

# sheet = wb.active
# sheet['A1'] = 'test'

# wb.save('bybit_symbol.xlsx')


session = HTTP(
    endpoint="https://api.bybit.com", 
)

symbols = session.query_symbol()
result = symbols['result']
# print(result)
# 코인 alias
symbol_alias=[]
# 코인 이름
symbol_name=[]
for symbol in result:
    # 각종목 정보 (주석)
    # pprint.pprint(symbol)
    symbol_alias.append(symbol['alias'])
    symbol_name.append(symbol['name'])
print(symbol_alias)

