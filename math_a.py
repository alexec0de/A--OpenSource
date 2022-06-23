'''
A# - math libs
'''
import math

def check_func_math(func, name_libs, args = None):
	if func == 'pi':
		return math.pi
	elif func == 'sin':
		if args == None:
			print(f'AttributeError: {func} require argument')
		else:
			return math.sin(int(args))
		
	elif func == 'cos':
		if args == None:
			print(f'AttributeError: {func} require argument')
		else:
			return math.cos(int(args))
	elif func == 'sqrt':
		if args == None:
			print(f'AttributeError: {func} require argument')
		else:
			return math.sqrt(int(args))
	else:
		print(f'FunctionError: {func} is undefined on libs {name_libs}')
		
		
#print(math.sqrt(5))
		
	