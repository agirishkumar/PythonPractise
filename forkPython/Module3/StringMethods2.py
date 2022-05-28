'''
1. len() :- This function returns the length of the string.
2. count("string", beg, end) :- This function counts the occurrence of mentioned substring in whole string. This function takes 3 arguments, substring, beginning position( by default 0) and end position(by default string length).
3. center() :- This function is used to surround the string with a character repeated both sides of string multiple times. By default the character is a space. Takes 2 arguments, length of string and the character.
4. ljust() :- This function returns the original string shifted to left that has a character at its right. It left adjusts the string. By default the character is space. It also takes two arguments, length of string and the character.
5. rjust() :- This function returns the original string shifted to right that has a character at its left. It right adjusts the string. By default the character is space. It also takes two arguments, length of string and the character.
6. isalpha() :- This function returns true when all the characters in the string are alphabets else returns false.

7. isalnum() :- This function returns true when all the characters in the string are combination of numbers and/or alphabets else returns false.

8. isspace() :- This function returns true when all the characters in the string are spaces else returns false.
9. join() :- This function is used to join a sequence of strings mentioned in its arguments with the string.

'''

# len() and count()
str = "geeksforgeeks is for geeks"
 
# Printing length of string using len()
print (" The length of string is : ", len(str));

# Printing occurrence of "geeks" in string
# Prints 2 as it only checks till 15th element
print (" Number of appearance of ""geeks"" is : ",end="")
print (str.count("geeks",0,15))

# center(), ljust() and rjust()
str = "geeksforgeeks"
 
# Printing the string after centering with '-'
print ("The string after centering with '-' is : ",end="")
print ( str.center(20,'-'))

# Printing the string after ljust()
print ("The string after ljust is : ",end="")
print ( str.ljust(20,'-'))

# Printing the string after rjust()
print ("The string after rjust is : ",end="")
print ( str.rjust(20,'-'))

# isalpha(), isalnum(), isspace()
str = "geeksforgeeks"
str1 = "123"
 
# Checking if str has all alphabets 
if (str.isalpha()):
       print ("All characters are alphabets in str")
else : print ("All characters are not alphabets in str")

# Checking if str1 has all numbers
if (str1.isalnum()):
       print ("All characters are numbers in str1")
else : print ("All characters are not numbers in str1")

# Checking if str1 has all spaces
if (str1.isspace()):
       print ("All characters are spaces in str1")
else : print ("All characters are not spaces in str1")

# join()
str = "_"
str1 = ( "geeks", "for", "geeks" )

# using join() to join sequence str1 with str
print ("The string after joining is : ", end="")
print ( str.join(str1))