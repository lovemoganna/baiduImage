import os
import urllib.request
url='http://www.baidu.com'

# 进入到当前目录下
dir=os.path.abspath('.')
work_path=os.path.join(dir,'baidu.html')
urllib.request.urlretrieve(url,work_path)
