#!/usr/bin/env python
import random
import time

from multiprocessing import Pool

def random_wait((n,)):
	sec = random.randint(5, 20)
	print "Process {} will wait for {} seconds".format(str(n), str(sec))
	time.sleep(sec)
	print "Process {} done waiting".format(str(n))


if __name__=="__main__":
	p = Pool(processes=10)

	res = p.map_async(random_wait, ((i,) for i in range(10)))
	p.close()
	p.join()
