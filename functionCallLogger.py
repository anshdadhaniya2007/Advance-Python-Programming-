from datetime import datetime
def decorator(func):
    def wrapper():
        print("Name of the function is :", func.__name__)
        print("date and time at which function is been called : ",datetime.now())
    return wrapper
@decorator
def hello():
    print("hello")
hello()