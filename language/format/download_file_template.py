import hashlib
import os
import urllib.request

url = 'http://pic.qqtn.com/up/2017-12/15139132592016065.jpg'
from md5.randomCreateMD5 import random_create_md5


def download_images(url):
    file_path = 'F:/pythonProject/baiduImage/hi'
    file_name = random_create_md5(url)
    try:
        if not os.path.exists (file_path):
            os.makedirs (file_path)
            # 获取URL的后缀
            file_end_with = os.path.splitext (url)[1]
            file_all_name = "{}{}{}{}".format (file_path, os.sep, file_name, file_end_with)
            # 根据file_all_name下载图片,并存储到相应的位置中去
            urllib.request.urlretrieve (url, filename=file_all_name)
        print (url, '--------下载成功')
    except IOError:
        print ("IOError--------", url)
    except Exception:
        pass


# 计算出一个字符串的MD5值作为file_name
def random_create_md5_file_name(url):
    # 生成一个hash对象
    m = hashlib.md5 ()
    # 给这个hash对象附加url的信息.
    m.update (url.encode('utf-8'))
    # 将这个md5加密的哈希值转成16进制
    m.hexdigest ()





def main():
    download_images (url)


if __name__ == '__main__':
    main ()
