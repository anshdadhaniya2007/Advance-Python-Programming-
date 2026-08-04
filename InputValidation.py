def decorator(func):
    def wrapper(acsses):
        if acsses==True:
            func(acsses)
            print("your sum has been calculated")
        else:
            print("your function is not executed")
    return wrapper
@decorator
def sum(acsses):
    print("your function is executed")            
a=int(input("enter numbers"))
b=int(input("enter numbers"))
c=int(input("enter numbers"))
if (a>=0 and b>=0 and c >=0):
    acsses=True
else:
    acsses=False
sum(acsses)