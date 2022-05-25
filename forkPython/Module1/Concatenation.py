# Function to concatenate given two strings and print
def print_fun(string1, string2):
    print (string1 + string2)

#{ 
#Driver Code Starts.

# Python Code to concatenate given strings
def main():
    testcases = int(input("enter no of testcases: "))
    
    while(testcases > 0):
        string1 = input("enter a string1: ")
        string2 = input("enter a string2: ")
        print_fun(string1, string2)
        
        testcases -= 1

if __name__ == '__main__':
    main()
    

#} Driver Code Ends