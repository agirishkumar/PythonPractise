# Python program to demonstrate the use of formatting using % 
  
# Initialize variable as a string 
variable = '15'
string = "Variable as string = %s" %(variable) 
print (string )
  
# Printing as raw data 

print ("Variable as raw data = %r" %(variable))
  
# Convert the variable to integer 
# And perform check other formatting options 
  
variable = int(variable) # Without this the below statement 
                        # will give error. 
string = "Variable as integer = %d" %(variable) 
print (string) 
print ("Variable as float = %f" %(variable)) 
  
# printing as any string or char after a mark 

print ("Variable as printing with special char = %cAsuran" %(variable)) 
  
print ("Variable as hexadecimal = %x" %(variable))
print ("Variable as octal = %o" %(variable)) 