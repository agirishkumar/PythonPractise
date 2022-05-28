'''
find("string", beg, end) :- This function is used to find the position of the substring within a string.It takes 3 arguments, substring , starting index( by default 0) and ending index( by default string length). 
 


It returns "-1 " if string is not found in given range.
It returns first occurrence of string if found.


2. rfind("string", beg, end) :- This function has the similar working as find(), but it returns the position of the last occurrence of string.

3. startswith("string", beg, end) :- The purpose of this function is to return true if the function begins with mentioned string(prefix) else return false.
4. endswith("string", beg, end) :- The purpose of this function is to return true if the function ends with mentioned string(suffix) else return false.
5. islower("string") :- This function returns true if all the letters in the string are lower cased, otherwise false.
6. isupper("string") :- This function returns true if all the letters in the string are upper cased, otherwise false.

7. lower() :- This function returns the new string with all the letters converted into its lower case.
8. upper() :- This function returns the new string with all the letters converted into its upper case.
9. swapcase() :- This function is used to swap the cases of string i.e upper case is converted to lower case and vice versa.
10. title() :- This function converts the string to its title case i.e the first letter of every word of string is upper cased and else all are lower cased.


'''

# find() and rfind()
str = "geeksforgeeks is for geeks"
str2 = "geeks"

# using find() to find first occurrence of str2
# returns 8
print ("The first occurrence of str2 is at : ", end="")
print (str.find( str2, 4) )

# using rfind() to find last occurrence of str2
# returns 21
print ("The last occurrence of str2 is at : ", end="")
print ( str.rfind( str2, 4) )

# startswith() and endswith() 
str = "geeks"
str1 = "geeksforgeeksportal"

# using startswith() to find if str 
# starts with str1 
if str1.startswith(str): 
        print ("str1 begins with : " + str) 
else : print ("str1 does not begin with : "+ str) 

# using endswith() to find 
# if str ends with str1 
if str1.endswith(str): 
    print ("str1 ends with : " + str) 
else : 
    print ("str1 does not end with : " + str) 


# isupper() and islower()
str = "GeeksforGeeks"
str1 = "geeks"

# checking if all characters in str are upper cased
if str.isupper() :
    print ("All characters in str are upper cased")
else : 
    print ("All characters in str are not upper cased")

# checking if all characters in str1 are lower cased
if str1.islower() :
    print ("All characters in str1 are lower cased")
else : 
    print ("All characters in str1 are not lower cased")

# upper(), lower(), swapcase() and title()
str = "GeeksForGeeks is fOr GeeKs"

# Converting string into its lower case
str1 = str.lower();
print (" The lower case converted string is : " + str1)

# Converting string into its upper case
str2 = str.upper();
print (" The upper case converted string is : " + str2)

# Converting string into its swapped case
str3 = str.swapcase();
print (" The swap case converted string is : " + str3)

# Converting string into its title case
str4 = str.title();
print (" The title case converted string is : " + str4)