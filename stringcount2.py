import pprint

message = 'It was a bright cold day in april, and the clocks were striking thirteen.'

dic={}



for c in message:
    if c not in dic: 
        dic[c] = 1
    else:
        dic[c] = dic[c] + 1
pprint.pprint (dic)
