# -*-coding:UTF-8 -*-
# from random import random
# from python_project.123.123.111 import cai
# 
# print('我爱包包')
# 
# 
# def total():
#     total = 0
#     for i in range(1, 101):
#         total = i + total
#     
#     print('1+2+3+....+100的和:%s' % total)
#     
# total()
# def zhengchu():
#     num_list = []
#     for i in range(101):
#         if i % 3 == 0 and i % 5 != 0:
#             num_list.append(i)
#     print("100以内能被3整除但是不能被5整除的数:%s" % num_list)
# 
# def shuigang():
#     total = 0
#     
#     for i in range(0, 50, 4):
#         if i <= 50 - 15:
#             total = total + 1
#     
#     print('%s次可以挑完' % total)

class Cai():
    def cai(self):    
        me = random.randint(1, 100)
        total = 0
        print(me)
        for i in range(1001):
            guess = int(input('请输入你要猜测的数（1-100包含1和100）：'))
            if guess > me:
                total = total + 1
                print('大了')
            elif guess < me:
                total = total + 1
                print('小了')
            else:
                total = total + 1
                print('猜对了，喝酒吧,我们测了%s次才正确' % total)
                break
   
            caishu=Cai()
            cs=caishu.cai()
            print(cs)
