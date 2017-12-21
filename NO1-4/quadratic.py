# 请定义一个函数quadratic(a,b,c),接收3个参数，返回一元二次方程：
# ax^2 + bx + c =0(a != 0)的两个解
# 一元二次方程组求根公式 X = [-b±√(b^2-4ac)]/2a
import math
def quadratic(a, b, c):
	if a == 0 :
		print('方程组为一元一次方程',-c/b)
	else:
		if (b*b- 4*a*c ) > 0:
			print('该方程组有两个解',(-b+math.sqrt(b*b-4*a*c))/(2*a),(-b-math.sqrt(b*b-4*a*c))/(2*a))
		elif (b*b- 4*a*c ) == 0:
			print('该方程组有一个解',(-b+math.sqrt(b*b-4*a*c))/(2*a))
		else:
			print('该方程组有无解')

	