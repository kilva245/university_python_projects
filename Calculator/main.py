## import math module 
import math

## here is for pick the calculator model 
calculator_model = input("Please choose a calculator model (basic/comparative/Engineering ): ")

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
        
elif calculator_model == 'Engineering' or calculator_model == 'engineering':
    num1 = float(input("Enter your number: "))
    cr = input("Enter [sin , cos, tan, cot, pi, e, ceil, floor, log, log10, log2, round, sqrt, abs]")
    
    if cr == 'sin':
        print(math.sin(num1))
    elif cr == 'cos':
        print(math.cos(num1))
    elif cr == 'tan':
        print(math.tan(num1))
    elif cr == 'pi':
        print(math.pi)
    elif cr == 'e':
        print(math.e)
    elif cr == 'ceil':
        print(math.ceil(num1))
    elif cr == 'floor':
        print(math.floor(num1))
    elif cr == 'log':
        print(math.log(num1))
    elif cr == 'log10':
        print(math.log10(num1))
    elif cr == 'log2':
        print(math.log2(num1))
    elif cr == 'round':
        print(round(num1))
    elif cr == 'sqrt':
        print(math.sqrt(num1))
    elif cr == 'abs':
        print(abs(num1))
    elif cr == 'cot':
        if math.tan(num1) != 0:
            print(1 / math.tan(num1))
        else:
            print("Undefined (tan(x) = 0)")
    else:
        print('Invalid input')
else:
    print("Invalid calculator model!")