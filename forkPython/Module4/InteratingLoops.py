# Function to print list 
# print elements in required fashion
def print_elements(N, arr):
    
    for x in range(N//2):
       print(arr[x],end=" ")
    for i in range(N//2,N,3):
       print(arr[i],end=" ")


    
    # Your code here 
    # use '//' to divide to get int for index

#{ 
#Driver Code Starts.
# Driver Code
def main():
    
    # Testcase input
    testcases = int(input())
    
    # Looping through testcases
    while(testcases > 0):
        # size of array
        N = int(input())
        
        # array elements input
        array = input().split()
        # print (array)
        arr = list()
        for i in array:
            arr.append(int(i))
            
        # print (arr)
        
        # calling function to print elements
        print_elements(N, arr)
        print ()
        testcases -= 1
 
if __name__ == '__main__':
    main()
#} Driver Code Ends