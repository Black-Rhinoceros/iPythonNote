def normalize(name):
	r = name.lower()
	return r.capitalize()

# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
if L2 == ['Adam', 'Lisa', 'Bart']:
	print('测试成功')