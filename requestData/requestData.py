from urllib.parse import urlencode

import requests
from requests import RequestException
import time

from parseJson.parseJson import parse_json


def get_page_index(offset, keyword):
    data = {'tn': 'resultjson_com', 'ipn': 'rj', 'ct': '201326592', 'is': '', 'fp': 'result', 'queryWord': keyword,
        'cl': 2, 'lm': -1, 'v': 'utf-8', 'oe': 'utf-8', 'adpicid': '', 'st': -1, 'z': '', 'ic': 0, 'word': keyword,
        's': '', 'se': '', 'tab': '', 'width': '', 'height': '', 'face': 0, 'istype': '2', 'qc': '', 'nc': 1, 'fr': '',
        'pn': offset, 'rn': '30', 'gsm': '1e', }
    # 构建此网址所需要的时间戳字符串
    t = int (round (time.time () * 1000))
    timestamp = str (t)
    url = 'http://image.baidu.com/search/acjson?' + urlencode (data) + timestamp
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
    }

    try:
        response = requests.get (url, headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print ('请求索引页出错!')
        return None


def main():
    json = get_page_index (0, '圆形头像女')
    # print(json)
    # 解析JSON数组.
    parse_json(json)


if __name__ == '__main__':
    main ()

# t = time.time ()
# print (int(round(t * 1000)))

# 1529380468735
# 1529380761018
