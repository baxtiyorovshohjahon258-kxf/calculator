
balance = 100000000
history = []


while True:
    print("\n===== ATM =====")
    print("1. Balansni ko'rish")
    print("2. Pul yechish")
    print("3. Pul qo'shish")
    print("4. Tarixni ko'rish")
    print("5. Chiqish")

    choice = input("Tanlang (1-5): ")

    if choice == "1":
        print("sizning balansingiz:" , balance  , "sum")

    elif choice == "2":
        amount = int(input("Yechmoqchi bo'lgan summa kiriting: "))

        if amount <= 0:
            print("Noto'g'ri summa !")
        elif amount > balance:
            print("Hisobingizda mablag' yetarli emas!")
        else:
            balance -= amount
            history.append(f"- {amount} so'm yechildi")
            print(f"{amount} so'm muvaffaqiyatli yechildi")

    elif choice == "3":
        amount = int(input("Qo'shmoqchi bo'lgan summani kiriting: "))

        if amount <= 0:
            print("Noto'g'ri summa")
        else:
            balance += amount
            history.append("+" , amount , "sum qo'shildi")

    elif choice == "4":
        print("\n===== Tarix =====")
        
        if len(history) == 0:
            print("Tarix bo'sh")
        else:
            for operation in history:
                print(operation)

    elif choice == 5:
        print("ATM dan foydalanganingiz uchun raxmat")
        break
    else:
        print("Noto'g'ri tanlov !")         

