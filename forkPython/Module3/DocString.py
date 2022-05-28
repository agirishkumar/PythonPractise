def my_function():
	'''Demonstrates triple double quotes
	docstrings and does nothing really.'''

	return None

print("Using __doc__:")
print(my_function.__doc__)

print("Using help:")
help(my_function)


def power(a, b):
    """Returns arg1 raised to power arg2."""
   
    return a**b
  
print(power.__doc__)

def my_function2(arg1):
    """
    Summary line.
  
    Extended description of function.
  
    Parameters:
    arg1 (int): Description of arg1
  
    Returns:
    int: Description of return value
  
    """
  
    return arg1
  
print(my_function2.__doc__)