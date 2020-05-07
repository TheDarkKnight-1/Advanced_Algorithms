dict={}
def fib(n):
    if n<=2:
        return 1
    if not(n-1 in dict):
        dict[n-1]=fib(n-1)
    if not(n-2 in dict):
        dict[n-2]=fib(n-2)
    return dict[n-1]+dict[n-2]
    
print(fib(100))
        
