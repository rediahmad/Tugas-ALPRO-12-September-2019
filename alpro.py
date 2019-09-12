GPA = (3 , 2.7 , 2.5 , 4)

def Bonus() : 
    TotalBonus = x * B 
    return TotalBonus

B = 500000

for x in GPA :
    print(x)
    if x > 3 :
        print(x, "anda mendapatkan bonus", Bonus())
    elif x <= 3 :
        print("anda tidak mendapatkan bonus")s