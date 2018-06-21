import hashlib


# src = 'this is a md5 test.'
# m2 = hashlib.md5()
# m2.update(src.encode('utf-8'))
# print(m2.hexdigest())


# str->bytes:encode编码
# bytes->str:decode解码

src = 'http://p1.pstatp.com/orig/11298' + '.jpg'

def random_create_md5(src):
    image_url = src.encode ('utf-8')
    m = hashlib.md5 ()
    # 哈希对象
    # print (m)
    # 用string参数arg更新md5对象
    m.update (image_url)
    # 以16进制的形式返回摘要
    file_name = m.hexdigest ()
    return file_name

# def main():
#     name = random_create_md5(src)
#     print(name)
# if __name__ == '__main__':
#     main()
