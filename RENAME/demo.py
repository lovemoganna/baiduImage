import os

# 定义一个路径
path = 'D:/360Downloads/images'

# 查出文件列表
fileList = os.listdir (path)
print (fileList) # 这是一堆文件名的路径list

# 获得文件列表的长度
image_number = len (fileList)
print (image_number)  # 19

# 遍历这个文件列表

for index, item in enumerate (fileList):
    if item.endswith ('.jpg'):
        # os.path.abspath()---获取文件当前路径
        src = os.path.join (os.path.abspath (path), item)
        dst = os.path.join (os.path.abspath (path), str (index) + '.jpg')
        try:
            os.rename (src, dst)
            print ('重命名 %s to %s' % (src, dst))
        except:
            continue
print('一共有 %d 张图片正在改名,现在改了 %s 张图片' % (image_number,index+1))
