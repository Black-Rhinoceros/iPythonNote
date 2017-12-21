#求1*2*n的乘积
def product(*number):
	s = 1
	for n in number:
		s = s * n
	return s
