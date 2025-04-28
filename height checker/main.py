gender = input("Enter your gender: ")
height = int(input("Enter your height(150cm): "))

if gender in ["woman", "female"]:
    if height >= 165 :
        print("you are tall!")
    elif height >= 150:
        print("normal height")
    else:
        print("huh....?")
        
elif gender in ["man" , "male"]:
    if height >= 175:
        print("you are tall!")
    elif height >= 160:
        print("normal height")
    else:
        print("huh....?")
        
else:
    print("error")