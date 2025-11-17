
n=8
if n==1:
    print(1)
one=1
two=1
total=0
for i in range(2,n+1):
    total=one+two
    two=one
    one=total
print(total)








# def fib(n):  
#     if n <= 1:  
#         return n  
#     else:  
#         return fib(n-1) + fib(n-2)  
# print(fib(5))
# print(fib(1))
# print(fib(10))

