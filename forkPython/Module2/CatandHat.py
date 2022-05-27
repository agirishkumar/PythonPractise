def cat_hat(str):
  ##your code here##
  ##You need to write complete code this time 
  return str.count('cat')==str.count("hat")


#{ 
#Driver Code Starts.




def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        str = input()
        print(cat_hat(str))
        testcases-=1
        


if __name__=='__main__':
    main()
#} Driver Code Ends