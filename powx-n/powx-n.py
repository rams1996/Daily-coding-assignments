class Solution:
    def myPow(self, x: float, n: int) -> float:
        flag=False
        if n<0:
            flag=True
            n=n*-1
        if n==0:
            return 1
        
        
        def recursion(x,n):
            # print(n)
            if n==1:
                return x
            a=recursion(x,n//2)
            if n%2==0:
                return a*a
            else:
                return a*a*x
        if not flag:
            return recursion(x,n)
        else:
            return 1*(1/(recursion(x,n)))
        
