''' 
1. strip():- This method is used to delete all the leading and trailing characters mentioned in its argument.
2. lstrip():- This method is used to delete all the leading characters mentioned in its argument.
3. rstrip():- This method is used to delete all the trailing characters mentioned in its argument.
4. min("string"):- This function returns the minimum value alphabet from the string.
5. max("string") :- This function returns the maximum value alphabet from string.
6. maketrans():- It is used to map the contents of string 1 with string 2 with respective indices to be translated later using translate(). 
7. translate():- This is used to swap the string elements mapped with the help of maketrans().
8.replace():- This function is used to replace the substring with a new substring in the string. This function has 3 arguments. The string to replace, new string which would replace and max value denoting the limit to replace action ( by default unlimited ). 

'''

# strip(), lstrip() and rstrip()
str = "---geeksforgeeks---"

# using strip() to delete all '-'
print ( " String after stripping all '-' is : ", end="")
print ( str.strip('-') )

# using lstrip() to delete all trailing '-'
print ( " String after stripping all leading '-' is : ", end="")
print ( str.lstrip('-') )

# using rstrip() to delete all leading '-'
print ( " String after stripping all trailing '-' is : ", end="")
print ( str.rstrip('-') )

# min() and max()
str = "geeksforgeeks"

# using min() to print the smallest character
# prints 'e'
print ("The minimum value character is : " + min(str))

# using max() to print the largest character
# prints 's'
print ("The maximum value character is : " + max(str))

# maketrans() and translate()
# for maketrans()

str = "geeksforgeeks"

str1 = "gfo"
str2 = "abc"

# using maketrans() to map elements of str2 with str1
mapped = str.maketrans( str1, str2 )

# using translate() to translate using the mapping
print ("The string after translation using mapped elements is : ")
print  (str.translate(mapped)) 

# replace()

str = "nerdsfornerds is for nerds"

str1 = "nerds"
str2 = "geeks"

# using replace() to replace str2 with str1 in str
# only changes 2 occurrences 
print ("The string after replacing strings is : ", end="")
print (str.replace( str1, str2, 2)) 