#!/usr/bin/env python3

from integer import Integer
from time import perf_counter as pc
import numpy as np
import matplotlib.pyplot as plt

def fib_py(n):
	if n <= 1:
		return n
	else:
		return(fib_py(n-1) + fib_py(n-2))


def main():
	f = Integer(5)
	print(f.get())
	f.set(47)
	print(f.get())


	array = np.arange(25,40)
	time_py = []
	time_cpp = []

	for i in array:
		start1 = pc()
		fib_py(i)
		stop1 = pc()
		time_py.append(stop1-start1)

	for j in array:
		start2 = pc()
		g = Integer(j)
		g.fibcpp()
		stop2 = pc()
		time_cpp.append(stop2-start2)

	plt.plot(array, time_py, 'r-', array, time_cpp, 'b-')
	plt.savefig('Comparing fib 25 to 40 calculated with python and c++')
	plt.show()

	startpy = pc()
	resultpy = fib_py(47)
	print(resultpy)
	stoppy = pc()

	print(f"Calculating fib with python took {round(stoppy-startpy, 5)} seconds")#Took approx 30 min

	startcpp = pc()
	resultcpp = f.fibcpp()
	print(resultcpp)
	stopcpp = pc()

	print(f"Calculating fib with C++ took {round(stopcpp-startcpp, 5)} seconds")#Took approx 1 minute

if __name__ == '__main__':
	main()

