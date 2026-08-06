class creditcard:
    def pay(self,amount):
        print("paid ",amount,"using credit card")
class upi:
    def pay(self,amount):
        print("paid" ,amount,"using upi")
class cash:
    def pay(self,amount):
        print("paid ",amount,"using cash")
class payment:
    def __init__(self,strategy):
        self.strategy=strategy
    def process(self,amount):
        self.strategy.pay(amount)
amount=int(input("enter amount"))
choice=int(input("1.cedit card\n2.upi\n3.cash\n"))
if choice==1:
    p=payment(creditcard())
elif choice==2:
    p=payment(upi())
elif choice==3:
    p=payment(cash())
p.process(amount)