import json
import os


# ანგარიშის კლასი

class Account:
    def __init__(self, name, balance=0):
        self.name = name  
        self.balance = balance 
    # თანხის შეტანა
    def deposit(self, amount):
        if amount <= 0:
            print("შეტანილი თანხა უნდა იყოს დადებითი რიცხვი")
            return
        self.balance += amount
        print(f"{amount}-ლარი წარმატებით დაემატა ბალანსს.")
    # თანხის გატანა
    def withdraw(self, amount):
        if amount <= 0:
            print("გამოტანილი თანხა უნდა იყოს დადებითი!")
            return
        if amount > self.balance:
            print("ანგარიშზე არ არის საკმარისი თანხა!")
            return
        self.balance -= amount
        print(f" თქვენ წარმატებით გაიტანეთ. {amount} ლარი.")
    # ბალანსის ნახვა
    def show_balance(self):
        print(f"მიმდინარე ბალანსი: {self.balance} ")

# ბანკომატის კლასი
class ATM:
    def __init__(self, filename="account.json"):
        self.filename = filename
        self.account = self.load_account() 

    # ანგარიშის ჩატვირთვა JSON ფაილიდან
    def load_account(self):
        if not os.path.exists(self.filename):
            print("ანგარიში ვერ მოიძებნა. ახალი ანგარიშის შექმნა.")
            name = input("შეიყვანეთ თქვენი სახელი: ")
            account = Account(name)
            self.save_account(account)
            return account
        try:
            with open(self.filename, "r") as f:
                data = json.load(f)
                return Account(data["name"], data["balance"])
        except:
            print("ფაილის წაკითხვისას დაფიქსირდა შეცდომა , შეიქმნება ახალი ანგარიში.")
            name = input("შეიყვანეთ თქვენი სახელი: ")
            account = Account(name)
            self.save_account(account)
            return account
    # ანგარუიშის შენახვა JSON ფაილში
    def save_account(self, account):
        try:
            with open(self.filename, "w") as f:
                json.dump({"name":account.name, "balance":account.balance}, f, indent=4)
        except:
            print("ანგარიშის შენახვაში მოხდა შეცდომა!")
    # მთავარი მენიუ
    def menu(self):
        print(f"\nმოგესალმებით, {self.account.name}!")

        while True:
            print("\n1. ბალანსის ნახვა")
            print("2. თანხის შეტანა")
            print("3. თანხის გატანა")
            print("4. გამოსვლა")

            choice = input("აირჩიეთ ოპცია: ")
            try:
                if choice == "1":
                    self.account.show_balance()

                elif choice == "2":
                    amount = float(input("შეიყვანეთ შეტანის თანხა: "))
                    self.account.deposit(amount)
                    self.save_account(self.account)

                elif choice == "3":
                    amount = float(input("შეიყვანეთ გატანის თანხა: "))
                    self.account.withdraw(amount)
                    self.save_account(self.account)

                elif choice == "4":
                    print("გმადლობთ ბანკომატისთვის. კარგად იყავით!")
                    self.save_account(self.account)
                    break

                else:
                    print("არასწორი არჩევანი!")
            except:
                print("შეიყვანეთ რიცხვი მენიუდან")

# პროგრამის გაშვებ
if __name__ == "__main__":
    atm = ATM()
    atm.menu()
