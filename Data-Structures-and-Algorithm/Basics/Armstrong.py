class Solution:
    def armstrong(n):
#Tc = log(N) because we are reducing the number and it takes the number of digits as itteration
#SC-O(1)
        count=n
        counter=0
        while count!=0:
        #this can also be converted into a string to get the len 
            counter+=1
            count=count//10
        ans=0  
        while n!=0:
            y=n%10
            ans+=pow(y,counter)
            n=n//10
        return ans
sol=Solution
print(sol.armstrong(13))     

"""
If n = 1,000,000 (one million):

You don’t do a million iterations.

You only do 7 iterations (because it has 7 digits).

That’s why the growth is much slower than O(n).
"""