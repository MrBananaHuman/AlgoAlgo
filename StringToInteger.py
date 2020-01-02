import re

class Solution:
    def myAtoi(self, str: str) -> int:
        neg_flag = False
        symbols = re.compile('[\\+\\-a-zA-Z가-힣]')
        modi_s = str.strip().split('.')[0].split(' ')[0]
        if not modi_s.replace('-', '').replace('+', ''):
            return 0
        if modi_s[0] == '-':
            neg_flag = True
            modi_s = modi_s[1:]
        elif modi_s[0] == '+':
            modi_s = modi_s[1:]
        if not modi_s.replace('-', '').replace('+', ''):
            return 0
        symbol_cnt = re.search(symbols, modi_s)
        if symbol_cnt == None:
            if neg_flag:
                modi_s = '-' + modi_s
            if int(modi_s) >= 2**31-1:
                return 2**31-1
            elif int(modi_s) <= -2**31:
                return -2**31
            else:
                return int(modi_s) 
        elif symbol_cnt.start() == 0:
            return 0
        else:
            modi_s = modi_s[0:symbol_cnt.start()]
            if neg_flag:
                modi_s = '-' + modi_s
            if int(modi_s) >= 2**31-1:
                return 2**31-1
            elif int(modi_s) <= -2**31:
                return -2**31
            else:
                return int(modi_s)
            
        
