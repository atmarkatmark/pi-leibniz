# coding: utf-8

import numba
import time
from multiprocessing import Process, Queue
from decimal import Decimal, getcontext

n = 10 ** 7
getcontext().prec = 32

@numba.autojit
def leibniz_child(n, begin, step, queue):
	sum = Decimal(0)
	sign = Decimal(-1 if begin % 2 else 1)
	
	for i in range(begin, n, step):
		sum += sign / (2 * i + 1)
	
	queue.put(sum)

def leibniz_pi(n, core = 2):
	q = Queue()
	for i in range(core):
		p = Process(target = leibniz_child, args= (n, i, core, q))
		p.start()
	
	sum = Decimal(0)
	for i in range(core):
		sum += q.get()
	
	return 4 * sum

if __name__ == '__main__':
	start = time.time()
	print(leibniz_pi(n, 4))
	print('time: {}s'.format(time.time() - start))
