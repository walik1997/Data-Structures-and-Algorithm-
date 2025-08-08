#Reverse a number
#space complexity O(N)
#Time Complexity O(N)
class Solution:
    def reverseNumber(n):
        new=""
        while n!=0:
            y=str(n%10)
            n=n//10
            new+=y
        return int(new)    

#Better approach
#Intution - We keep peeling each number from the back and move its place like units to tens and then add the other number 
#41> 41*10> 410+2>412
#Time Complexity - O(N)
#Space Complexity - O(1)
    def reverseNumber1(n):
        rev=0
        while n!=0:
            y=n%10
            rev=rev*10
            n=n//10
        return rev
X=Solution.reverseNumber(9214)
print(X)
Y=Solution.reverseNumber(9214)
print(Y)