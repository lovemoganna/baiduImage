import os, sys

# 打开文件
# 获得读取权限
fd = os.open ("f1.txt", os.O_RDWR)

# 读取文本
# fd - 文件描述符
# n-读取的字节

ret = os.read (fd, 12)
# 将字节转为字符串
print(ret.decode())
# 关闭文件
os.close (fd)
print("关闭文件成功!!")
