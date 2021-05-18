import requests

'''
from bs4 import BeautifulSoup
import pandas as pd
'''

url = "http://www.baidu.com"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/86.0.4240.75 "
                  "Safari/537.36 "
}

'''response = requests.get(url, headers=headers)'''

response = requests.get(url)

response.encoding = "utf-8"

print('状态码：' + str(response.status_code))

'''print("\nr的类型" + str(type(response)))

print("\n头部信息:" + str(response.headers))

print("\n响应内容:")

print(response.text)
'''
r = requests.get("http://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png", headers=headers)
print("状态码：" + str(r.status_code))

'''file = open("F:\\11_PythonWorkSpace\\download files\\download.html", "w",
            encoding="utf")  # 打开一个文件，w是文件不存在则新建一个文件，这里不用wb是因为不用保存成二进制
file.write(response.text)
file.close()'''

file = open("F:\\11_PythonWorkSpace\\download files\\baidu.png", "wb")
file.write(r.content)
file.close()
