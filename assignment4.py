dp=[-1]*100
def fib_Memoization(n):
    if (n<=1):
        return n
    if dp[n]!=-1:
        return dp[n]
    dp[n]=fib_Memoization(n-1) + fib_Memoization(n-2)
    return dp[n]

def fib_Tabulation(n):
    dp=[0]*(n+1)
    dp[0]=0
    dp[1]=1
    for i in range(2,n+1):
        dp[i]=dp[i-1]+dp[i-2]
    return dp[n]
a=int(input("enter the number to find the nth fabonachi : "))
print(f"fabonachi using tabulation : {fib_Tabulation(a)}")
print(f"fabonachi using memoization : {fib_Memoization(a)}")