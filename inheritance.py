class Mpesa:
     def __init__(self,account_balance, phone_number):
         self.account_balance = account_number
         self.phone_number = phone_number
     def sendmoney(self,account, receipient):
           if self.account_balance >= amount:
               self.account_balance -= amount
               print(f"{amount} KES sent to {receipient}")
           else:
                print("insufficient amount to send")
class personalMpesa(Mpesa):
    def __init__(self,account_balance, phone_number, idno):
        super(). __init__(account_balance,phone_number)
        self. idno = idno
    def buyairtime(self,amount):
           self.account_balance-=amount
           print(f"{amount} KES airtime bought successfull")
class BussinessMpesa (Mpesa):
    def __init__(self,account_balance, phone_number, bussiness):
      super().__init__(account_balance, phone_number)
      self.Bussiness_name = Bussiness_name
    def receive_payment(self,amount):
        self.account_balance +=amount
        print(f"{amount} KES received from a customer ")
personal=personalMpesa(100,748067487)
personal.send_money(300,)
personal_buyairtime(150)