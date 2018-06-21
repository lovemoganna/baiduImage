import os
from _md5 import md5

import requests
# 这种方式是往文件里面写入图片的二进制数据.
from requests import RequestException

from config import *


# url = 'http://pic.qqtn.com/up/2017-12/15139132592016065.jpg'
def save_image(content, url):
    # file_suffix = os.path.splitext (url)[1]
    # file_path=FILEPATH
    # file_all_path= '{}{}{}{}'.format (file_path, os.sep, md5 (content).hexdigest (), file_suffix)
    try:
        file_all_path = '{0}/{1}.{2}'.format (os.getcwd(), md5 (content).hexdigest (), 'jpg')
        if not os.path.exists (file_all_path):
            # 保存为一个文件
            with open (file_all_path, 'wb') as f:
                f.write (content)
                f.close ()
                print(KEYWORD,'---风格的图片---',url,'下载成功!')
    except Exception as e:
        print ("下载图片失败!")


# 下载图片之前,需要校验url的合法性,过滤不符合条件的image_url
def download_image(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
        response = requests.get (url, headers=headers, timeout=16)
        if response.status_code == 200:
            # return response.text
            # content返回二进制内容,text返回网页的正常结果.
            save_image (response.content, url)
        return None
    except RequestException:
        pass

# def main():
#     download_image (url)
#
#
# if __name__ == '__main__':
#     main ()
