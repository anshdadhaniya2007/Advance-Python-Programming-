def decorator(func):
    def wrapper(islogedin):
        if islogedin==True:
            func(islogedin)
            print("You are sucssesfully loged in")
        else:
            print("accces denied, please log in first")
    return wrapper
@decorator
def dashboard(islogedin):
    print("welcom you have succesfully loged in")
    print("providing acces")

status=input("have you logged in")
if status=="yes":
    islogedin=True
else:
    islogedin=False
dashboard(islogedin) 