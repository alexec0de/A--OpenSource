"""
A# - sqlite3 libs

"""


import sqlite3

connection = sqlite3.connect('test.db')
cursor = connection.cursor()

def check_func_sqlite3(func, args = None):
	
	if func == 'connect':
		pass
	elif func == 'execute':
		cursor.execute(str(args))
		connection.commit()
	else:
		print(f'NameError: {func} is not defined')
		
	
	