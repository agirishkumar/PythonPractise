def friends_in_trouble(j_angry, s_angry):
    if j_angry ^ s_angry:
        return False
    else:
        return True
    

#{ 
#Driver Code Starts.

# Driver code    
def main():
    testcase = int(input())
    
    # loop for testcases
    while(testcase > 0):
        string = input().split()
        j_angry = string[0]
        s_angry = string[1]
        if(j_angry == 'True'):
            j_angry = True
        else:
            j_angry = False
        
        if(s_angry == 'True'):
            s_angry = True
        else:
            s_angry = False
            
        print(friends_in_trouble(j_angry, s_angry))
        
        testcase -= 1
    
if __name__ == '__main__':
    main()
#} Driver Code Ends