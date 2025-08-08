#Brute Force- The Tc and Sc is O(N) 
class Solution:
    def palindrome(n):
        n=str(n) #creating a copy O(N)
        rev=n[::-1] #reversing the copy
        if rev ==n:
            return True
        else:
            return False
#Better- TC - O(N) and SC - O(1)
    def palindrome1(n):
        if n<0: #edge case when te number is less than 0 it cannot be checked for being a palindrome
            return False
        org=n
        check=0
        while n!=0:
            y=n%10
            check=check*10+y
            n=n//10
        return check==org

print(Solution.palindrome(1234567))
print(Solution.palindrome(121))
print(Solution.palindrome1(1234567))
print(Solution.palindrome1(121))
