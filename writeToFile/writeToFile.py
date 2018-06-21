import json
# 从json里面解析出image_url之后，将截取的URL写到一个文件里面.
def write_to_file(content):
    with open ('./photoURL.txt', 'a', encoding='UTF-8') as f:
        # 通过json转为字符串的形式存储,后面是为了解决编码问题.
        f.write (json.dumps (content, ensure_ascii=False) + '\n')
        f.close ()