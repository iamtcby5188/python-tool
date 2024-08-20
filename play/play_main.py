import time

from selenium import webdriver

driver = webdriver.Chrome()  # 这里可以改为其他支持的浏览器，如 Firefox 等
driver.get('https://www.baidu.com')
while True:
    print('----s')
    time.sleep(1)