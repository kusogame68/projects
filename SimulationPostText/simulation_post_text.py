# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 15:49:48 2023

@author: Johnson
"""

'''
[ Request 模擬發文]
說明 : 此小作品為模擬發文，考量到大部分服務器會設置非人類user瀏覽的抵制功能，
    因此以requests函式庫模擬人類使用者在網頁使用時的狀態讓服務器python是人。
    
Tips:請事先登入完成及抓取authorization，目前僅發送文字功能
'''

import requests as req

url='https://qa.pixnet.cc/personal_articles?with_member_profile=true'

# authorization,useragent,text,pictures 請輸入個人資訊
authorization='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJhcGkucGl4bmV0LmNjIiwibWVtYmVyX3VuaXFpZCI6IjE5NDA1NjRmNDQ3MWQ1Mjc3NyIsInRva2VuIjoiMmI2Y2U1MDNkZTZmMzRjMmZhMDUyMzY0NTcwZDQ2OGMiLCJpYXQiOjE2OTM3NDI0ODcsImV4cCI6MTY5Mzc0NjA4N30.dty30vOOfG9bjxVWl9FJXS0dNYdSw_Hq65w-pf_FUik'
useragent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
text="你好" # 要傳入的文字
pictures='' # 要傳入的圖片

try:
    # set模擬人類使用
    setting={
        # Authorization : 授權狀態
        'Authorization':f'{authorization}',
        # User-Agent : 使用者代理
        'User-Agent':f'{useragent}',
        }

    # content-type:text/palane;charset=utf-8
    if pictures=='':
        textdata='{"content":"text","source":"www","pictures":[]}'.replace('text',str(text))
    else:
        textdata='{"content":"text","source":"www","pictures":[image]}'.replace('text',str(text)).replace('image',str(pictures))

    rsp=req.post(url,headers=setting,data=textdata.encode('utf-8'),timeout=3)
    print('url.status=',rsp.status_code)

except Exception as e:
    print(e)

finally:
    print('Programing is done')

