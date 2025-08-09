class Solution:
    #Brute force- Taking the smallest number and from there checking in reverse till 0 in the worsy case it would be O(N) Space would 
    def gcd(n1,n2):
        if n1==0:
            return b
        elif n2==0:
            return a 
        if n1>n2:
            a=n2
            b=n1
        else:
            a=n1
            b=n2
        if b%a==0:
            return a
        num=a-1
        while a!=0:
            if a%num==0:
                if b%num==0:
                    return num
            num=num-1
    #This is a Euclidean algorithm where we try to check a number  is divisible by another and we keep
#shifting n1 to n2 and n2 to n1.if a 3%9,  modulo returns 3 when the operation is not possible 
#time complexity - O(log(min(n1,n2))) 
    def gcd1(n1,n2):
        while n2!=0:
            n1,n2=n2,n1%n2
        return n1
print(Solution.gcd(27,36))
print(Solution.gcd1(27,36))