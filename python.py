# A = 0
# for B in range(0 , 11):
#     if B%2 == 0:
#         A = A + B
# print(A)

# son = 0.00
# for hisob in range(0 , 20 , 2):
#     if hisob%2 == 0.0000000 :
#         son = son + hisob
# print(son)
# A = "shohjahon , baxtiyorov"
# for i in A:
#     print(i.capitalize())
# a = 0
# matn = str(input("matn: "))
# for i in matn :
#     a = a + 1
# print(a)

# ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;; JUFT SONLAR YIG'INDISI:

# a = 0
# for b in range(0 , 11):
#     if b%2 == 0:
#         a = a + b
# print(a)
# ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;; TOQ SONLAR YIG'INDISI:

# a = 0
# for i in range(0 ,11):
#     if i%2 != 0:
#         a = a + i
# print(a)

# ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;; a DAN b GACHA SONLAR YIG'INDISI:

# a = int(input("sonni kiriting: "))
# b = int(input("sonni kiriting: "))
# for i in range(a , b):
#     if i%0 
#     print(i)
# errrrrroroooor

# a = 1
# b = 20
# c = 0
# DAVR = int(input(" 1 dan 5 gacha ixtiyoriy  son kiriting: "))
# for i in range(a , b ):
#     c =  c + i
#     print(i)
# print(c)



# natija>>>>>>>>>
# 5 ta juft 
# 5 ta toq 

# A = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10]
# juft = 0
# toq = 0
# for i in A:
#     if i%2 == 0:
#         juft = juft + 1
#     elif i%2 != 0:
#         toq = toq + 1

# print("juftlar", juft , "ta")
# print("toqlar" , toq , "ta")

# /;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

# B = [ 25 , 54 , 61 , 56 , 584 , 151]
# JUFT = 0
# TOQ = 0
# for i in B:
#     if i%2 == 0:
#         JUFT += 1
#     elif i%2 != 0:
#         TOQ += 1
# print("juftlar" , JUFT , "ta")
# print("toqlar"  ,TOQ , "ta")

# ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
# B = [ 25 , 54 , 61 , 10 , 200 , 151]
# gigant = B[0]
# for son in B:
#     if son > gigant:
#         gigant = son
# print(gigant) 
 
# matn = str(input("ixtiyoriy matn kiriting: "))  


# print(matn.lower())

# print(matn.capitalize())

# print(matn.index("o") , "ta shu harf qatnashgan ushbu matnda ")

# print(matn.upper())

# print(matn.title())
# print(matn.())
# print(matn.())
# print(matn.())
# print(matn.())
# print(matn.())







# while True:
#     print("1", "yig'indini hisoblang")
#     print("2", "ayirmani hisoblang")
#     print("3", "ko'paytmani hisoblang")
#     print("4", "bo'linmani hisoblang")
#     print("5", "amallar tarixini ko'rish")
#     print("6", "Chiqish")

#     call = int(input("1 dan 7 gacha tanlang: "))

#     A = int(input("sonni kiriting: "))
#     B = int(input("sonni kiriting: "))

#     son = int(input("amalni bajaring: "))

#     if son == 1:
#         print(A + B)

    # cost = int(input("sonni kiriting: "))
    # if cost == 2:
    #     print(A - B)

    # change = int(input("sonni kiriting: "))
    # if change == 3:
    #     print(A * B)

    # num = int(input("sonni kiriting: "))
    # if num == 4:
    #     print(A / B)
    # elif B != 0:
    #     print("mavjud emas")

    # digital = int(input("sonni kiriting: "))
    # if digital == 5:
    #     print("hisob bosh")

    # digitals = int(input("tanlang: "))
    # if digitals == 6:
    #     print("foydalanganingiz uchun raxmat!")
    #     break






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

    A = float(input("Birinchi sonni kiriting: "))
    B = float(input("Ikkinchi sonni kiriting: "))

    if tanlov == "1":
        print("Natija:", A + B)

    elif tanlov == "2":
        print("Natija:", A - B)

    elif tanlov == "3":
        print("Natija:", A * B)

    elif tanlov == "4":
        if B != 0:
            print("Natija:", A / B)
        else:
            print("0 ga bo'lish mumkin emas!")

    else:
        print("Noto'g'ri tanlov!")








































