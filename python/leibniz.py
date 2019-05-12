# coding: utf-8

import time
import numba
import sys

times = 5

@numba.jit(nopython = True, parallel = True, fastmath = True)
def leibniz(n):
	sum = 0

	for i in range(0, n + 1, 2):
		sum += 1 / (2 * i + 1)

	for i in range(1, n + 1, 2):
		sum += -1 / (2 * i + 1)

	return sum


if __name__ == '__main__':
	if len(sys.argv) < 2:
		print('Usage: {} NUMBER_OF_DIGITS'.format(sys.argv[0]))
		sys.exit(-1)
	
	# JIT compile
	leibniz(10)

	# Do calculate
	start = time.time()
	for i in range(times):
		print(4 * leibniz(10 ** int(sys.argv[1])))
	print('calc time: {}s'.format((time.time() - start) / times))
