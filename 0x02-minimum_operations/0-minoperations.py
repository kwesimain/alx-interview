#!/usr/bin/python3

"""Minimum Operations are those activities necessary for the 
business or operation to maintain the condition of facilitiy.
"""

def minOperations(n):
	"""Returns the fewest number of operations needed 
	to result in exactly n H characters in the file.
	"""
	if not isinstance(n, int) or n < 2:
        	return 0
	operation = 0
	min_factor = 2
	while n > 1:
        	while n % min_factor == 0:
            		operation += min_factor
            		n //= min_factor
        	min_factor += 1 
    
	return operation
