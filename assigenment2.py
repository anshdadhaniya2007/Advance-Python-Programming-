def decorator(func):
    def wrapper(self):
        print("="*100)
        func(self)
        print("="*100)
    return wrapper
class report:
    template="normal"
    def __init__(self,tittle,details):
        self.tittle=tittle
        self.details=details
    @classmethod
    def change_template(cls,temp):
        cls.template=temp
    @decorator
    def show(self):  
        if report.template=="upper":
            print(self.tittle.upper())
            for key,value in self.details.items():
                print(key.upper(),":",value.upper())
        else:
            print(self.tittle)
            for key,value in self.details.items():
                print(key,":",value)            
        return
i=True
d={}
while(i==True):
    title=int(input("enter the title of the report\n 1.Buisness Report \n 2.Exam report \n 3.Food report\n"))
    j=int(input("How many feilds do you have regarding report"))
    for _ in range(j):
        key = input("Enter key: ")
        value = input("Enter value: ")
        d[key] = value
    if(title==1):
        r1=report("Buisness Report",d)
    elif(title==2):
        r1=report("Exam report",d)
    elif(title==3):
        r1=report("Food report",d)
    r1.show()
    choise=input("do you want to change the template of the report")
    if choise=="yes":
        r1.change_template("upper")
        r1.show()
    a=input("do you want to continue")
    if a=="no":
        i=False