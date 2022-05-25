# Function to print given string 'x' times
def print_fun(string, x):
    # Your code here
    print(string * x)
        

#{ 
#Driver Code Starts.

# Driver Code
def main():
    testcases = int(input("enter number of testcases: "))
    
    # Loop for testcases
    while(testcases > 0):
        string = input("Enter a string: ")
        x = int(input("Enter a number: "))
        print_fun(string, x)
        testcases -= 1

if __name__ == '__main__':
    main()
    
#} Driver Code Ends