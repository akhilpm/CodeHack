#fibonacci no finding using decorators
import time

def memoize(f):
	cache = {}
	
	def memoizedFunction(*args):
		if args not in cache:
			cache[args] = f(*args)

		return cache[args]

	memoizedFunction.cache = cache
	return memoizedFunction


@memoize
def fib(n):
	if n<=2:
		return 1

	else:
		return fib(n-1) + fib(n-2)


start = time.time()
print fib(30)
print('Execution Time : %f Seconds\n' %(time.time()-start))
#print memoize.memoizedFunction.cache
