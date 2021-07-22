class ATM(object):
    def __init__(self, card, pin):
        self.pin = pin
        self.card = card
        self.money = 5000

    def withdraw(self):
        print("Cash Withdrawed")

    def balance(self):
        print(f"balance amount = {self.money}")


atm1 = ATM("1234 5678 9123 4567", "1234")
atm1.withdraw()
atm1.balance()

