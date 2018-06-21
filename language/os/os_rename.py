import os, sys
# src -- 要修改的目录名
# dst -- 修改后的目录名
# 列出目录
print ("目录为: %s" % os.listdir (os.getcwd ()))

# 重命名目录
os.rename ("test", "test2")

print ("重命名成功。")

# 列出重命名后的目录

# %s 代表后面的字符串内容.
# %d 后面如果是数字的话,用%d来代替.
print ("目录为: %s" % os.listdir (os.getcwd ()))

