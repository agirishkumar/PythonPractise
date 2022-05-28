''' 
Given a string, write a python function to check if it is palindrome or not. A string is said to be palindrome if the reverse of the string is the same as string. For example, “radar” is a palindrome, but “radix” is not a palindrome
'''

#Method1

def isPalindrome(s):
    return s == s[::-1]

s = "malayalam"
ans = isPalindrome(s)
if ans:
    print("Yes ",s," is palindrome")
else:
    print("No",s," is not a palindrome")


#Method2

# function to check string is palindrome or not
def isPalindrome1(str):

	# Run loop from 0 to len/2
	for i in range(0, int(len(str)/2)):
		if str[i] != str[len(str)-i-1]:
			return False
	return True

s = "malayalam"
ans1 = isPalindrome1(s)

if (ans1):
	print("Yes")
else:
	print("No")

#Method3

# function to check string is
# palindrome or not
def isPalindrome2(s):

	# Using predefined function to
	# reverse to string print(s)
	rev = ''.join(reversed(s))

	# Checking if both string are
	# equal or not
	if (s == rev):
		return True
	return False


s = "malayalam"
ans2 = isPalindrome2(s)

if (ans2):
	print("Yes")
else:
	print("No")


#Method4
# Python program to check
# if a string is palindrome
# or not

x = "malayalam"

w = ""
for i in x:
	w = i + w

if (x == w):
	print("Yes")
else:
	print("No")


#Method5

# Python program to check
# if a string is palindrome
# or not
st = 'malayalam'
j = -1
flag = 0
for i in st:
	if i != st[j]:
		flag = 1
		break
	j = j - 1
if flag == 1:
	print("NO")
else:
	print("Yes")


#Method6

# Recursive function to check if a
# string is palindrome
def isPalindrome3(s):

	# to change it the string is similar case
	s = s.lower()
	# length of s
	l = len(s)

	# if length is less than 2
	if l < 2:
		return True

	# If s[0] and s[l-1] are equal
	elif s[0] == s[l - 1]:

		# Call is palindrome form substring(1,l-1)
		return isPalindrome3(s[1: l - 1])

	else:
		return False

# Driver Code
s = "MalaYaLam"
ans4 = isPalindrome3(s)

if ans4:
	print("Yes")

else:
	print("No")

