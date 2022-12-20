#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
	counter = 0
   
	for element in my_list:
		try:
          		if counter < x:
				print(f"{element}", end='')
				counter += 1
		except IndexError:
		break
	print()
	return counter



