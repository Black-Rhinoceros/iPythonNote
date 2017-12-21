#  求n！  含测试代码
# def product(*number):
#     if  len(number) == 0:
#         raise TypeError
#     s = 1
#     for n in number:
#         s = s * n
#     return s
# print('product(5) =', product(5))
# print('product(5, 6) =', product(5, 6))
# print('product(5, 6, 7) =', product(5, 6, 7))
# print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
# if product(5) != 5:
#     print('测试失败!')
# elif product(5, 6) != 30:
#     print('测试失败!')
# elif product(5, 6, 7) != 210:
#     print('测试失败!')
# elif product(5, 6, 7, 9) != 1890:
#     print('测试失败!')
# else:
#     try:
#         product()
#         print('测试失败!')
#     except TypeError:
#         print('测试成功!')

i = input ('please input a int data :')

if type(i) == type(1):
#if i is None:
    print (1)
    #print (i)
    # raise ValueError
    print (2)
else:
	print ("i的类型：",type(i))
	print("数字1的类型",type(1))

