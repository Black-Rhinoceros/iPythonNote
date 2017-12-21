#
#模拟堆栈
#

#define a stact 
stack=[]

#a char insert into stack 
def pushit():
	stack.append(input('Enter your string:').strip())

#pop a char from stack
def popit():
	if len(stack)==0:
		print("Can't pop from an enpty stack")
	else:
		#stakc.pop()
		#stack=stack[:-1] 不知道为什么不能复制，两个对象不能是同一个名字么？？
		#print(stack[:-1])
		print('Remover[',stack.pop(),']')

def viewstack():
	print(stack)

CMDs={'u':pushit,'o':popit,'v':viewstack}
def showmenu():
	pr='''
	p(u)sh
	p(o)p
	(v)iew
	(q)uit

	enter choice:'''

	while True:
		while True:
			try:
				choice=input(pr).strip()[0].lower()
			except (EOFError,KeyboardInterrupt,IndexError):
				choice='q'
			print('\nYou picked:[%s]'%choice)
			if choice not in 'uovq':
				print('fail,try again')
			else:
				break
		if choice=='q':
			break
		CMDs[choice]()

if __name__=='__main__':
	showmenu()

