import math
class Solution:
    def find_divisor(n1):
        #the tc is O(sqrt(n)) and sc is O(2*sqrt(n))
        # because we are holding 2 numbers for each itteration till sqrt of the number 
        divisors=set()
        val=int(math.sqrt(n1))
        #now we loop from one to val which is the sqr roor because after sqrt the values start to repeat
#1*36 and 36*1, the values that are seen for the first time are observed to exsist till the sqrt of a problem
        for elems in range(1,val+1):
            #now we have to find both parts of divisors 4*9 > we find 4 and 9 heree
            #to get the first part we check if the elem divides n1
            if n1%elems==0:
                divisors.add(elems) #elems*x=36
            #now we find the x from the above statement
                if elems!=n1//elems:
                    divisors.add(n1//elems) #this gives me second value that is to be multiplied to elems
        return divisors
          
                
            
sol=Solution
print(sol.find_divisor(36))
print(sol.find_divisor(12))