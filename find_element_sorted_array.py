"""
Algorithms to find element and return list index in a sorted array
"""
import time
import math

array_size = 10000
sorted_dict = {x: x for x in range(array_size)}
sorted_list = range(array_size)

def find_ewise_list(l, element):
	for i in range(len(l)):
		if l[i] == element:
			return i

def binary_search(l, element, index):
	mid = int(math.floor(len(l)/2))

	if l[mid] == element:
		return mid + index
	if len(l) == 1:
		return None
	if element > l[mid]:
		return binary_search(l[mid:len(l)], element, index + mid)
	else:
		return binary_search(l[0:mid],element, index)



element = 1000

t0 = time.time()
print "Index of element by element wise list search  = %d" %find_ewise_list(sorted_list,element)
t1 = time.time()
print "Time taken %f s" %(t1-t0)	

t0 = time.time()
print "Index of element by element wise list search  = %d" %binary_search(sorted_list,element, 0)
t1 = time.time()
print "Time taken %f s" %(t1-t0)



