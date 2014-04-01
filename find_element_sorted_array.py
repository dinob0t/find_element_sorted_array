"""
Algorithms to find element and return list index in a sorted array
"""
import time

array_size = 100
sorted_dict = {x: x for x in range(array_size)}
sorted_list = range(array_size)

def find_ewise_list(l, element):
	for i in range(len(l)):
		if l[i] == element:
			return i





element = 10
t0 = time.time()
print "Index of element by element wise list search  = %d" %find_ewise_list(sorted_list,element)
t1 = time.time()
print "Time taken %f s" %(t1-t0)	




