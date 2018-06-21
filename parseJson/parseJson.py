# 常用语法: json.dumps(): 对数据进行编码。 json.loads(): 对数据进行解码。

import json
import os
import urllib



def parse_json(file):
    f = open (file, encoding='utf-8')
    # 读取文件
    res = f.read ()
    # 把json串变成python的数据类型：字典
    dicts = json.loads (res)
    # 获取里面的data数据
    datas = dicts['data']
    # datas是一个list,需要遍历
    # print(datas[0])

    # 将list转换为有索引的枚举类型
    for i, value in enumerate (datas):
        # print(i,value)
        for key in value:
            # print(key,value[key])
            if (key == 'hoverURL'):
                print(value['hoverURL'])
                # download_photo(image_url)
                # print(image_url)

                #取出文件的URL
                # write_to_file(image_url)

def main():
    image_url =parse_json ('./baiduImage.json')
    print(image_url)


if __name__ == '__main__':
    main ()
