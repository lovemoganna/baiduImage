import json
from multiprocessing.dummy import Pool
from urllib.parse import urlencode

import requests
from requests import RequestException
import time


# 1.获得详情页的内容,就是一个json
from downloadImage.download_image_by_request import download_image


def get_page_index(offset, keyword):
    try:
        data = {'tn': 'resultjson_com', 'ipn': 'rj', 'ct': '201326592', 'is': '', 'fp': 'result', 'queryWord': keyword,
                'cl': 2, 'lm': -1, 'v': 'utf-8', 'oe': 'utf-8', 'adpicid': '', 'st': -1, 'z': '', 'ic': 0, 'word': keyword,
                's': '', 'se': '', 'tab': '', 'width': '', 'height': '', 'face': 0, 'istype': '2', 'qc': '', 'nc': 1,
                'fr': '', 'pn': offset, 'rn': '30','gsm':'1e'}
        # 构建此网址所需要的时间戳字符串
        t = int (round (time.time () * 1000))
        timestamp = str (t)
        url = 'http://image.baidu.com/search/acjson?' + urlencode (data) + timestamp
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
        response = requests.get (url, headers=headers,timeout=16)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print ('请求索引页出错!')
        return None



# 解析json文件
def parse_json_get_image_url(html):
    html =json.loads(html)
    if html:
            data = html['data']
            if data:
                for item in data:
                    if item and 'replaceUrl' in item.keys():
                        for item in item['replaceUrl']:
                            yield item['ObjURL']



from config import  *

def main(offset):
    json = get_page_index (offset, KEYWORD)
    # print(json)
    # 解析JSON数组.
    if json:
        result = parse_json_get_image_url(json)
        if result:
            for i in result:
                # 这样就解析出很多图片了,注意有一些图片是存在着缓存过期这个问题的,甚至源服务器已经删除了这类图片,我们测试只要能下载部分和我们类似的就可以了.
                # print(i)
                print ('正在下载URL为 ', i, ' 的图片')
                download_image (i)


if __name__ == '__main__':
    groups = [x * 20 for x in range (GROUP_START, GROUP_END + 1)]
    main (groups)
    # 引入多线程中的进程池
    pool = Pool ()
    # 开启多线程
    pool.map (main, groups)

# t = time.time ()
# print (int(round(t * 1000)))

# 1529380468735
# 1529380761018
