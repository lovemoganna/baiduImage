#导入urllib.request模块
import urllib.request
from datetime import time
from urllib.parse import urlencode


def get_page_index(offset,keyword):
    data = {
            'tn': 'resultjson_com',
            'ipn': 'rj',
            'ct': '201326592',
            'is': '',
            'fp': 'result',
            'queryWord': keyword,
            'cl': 2,
            'lm': -1,
            'v': 'utf-8',
            'oe': 'utf-8',
            'adpicid':'',
            'st': -1,
            'z': '',
            'ic': 0,
            'word': keyword,
            's': '',
            'se': '',
            'tab': '',
            'width': '',
            'height': '',
            'face': 0,
            'istype': '2',
            'qc': '',
            'nc': 1,
            'fr': '',
            'pn': offset,
            'rn': '30',
            'gsm': '1e',
    }
    # 构建此网址所需要的时间戳字符串
    t =int (round (time.time () * 1000))
    timestamp=str(t)
    headers=('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36')
    url = 'http://image.baidu.com/search/acjson?' + urlencode (data) + timestamp
    # 创建一个opener
    opener=urllib.request.build_opener()
    #将headers添加到opener中
    opener.addheaders=[headers]
    #将opener安装为全局
    urllib.request.install_opener(opener)
    # 用urlopen打开网页
    data=urllib.request.urlopen(url).read().decode('utf-8','ignore')
    print(data)

    def main():
        get_page_index (0, '圆形头像女')


    if __name__ == '__main__':
        main ()
