# 计算淘宝动态评分，算出差多少人能到行业平均分
import requests
from bs4 import BeautifulSoup
import re

address = 'https://shop140596725.taobao.com'
text = requests.get(address)
# print(text.text)

soup = BeautifulSoup(text.text)
html_content = soup.find_all('a', 'mini-dsr J_TGoldlog')
url = html_content[0].attrs['href']

full_url = address + url[1:]
print(full_url)

people = 100
ms = 4 * people
fw = 3 * people
wl = 2 * people

ms_g = 4 / (1 - 0.05) * people
fw_g = 3 / (1 - 0.04) * people
wl_g = 2 / (1 - 0.03) * people

ms_xu = (ms_g - ms) / 5
fw_xu = (fw_g - fw) / 5
wl_xu = (wl_g - wl) / 5

print(
    '描述分数需：{}人\n'.format(ms_xu),
    '服务分数需：{}人\n'.format(fw_xu),
    '物流分数需：{}人\n'.format(wl_xu),
)
