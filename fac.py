'''
import math
print("the factorial of 22 is:", end=" ")
print(math.factorial(22))

'''
'''
import math
s=input("enter a number:")
print(math.factorial(int(s)))
'''
'''
import math
def fact(n):
    if n<0:
        return None
    ans = 1
    while n!=0:
        ans = ans*n
        n = n-1
    return(ans)
num=int(input("enter a no:"))
f=fact(num)
print("factorial of",num,"is",f)
'''
import math
absolute=-5.999
floor_test=198.42
result1=math.fabs(absolute)
result2=math.floor(floor_test)
print(result1,"is the absolute value of: ",absolute)
print(result2,"is the flow value of: ",floor_test)








