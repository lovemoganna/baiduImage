#!/usr/bin/env python
# coding=utf-8
import os
import urllib.request

# 下载文件,并显示下载进度
def cbk(a, b, c):
    '''''回调函数
    @a:已经下载的数据块
    @b:数据块的大小
    @c:远程文件的大小
    '''
    per = 100.0 * a * b / c
    if per > 100:
        per = 100
        # %.2f是指显示小数点后两位,%f为float浮点数的一般显示格式。
        # %% 指的就是真的%
    print('已经下载','%.2f%%' % per)

# url = 'http://www.python.org/ftp/python/2.7.5/Python-2.7.5.tar.bz2'
def download_file(iamge_url,file_name):
    dir = os.path.abspath ('.')
    work_path = os.path.join (dir, file_name)
    urllib.request.urlretrieve (iamge_url, work_path, cbk)