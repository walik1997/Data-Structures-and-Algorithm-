import math
#Brute Force - checking grom n to 1 to see if any other no satisfies the condition 
# making it non prime
class Solution:
    def prime(self,n1):
        #TC - O(sqrt(n)), SC - O(1)
        if n1 <= 1:
            return False
        for i in range(2,math.ceil(math.sqrt(n1)+1)):
            if n1%i==0: 
                if i!=n1:
                    return False
        return True
sol=Solution()
print(sol.prime(4))
                 