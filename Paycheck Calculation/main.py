user_input = float(input("please enter your salary(toman): "))

## 1500000 = Right_to_children , 4500000 = insurance , 7000000 = installments , 15% = tax

all = user_input * (1 - 0.15)  - 1500000  - 4500000 - 7000000


print("Final asset :", all,'toman')