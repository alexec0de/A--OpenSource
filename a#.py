from sys import argv
from math_a import check_func_math
from sqllite3_a import check_func_sqlite3
from discord_a import check_func_discord
from http_a import  check_func_http
path = argv[1] if __name__ == "__main__" else argv[0]

if_if = False
VARS = {}
LIBS ={}
def isint(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def isf(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
def issplit(s):
	try:
		s.split(' ', 1)[1]
		return True
	except IndexError:
		return False

def islibs(s):
	try:
		s.split('.', 1)[1]
		return True
	except IndexError:
		return False
		
		
def islibss(s):
	try:
		s.split('.', 2)[2]
		return True
	except IndexError:
		return False
		
		


with open(path) as f:
  code = f.readlines()

for s in code:
  fn = s.split(" ", 1)[0]
  #val = s.split(" ", 1)[1] if s.split(" ", 1)[1] else None
  if fn == 'print':
  	val = s.split(' ', 1)[1]
  	if val[0] == '"' or val[0] == "'":
  		if val[-1] == '\n':
  			val = val[:-1]
  			print(val[1:-1])
  		else:
  			print(val[1:-1])
  	else:
  		if val[-1]== '\n':
  			val = val[:-1]
  		if val in VARS:
  			test_var = VARS[val]
  			print(test_var)
  		else:
  			if islibs(val) == True:
  				name_libs = val.split('.', 1)[0]
  				func = val.split('.', 1)[1]
  				if name_libs in LIBS:
  					if name_libs == 'math':
  						if issplit(func) == True:
  							func_final = func.split(' ', 1)[0]
  							args = func.split(' ', 1)[1]
  							result = check_func_math(func_final, name_libs, args)
  							print(result)
  						else:
  							result = check_func_math(func, name_libs)
  							print(result)
  				else:
  					print(f'NameError: {name_libs} is not undefined')
  					break
  			else:
  				
  				print(val)
  elif fn == 'var':
  	name_var = s.split(' ', 2)[1]
  	var = s.split(' ', 2)[2]
  	var_final = var.split(' ', 1)[1]
  	if var_final[0] == '"' or var_final[0] == "'":
  		VARS[name_var] = var_final[1:-1]
  	else:
  		if issplit(var_final) == True:
  			opration = var_final.split(' ', 1)[0]
  			val = var_final.split(' ', 1)[1]
  			val_final = val.split(' ', 2)
  			if opration == 'sum':
  				if isint(val_final[0]) == True or isf(val_final[0]) == True:
  					if isint(val_final[2]) == True or isf(val_final[2]) == True:
  						result = int(val_final[0]) + int(val_final[2])
  						VARS[name_var] = result
  					else:
  						print(f"ValueError: '{val_final[2]}' is not number")
  						break
  				else:
  					print(f"ValueError: '{val_final[0]}' is not number")
  					break
  			elif opration == 'min':
  				if isint(val_final[0]) == True or isf(val_final[0]) == True:
  					if isint(val_final[2]) == True or isf(val_final[2]) == True:
  						result = int(val_final[0]) - int(val_final[2])
  						VARS[name_var] = result
  					else:
  						print(f"ValueError: '{val_final[2]}' is not number")
  						break
  				else:
  					print(f"ValueError: '{val_final[0]}' is not number")
  					break
  			elif opration == 'mul':
  				if isint(val_final[0]) == True or isf(val_final[0]) == True:
  					if isint(val_final[2]) == True or isf(val_final[2]) == True:
  						result = int(val_final[0]) * int(val_final[2])
  						VARS[name_var] = result
  					else:
  						print(f"ValueError: '{val_final[2]}' is not number")
  						break
  				else:
  					print(f"ValueError: '{val_final[0]}' is not number")
  					break
  			elif opration == 'div':
  				if isint(val_final[0]) == True or isf(val_final[0]) == True:
  					if isint(val_final[2]) == True or isf(val_final[2]) == True:
  						result = int(val_final[0]) / int(val_final[2])
  						VARS[name_var] = result
  					else:
  						print(f"ValueError: '{val_final[2]}' is not number")
  						break
  				else:
  					print(f"ValueError: '{val_final[0]}' is not number")
  					break
  			elif opration == 'read':
  				
  				val_read = input()
  				VARS[name_var] = val_read
  		#VARS[name_var] = var_final
  		
  elif fn == ' ':
  	pass
  	
  elif fn == "\n":
  	pass
  	
  elif fn == "#":
  	pass
  	
  elif fn == 'import':
  	val = s.split(' ', 1)[1]
  	if val[-1] == '\n':
  		val = val[:-1]
  	if val == 'math':
  		LIBS[val] = 1
  	elif val == 'sqlite3':
  		LIBS[val] = 1
  	elif val == 'discord':
  		LIBS[val] = 1
  	elif val == 'http':
  		LIBS[val] = 1
  	else:
  		print(f'ModuleNotFoundError: Module {val} is not found')
  		break
  
  elif fn == 'if':
  	val = s.split(' ', 1)[1]
  	number = val.split(' ', 2)[0]
  	operator = val.split(' ', 2)[1]
  	number1 = val.split(' ', 2)[2]
  	if number in VARS:
  		number_final = VARS[number]
  		if operator == '==':
  			if int(number_final) == int(number1[:-2]):
  				if_if = True
  			else:
  				if_if = False
  		elif operator == '!=':
  			if int(number_final) != int(number1[:-2]):
  				if_if = True
  			else:
  				if_if = False
  		elif operator == '>':
  			if int(number_final) > int(number1[:-2]):
  				if_if = True
  			else:
  				if_if = False
  		elif operator =='<':
  			if int(number_final) < int(number1[:-2]):
  				if_if = True
  			else:
  				if_if = False
  		elif operator == '<=':
  			if int(number_final) <= int(number1[:-2]):
  				if_if = True
  			else:
  				if_if = False
  		elif operator == '>=':
  			if int(number_final) >= int(number1[:-2]):
  				if_if = True
  			else:
  				if_if = False
  		else:
  			print(f'SyntaxError:{operator} is not defined')
  			
  		
  		
  elif fn == '\tprint':
  	val = s.split(' ',1)[1]
  	if if_if == True:
  		if val[0] == '"' or val[0] == "'":
  			if val[-1] == '\n':
  				val = val[:-1]
  				print(val[1:-1])
  			else:
  				print(val[1:-1])
  		else:
  			if val[-1]== '\n':
  				val = val[:-1]
  			if val in VARS:
  				test_var = VARS[val]
  				print(test_var)
  			else:
  				if islibs(val) == True:
  					name_libs = val.split('.', 1)[0]
  					func = val.split('.', 1)[1]
  					if name_libs in LIBS:
  						if name_libs == 'math':
  							if issplit(func) == True:
  								func_final = func.split(' ', 1)[0]
  								args = func.split(' ', 1)[1]
  								result = check_func_math(func_final, name_libs, args)
  								print(result)
  							else:
  								result = check_func_math(func, name_libs)
  								print(result)
  					else:
  						print(f'NameError: {name_libs} is not undefined')
  						break
  				else:
  					print(val)
   
   
  elif fn.split('.', 1)[0] in LIBS:
  	func = fn.split('.', 1)[1]
  	if fn.split('.', 1)[0] == 'math':
  		if issplit(s) == True:
  			args = s.split(' ', 1)[1]
  			result = check_func_math(func, name_libs, args)
  		else:
  			result = check_func_math(func, fn.split('.',1)[0])
  	elif fn.split('.', 1)[0] == 'sqlite3':
  		if issplit(s) == True:
  			args = s.split(' ', 1)[1]
  			result = check_func_sqlite3(func, args)
  		else:
  			result = check_func_sqlite3(func)
  	elif fn.split('.', 1)[0] == 'discord':
  		if issplit(s) == True:
  			args = s.split(' ', 1)[1]
  			result = check_func_discord(func, args)
  		else:
  			result = check_func_discord(func)
  	
  	elif fn.split('.', 1)[0] == 'http':
  		if issplit(s) == True:
  			args = s.split(' ', 1)[1]
  			result = check_func_http(func, args)
  		else:
  			result = check_func_http(func)
  			
  	
  elif fn == '\tvar':
  	name_var = s.split(' ', 2)[1]
  	var = s.split(' ', 2)[2]
  	var_final = var.split(' ', 1)[1]
  	if var_final[0] == '"' or var_final[0] == "'":
  		VARS[name_var] = var_final[1:-1]
  	else:
  		if issplit(var_final) == True:
  			opration = var_final.split(' ', 1)[0]
  			val = var_final.split(' ', 1)[1]
  			val_final = val.split(' ', 2)
  			if opration == 'sum':
  				if isint(val_final[0]) == True or isf(val_final[0]) == True:
  					if isint(val_final[2]) == True or isf(val_final[2]) == True:
  						result = int(val_final[0]) + int(val_final[2])
  						VARS[name_var] = result
  					else:
  						print(f"ValueError: '{val_final[2]}' is not number")
  						break
  				else:
  					print(f"ValueError: '{val_final[0]}' is not number")
  					break
  			elif opration == 'min':
  				if isint(val_final[0]) == True or isf(val_final[0]) == True:
  					if isint(val_final[2]) == True or isf(val_final[2]) == True:
  						result = int(val_final[0]) - int(val_final[2])
  						VARS[name_var] = result
  					else:
  						print(f"ValueError: '{val_final[2]}' is not number")
  						break
  				else:
  					print(f"ValueError: '{val_final[0]}' is not number")
  					break
  			elif opration == 'mul':
  				if isint(val_final[0]) == True or isf(val_final[0]) == True:
  					if isint(val_final[2]) == True or isf(val_final[2]) == True:
  						result = int(val_final[0]) * int(val_final[2])
  						VARS[name_var] = result
  					else:
  						print(f"ValueError: '{val_final[2]}' is not number")
  						break
  				else:
  					print(f"ValueError: '{val_final[0]}' is not number")
  					break
  			elif opration == 'div':
  				if isint(val_final[0]) == True or isf(val_final[0]) == True:
  					if isint(val_final[2]) == True or isf(val_final[2]) == True:
  						result = int(val_final[0]) / int(val_final[2])
  						VARS[name_var] = result
  					else:
  						print(f"ValueError: '{val_final[2]}' is not number")
  						break
  				else:
  					print(f"ValueError: '{val_final[0]}' is not number")
  					break
  			elif opration == 'input':
  				
  				val_read = input()
  				VARS[name_var] = val_read
  		#VARS[name_var] = var_final
  
 
  else:
  	print(f"NameError: name {fn} is not defined")
  	break