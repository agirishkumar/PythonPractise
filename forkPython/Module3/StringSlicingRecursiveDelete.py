''' 
Given a string “str” and another string “sub_str”. We are allowed to delete “sub_str” from “str” any number of times. It is also given that the “sub_str” appears only once at a time. The task is to find if “str” can become empty by removing “sub_str” again and again.
'''

def checkEmpty(input1, pattern):
		
	# If both are empty
	if len(input1)== 0 and len(pattern)== 0:
		return 'true'
	
	# If only pattern is empty
	if len(pattern)== 0:
		return 'true'
	
	while (len(input1) != 0):

		# find sub-string in main string
		index = input1.find(pattern)

		# check if sub-string founded or not
		if (index ==(-1)):
		    return 'false'

		# slice input string in two parts and concatenate
		input1 = input1[0:index] + input1[index + len(pattern):]			

	return 'true'
	
# Driver program
if __name__ == "__main__":
	input1 ='GEEGEEKSKS'
	pattern ='GEEKS'
	print (checkEmpty(input1, pattern))
