#!/usr/bin/python
# _*_ coding: UTF-8 _*_

import os, sys

# os.O_RDWR : 以读写的方式打开
# os.O_CREAT: 创建并打开一个新文件

import os, sys

# 打开文件
fd = os.open( "foo.txt", os.O_RDWR|os.O_CREAT )

# 写入字符串,就是一个替换的过程
# 这里会出现一个错误,需要我们将字符串编译成bytes类型
os.write(fd, "This is test".encode())

# 关闭文件
os.close( fd )

print ("关闭文件成功!!")