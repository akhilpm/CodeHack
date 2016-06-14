#plain fibonacci number code
import time

def fib(n):
	if n<=2:
		return 1

	else:
		return fib(n-1) + fib(n-2)


start = time.time()
print fib(30)
print('Execution Time : %f Seconds\n' %(time.time()-start))
