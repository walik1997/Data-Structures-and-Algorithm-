class Solution:
    def armstrong(n):
        count=n
        counter=0
        while count!=0:
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
        
        