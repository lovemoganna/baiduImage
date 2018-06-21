import os
img_url = 'http://img1.imgtn.bdimg.com/it/u=1901239711,355782583&fm=214&gp=0.jpg'
# 获得url后缀
file_suffix = os.path.splitext (img_url)[1]

print(file_suffix)

# # splitext 获取文件名和扩展名
# path = '/home/shawn/hello.py'
# print(os.path.splitext(path)) # ('/home/shawn/hello', '.py')
# print(os.path.splitext(path)[0]) # /home/shawn/hello
# print(os.path.splitext(path)[1]) # .py
#
# # python 中的路径
#
# # 获得当前路径
# print(os.getcwd()) # F:\pythonProject\baiduImage\language
#
# path_list = ['first_directory', 'second_directory', 'file.txt']
#
# import os
# base_dir = os.path.dirname(__file__)
# # 获取当前文件目录
# path = os.path.join(base_dir,'123.txt')
# # 获取文件拼接后的路径