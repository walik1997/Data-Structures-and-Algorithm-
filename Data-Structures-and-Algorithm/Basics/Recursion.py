class Solution:
    def recur(self,n1):
        #TC O(N) SC(N) Recursion stack
        if n1==95:
            return n1
        return self.recur(n1+1)
    def printname(self,n2,target):
        if n2==target:
            return
        print("Wali")
        self.printname(n2+1,target)
    def printname(self,n2,target):
        #Once the return statement is hit the stack startsto unwind and it starts unwinding 
        # from the next line where this was called from 
        if n2==target:
            return
        self.printname(n2+1,target)    
        print("Wali")
    def sumrecur(self,n1,target,sum):
        #sum of the numbers till a target
        if n1>target:
            return sum
        sum+=n1
        return self.sumrecur(n1+1,target,sum)
    def factorial(self,n,prod):
        if n==1:
            return prod
        prod=prod*n
        return self.factorial(n-1,prod)
        
        
        
sol=Solution()
print(sol.recur(0))
print(sol.printname(0,5))
print(sol.printname(0,5))
print(sol.sumrecur(1,21,0))
print(sol.factorial(12,1))