# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 19:00:42 2023

@author: User
"""
# 查看星座運勢


import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

driverpath=os.path.join(r'C:\Users\User\Desktop','chromedriver.exe')

# 查詢星座
starsign='雙子座'
# 今日運勢=1,明日運勢=2,本周運勢=3,本月運勢=4
when=input('請輸入欲查詢運勢代號(int):')
try:
    when_int = int(when)
    if not 1 <= when_int <= 4:
        raise ValueError
except ValueError:
    raise ValueError('請輸入正確數字: 1~4')

# chrome_options = Options()
# chrome_options.add_argument("--headless")
# driver = webdriver.Chrome(service=Service(driverpath), options=chrome_options)
driver = webdriver.Chrome(service=Service(driverpath))

driver.get('https://www.elle.com/tw/starsigns/')
time.sleep(1)
assert '12星座運勢' in driver.title

# 獲得連結
starsignURL=[]
link_elements = driver.find_elements(By.XPATH, f"//a[text()='{starsign}']")
for link_element in link_elements:
    if starsign in link_element.text:
        link_url = link_element.get_attribute('href')
        starsignURL.append(link_url)

redirect_url=starsignURL[when_int-1]
driver.get(redirect_url)
time.sleep(10)
driver.quit()
print('done')
