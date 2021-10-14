#!/usr/bin/env python3

from integer import Integer
from time import perf_counter as pc

def fib_py(n):
	if n <= 1:
		return n
	else:
		return(fib_py(n-1) + fib_py(n-2))def fib_py(n):
	if n <= 1:
		return n
	else:
		return(fib_py(n-1) + fib_py(n-2))




def main():
	f = Integer(5)
	print(f.get())
	f.set(7)
	print(f.get())
        start = pc()
	print(fib_py(7))
	stop = pc()
	print(fib_py(f'{stop-start}'))




if __name__ == '__main__':
	main()

