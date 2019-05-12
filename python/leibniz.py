# coding: utf-8

import time
import numba

@numba.jit(nopython = True, parallel = True)
def leibniz(n):
	sum = 0

	for i in range(0, n + 1, 2):
		sum += 1 / (2 * i + 1)

	for i in range(1, n + 1, 2):
		sum += -1 / (2 * i + 1)

	return sum

print(4 * leibniz(10))

start = time.time()
print(4 * leibniz(10 ** 8))
print('time: {}s'.format(time.time() - start))
