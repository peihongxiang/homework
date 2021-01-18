import base64
import time
import random
from tkinter import Image

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PIL import Image
# options = webdriver.ChromeOptions()
# # 设置中文
# options.add_argument('Authorization=tokentest2345534fejr344')
# options.add_argument('lang=zh_CN.UTF-8')
# # 更换头部
# options.add_argument(
#     'user-agent=baidu')
# browser = webdriver.Chrome(chrome_options=options)
# url = "https://httpbin.org/get?show_env=1"
# browser.get(url)
class Login():
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument(
            'user-agent=Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89dff.0.3497.100 Safari/537.36')
        options.add_argument(
            'Authorization=Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjZ3eV93WmVqdkNfWHNpRi1PS0V3Y09UUjlJUFRqYTBuWi1zWC1IYXdkd2sifQ.eyJqdGkiOiJ5OVExWUx3Zn44NmptOXJHS3M3MlAiLCJzdWIiOiIwMDAwMDAxNDkwIiwiaXNzIjoiaHR0cHM6Ly9hdXRoLmFtYmVyb3RjLmNvbSIsImlhdCI6MTYxMDg4NDE4MCwiZXhwIjoxNjEwOTcwNTgwLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIG9mZmxpbmVfYWNjZXNzIiwiYXVkIjoiQXBvbGxvIn0.IX_eL9VYqao5QHrnPKrdnooBquu7KDKdpC4c7WO__8KzzC57ZeMawS3-5TF98Dycgpd44lUaEPK9HjsCM5wdkRKb62EFbGfloCv8LrpjXfWftjRAJtF31GFdU_MbO9bsLywYBbkK0U0qcAp8kHs9FBrXXH7d_8VL_o-_UTrl9oVKdwMXF2Pl26E5ziAoJQ2V953o9Ydq4wO05E3S7e3LEla_QmWof89lLCqTRK-s3daOul19oUv9ynUYSpQqcvkTMJ6kRcQ3BYi1nBwQ2E0lFwSvqn1FKuTw2xHfGEXvVGH6maQUVKen_HnHtY0yo72U5mL7wl1ZAK8FlS9J6XsXUg')
        self.driver = webdriver.Chrome(chrome_options=options)
        self.driver.implicitly_wait(20)
#         options = webdriver.ChromeOptions()
#         # 设置中文
#         options.add_argument('lang=zh_CN.UTF-8')
#         # 更换头部
#         options.add_argument(
#             'user-agent="Mozilla/5.0 (iPod; U; CPU iPhone OS 2_1 like Mac OS X; ja-jp) AppleWebKit/525.18.1 (KHTML, like Gecko) Version/3.1.1 Mobile/5F137 Safari/525.20"')
#         browser = webdriver.Chrome(chrome_options=options)
#         url = "https://httpbin.org/get?show_env=1"
#         browser.get(url)
#
#         # self.driver = webdriver.Chrome()
#         # self.driver.get("https://amberotc.com/")
#         # self.driver.get("https://www.baidu.com")
#         # js = 'window.localStorage.setItem("Authorization","Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjZ3eV93WmVqdkNfWHNpRi1PS0V3Y09UUjlJUFRqYTBuWi1zWC1IYXdkd2sifQ.eyJqdGkiOiJ5OVExWUx3Zn44NmptOXJHS3M3MlAiLCJzdWIiOiIwMDAwMDAxNDkwIiwiaXNzIjoiaHR0cHM6Ly9hdXRoLmFtYmVyb3RjLmNvbSIsImlhdCI6MTYxMDg4NDE4MCwiZXhwIjoxNjEwOTcwNTgwLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIG9mZmxpbmVfYWNjZXNzIiwiYXVkIjoiQXBvbGxvIn0.IX_eL9VYqao5QHrnPKrdnooBquu7KDKdpC4c7WO__8KzzC57ZeMawS3-5TF98Dycgpd44lUaEPK9HjsCM5wdkRKb62EFbGfloCv8LrpjXfWftjRAJtF31GFdU_MbO9bsLywYBbkK0U0qcAp8kHs9FBrXXH7d_8VL_o-_UTrl9oVKdwMXF2Pl26E5ziAoJQ2V953o9Ydq4wO05E3S7e3LEla_QmWof89lLCqTRK-s3daOul19oUv9ynUYSpQqcvkTMJ6kRcQ3BYi1nBwQ2E0lFwSvqn1FKuTw2xHfGEXvVGH6maQUVKen_HnHtY0yo72U5mL7wl1ZAK8FlS9J6XsXUg")'
#         # self.driver.execute_script(js)
#         # self.driver.refresh()
        self.driver.get("https://amberotc.com/client/trade")

    def login(self):
        print("aaa")



if __name__ == "__main__":
    b = Login()
    b.login()
#
