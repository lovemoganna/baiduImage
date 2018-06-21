# format方法用于字符串的格式化输出
import urllib.request

print('{0}+{1}={2}'.format(1,2,1+2))  # 0+1 = 3
#
import os
# os.sep  操作系统特定的路径分隔符，win下为"\\",Linux下为"/"
url = 'http://img.duoziwang.com/2016/12/30/18213518949.jpg'
file_sufix = os.path.splitext (url)[1]
filename = '{}{}{}{}'.format ('D:/book/img', os.sep, 'xiaoming',file_sufix)
# D:/book/img\xiaoming.jpg
# urllib.request.urlretrieve(url,filename)
print(filename)