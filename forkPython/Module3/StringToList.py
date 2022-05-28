def Convert1(string):
    li = list(string.split(' '))
    return li
def Convert2(string):
    li = list(string.split('-'))
    return li

str1 = "Geeks For Geeks"
str2 = "Geeks-For-Geeks"
print(Convert1(str1))
print(Convert2(str2))

# Python code to convert string to list character-wise
def Convert3(string):
    list1=[]
    list1[:0]=string
    return list1
# Driver code
str1="ABCD"
print(Convert3(str1))