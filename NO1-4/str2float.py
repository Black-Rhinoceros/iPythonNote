from functools import reduce
def str2float(s):
	def str2list(b):
		return {'.':'.','0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[b]
	L = list(map(str2list,s))
	for i , value in enumerate(L):  #不能只留i，否则会报类型错误
		if L[i]=='.':
			x = i                   #不能用return返回i值，因为return表示程序结束
	L1 = L[0:x]
	L2 = L[x+1:] 
	a =len(L2)
	return reduce(lambda x,y:x * 10 +y , L1)+reduce(lambda x,y:x * 10 +y , L2)*10**(-a)

print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')