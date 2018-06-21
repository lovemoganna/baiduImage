for x in range (2, 10, 2):  # 范围是 2<=x<10 ,步长为2
    print (x)  # 2 4 6 8

lists = [x * 5 for x in range (2, 10, 2)]
print(isinstance(lists,list)) # True
print(lists) # [10, 20, 30, 40]