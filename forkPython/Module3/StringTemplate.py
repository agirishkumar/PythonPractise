
# A Simple Python template example

from re import T
from string import Template
# Create a template that has placeholder for value of x
t= Template('x is $x')
# Substitute value of x in above template
print (t.substitute({'x' : 1}))

Student = [('a',90),('b',80),('c',78)]
K = Template('Hi $name, you have got $marks marks')
for i in Student:
    print (K.substitute(name=i[0],marks=i[1]))


#Safe_substitute
template = Template('$name is the $job of $company')
 
string = template.safe_substitute(name='Raju Kumar',
                      job='TCE')
print(string)
#we have not provided the “$company” placeholder any data, but it won’t throw an error, rather will return the placeholder as a string as discussed above

#printing template string
t=Template('I am $name from $city')
print('Template String =',t.template)

#Escaping $ Sign
template = Template('$$ is the symbol for $name')
string = template.substitute(name='Dollar')
print(string)

#The ${Identifier}
template = Template( 'That $noun looks ${noun}y')
string = template.substitute(noun='Fish')
print(string)
