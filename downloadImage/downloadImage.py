import os
import urllib.request
from _md5 import md5

import requests
from requests import RequestException

from md5.randomCreateMD5 import random_create_md5

# 这种方式是往文件里面写入图片的二进制数据.

def save_image(content):
    file_path = 'D:/book/img'
    try:
        # 是否有这个路径
        if not os.path.exists (file_path):
            os.makedirs (file_path)
            # 创建路径
            file_path = '{0}/{1}'.format (file_path, md5 (content).hexdigest ())
            if not os.path.exists (file_path):
                # 保存为一个文件
                with open (file_path, 'wb') as f:
                    f.write (content)
                    f.close ()
    except Exception as e:
        print ("下载图片失败!")

# 下载图片之前,需要校验url的合法性,过滤不符合条件的image_url
def download_image(url):
    try:
        response = requests.get (url,timeout=5)
        if response.status_code == 200:
            # return response.text
            # content返回二进制内容,text返回网页的正常结果.
            save_image (response.content)
        return None
    except RequestException:
        print ('这个url有问题! ', url)
        return None

# 第二种下载图片的方式
def download_image2(img_url):
    file_path = 'D:/book/img'
    file_name = random_create_md5(img_url)
    try:
        # 是否有这个路径
        if not os.path.exists (file_path):
            # 创建路径
            os.makedirs (file_path)
            # 获得图片后缀
            file_suffix = os.path.splitext (img_url)[1]
            # print (file_suffix)
            # 拼接图片名（包含路径）
            filename = '{}{}{}{}'.format (file_path, os.sep, file_name, file_suffix)
            # 下载图片，并保存到文件夹中
            urllib.request.urlretrieve (img_url, filename=filename)
            print('下载成功!')
    except IOError as e:
        print ("IOError")
    except Exception as e:
        print ("Exception")


# def main():
#     download_image('http://p1.pstatp.com/origin/pgc-image/15294985067947497d4093e')
#
#
# if __name__ == '__main__':
#     main ()
