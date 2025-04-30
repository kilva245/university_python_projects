## here is for pick the calculator model 
calculator_model = input("Please choose a calculator model (basic/comparative): ")

## for basic calculator
if calculator_model == 'basic':
    
    ## basic calculator model inputs
    num1 = float(input("Enter first number: "))
    cr = input("Enter + - * ** % / : ")
    num2 = float(input("Enter second number: "))
    
    if cr == '+':
        print(num1 + num2)
    elif cr == '-':
        print(num1 - num2)
    elif cr == '*':
        print(num1 * num2)
    elif cr == '/':
        print(num1 / num2)
    elif cr == '**':
        print(num1 ** num2)
    elif cr == '%':
        print(num1 % num2)
    else:
        print("Invalid operator!")

## for comparative calculator    
elif calculator_model == 'comparative':
    
    ## comparative calculator model inputs
    num1 = float(input("Enter first number: "))
    cr = input("Enter > < >= <= == != : ")
    num2 = float(input("Enter second number: "))
    
    if cr == '>':
        print(num1 > num2)
    elif cr == '<':
        print(num1 < num2)
    elif cr == '>=':
        print(num1 >= num2)
    elif cr == '<=':
        print(num1 <= num2)
    elif cr == '==':
        print(num1 == num2)
    elif cr == '!=':
        print(num1 != num2)
    else:
        print("Invalid operator!")
else:
    print("Invalid calculator model!")