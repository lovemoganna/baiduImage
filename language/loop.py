# info = {'name': 'xiaoming', 'sex': 'nan', 'age': 20, 'id': 1}
#
# info2 = {'name': 'hhh', 'sex': 'nv', 'addr': 'beijign'}
#
# for k, v in info.items ():
#     print ('%s is %s' % (k, v))
#
# for k in info2:  # 这种方式效率比较高
#     print (k, info2[k])

html = '''
[{'ObjURL': 'http://img0.imgtn.bdimg.com/it/u=2088399050,2325131921&fm=214&gp=0.jpg',
         'FromURL': 'http://www.gexing.com/qqtouxiang/2621935_3.html'},
        {'ObjURL': 'http://p1.gexing.com/g1/m00/d1/47/rbace1pupqatmgijaad-m_d7lqg655_200x200_3.png?recache=20131108',
         'FromURL': 'http://www.gexing.com/qqtouxiang/3518587_2.html'}]
'''

# 解密百度的ObjURL,这种方式可行,但是不知道原理.待研究.
import re

txt = 'ippr_z2C$qAzdH3FAzdH3Fr8_z&e3B2jxtg2_z&e3Bv54AzdH3FG8AzdH3FMaaAzdH3F8AAzdH3FDFAzdH3F6BACFFHasueTnA8VAAEG-T3CH7Unb9_daaxdaa_n_z&e3Brg2?6jvwvij=da8n88ab'


def baidtu_uncomplie(url):
    res = ''
    c = ['_z2C$q', '_z&e3B', 'AzdH3F']
    d = {'w': 'a', 'k': 'b', 'v': 'c', '1': 'd', 'j': 'e', 'u': 'os', '2': 'g', 'i': 'h', 't': 'i', '3': 'j', 'h': 'k',
         's': 'l', '4': 'm', 'g': 'n', '5': 'o', 'r': 'p', 'q': 'q', '6': 'r', 'os': 's', 'p': 't', '7': 'u', 'e': 'v',
         'o': 'w', '8': '1', 'd': '2', 'n': '3', '9': '4', 'c': '5', 'm': '6', '0': '7', 'b': '8', 'l': '9', 'a': '0',
         '_z2C$q': ':', '_z&e3B': '.', 'AzdH3F': '/'}
    if (url == None or 'http' in url):
        return url
    else:
        j = url
        for m in c:
            j = j.replace (m, d[m])
        for char in j:
            if re.match ('^[a-w\d]+$', char):
                char = d[char]
            res = res + char
        return res


print (baidtu_uncomplie (txt))
