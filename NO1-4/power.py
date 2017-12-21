#设置默认参数计算x的2次方
def power(x,n=2):
	s = 1
	while n > 0:
		n = n -1
		s = s * x
	return s
