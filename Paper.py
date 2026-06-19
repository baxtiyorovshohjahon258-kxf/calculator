# while True:
#     print("\n1. Yig'indini hisoblash")
#     print("2. Ayirmani hisoblash")
#     print("3. Ko'paytmani hisoblash")
#     print("4. Bo'linmani hisoblash")
#     print("5. Chiqish")

#     tanlov = input("Tanlang (1-5): ")

#     if tanlov == "5":
#         print("Foydalanganingiz uchun rahmat!")
#         break

#     A = int(input("Birinchi sonni kiriting: "))
#     B = int(input("Ikkinchi sonni kiriting: "))

#     if tanlov == "1":
#         print("Natija:", A + B)

#     elif tanlov == "2":
#         print("Natija:", A - B)

#     elif tanlov == "3":
#         print("Natija:", A * B)

#     elif tanlov == "4":
#         if B != 0:
#             print("Natija:", A / B)
#         else:
#             print("0 ga bo'lish mumkin emas!")

#     else:
#         print("Noto'g'ri tanlov!")

while True:
        print("\n1. Yig'indini hisoblash")
        print("2. Ayirmani hisoblash")
        print("3. Ko'paytmani hisoblash")
        print("4. Bo'linmani hisoblash")
        print("5. Chiqish")

        tanlov = input("Tanlang (1-5): ")

        if tanlov == "5":
            print("Foydalanganingiz uchun rahmat!")
            break

        if tanlov not in ("1", "2", "3", "4"):
            print("Noto'g'ri tanlov!")
            continue

        son_1 = float(input("Birinchi sonni kiriting: "))
        son_2 = float(input("Ikkinchi sonni kiriting: "))

        if tanlov == "1":
            print("Natija:", son_1 + son_2)

        elif tanlov == "2":
            print("Natija:", son_1 - son_2)

        elif tanlov == "3":
            print("Natija:", son_1 * son_2)

        elif tanlov == "4":
            if son_2 == 0:
                print("Nolga bo'lib bo'lmaydi!")
            else:
                print("Natija:", son_1 / son_2)