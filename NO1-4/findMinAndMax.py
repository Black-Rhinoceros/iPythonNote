def findMinAndMax(L):
	if len(L) == 0:
		return (None,None)
	max = min = L[0]
	for x in L :
		if x <= min :
			min = x
		elif x > max:
		    max = x
	return (min,max)
# # 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!1')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!2')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!3')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!4')
else:
    print('测试成功!')