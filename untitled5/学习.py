# import os
# list = [1,1,3,5,6,6,8,9,4,4,5]
# set(list)
# print(set(list))


# a = [('2011-03-17', '2.26', 6429600, '0.0'), ('2011-03-16', '2.26', 12036900, '-3.0'),
# ('2011-03-15', '2.33', 15615500,'-19.1')]
# print (a[0][0])
# print(a)
# b = sorted(a,key=lambda result:result[0],reverse=True)
# print(b)
# c = sorted(b,key=lambda result:result[3],reverse=True)
# print (c)


# from operator import itemgetter
# aa = {"c":"3","dee":"4","ff":"1","b":"2"}
# print(aa)
# bb = sorted(aa.items(),key=itemgetter(1))
# print(bb)


# aa = {"c":"3","dee":"4","ff":"1","b":"2"}
# print(["%s=%s" % (k,v) for k,v in aa.items()])

# import datetime
# a = datetime.datetime.now() - datetime.timedelta(hours=10).strftime("%Y-%m-%d-%H:%M:%S")
# print(a)


# str = "abcdefg"
# print("%.3s"%str)

# num = 10
# print("HEX=%x" % num)


 # print(10 // 2)
# import os
# print(ord('A'))
# print(chr(25991))
#
# #
# list = ['Michael', 'Bob', 'Tracy']
# # print(list)
# # print(len(list))
# # print(list[-1])
# # list.append('zch')
# # list.insert(1,'lzl')
# # print(list)
# # list.pop(1)
# list[0] = 'lzz'
# print(list)


# age = 15
# if age >= 18:
#     print('teenager')
# elif age >= 6:
#     print('adult')
# else:
#     print('kid')


# birth = int(input('birth:'))
# if birth < 2000:
#     print('00前')
# elif birth > 2000:
#     print('00后')




# height = 1.75
# weight = 80.5
# s =  float((weight / height)**2)
# bmi = s
# if bmi < 18.5:
#    print('过轻')
# elif bmi < 25:
#    print('正常')
# elif bmi < 28:
#    print('过重')
# elif bmi < 32:
#    print('肥胖')
# else :
#    print ('严重肥胖')


# sum = 0
# for i in range(101):
#     sum = sum + i
#     #sum += i
# print(sum)

#
# L = ['Bart', 'Lisa', 'Adam']
# for name in L:
#     print('hello,',name)


# n = 1
# while n <= 100:
#     if n > 10: # 当n = 11时，条件满足，执行break语句
#         break # break语句会结束当前循环
#     print(n)
#     n = n + 1
# print('END')


# n = 0
# while n < 10:
#     n = n + 1
#     if n % 2 == 0: # 如果n是偶数，执行continue语句
#         continue # continue语句会直接继续下一轮循环，后续的print()语句不会执行
#     print(n)
#
# print('%s' % hex(255))
# x = int(input('请输入你的数字：'))
# def zch(x):
#     if x > 0:
#         return x
#     else:
#         return -x
# print(zch(x))d

#x = int(input('请输入你的数字：'))
# x = [5,6,2]
# def product(x):
#     L = 1
#     n = len(x)
#     for i in x:
#         L*=i
#     return L
# print(product())


# f = open('zch.txt','r','encoding='UTF-8')
# print(f.read(zch,10))
# from os import path
# f = open(r'C:\Users\Po1son\PycharmProjects\untitled5\zch','r',encoding='UTF-8')
# L = f.readlines()
# for i in range(5):
#     # L = f.readline().strip()
#     print(L[i])
# # s = f.readlines(10)
# # l = f.readline()
# # print(s)
# f.close()

# for i in range(1,10):
#     for j in range(1,i+1):
#         print (i,'*',j,"=",i*j,end=' ')
#     print()


#
# s = ' abcdadfg '
# s1 = 'HHHHSHHS'
# s2 = 'aaaaBBBB'
# # print(info.find('a',1))
# # print(info.index('a'))
# # print(info)
# # print(info.strip())
# # print(info.rstrip())
# print(s2.swapcase())




