# Prog04: Create a program that ask user to input 2 numbers. Print the quotient of the two numbers without the decimal point
'''
    input 2 numbers
    divide the dividend to the divisor
    print result without decimal
'''

dividend = float(input("Enter the dividend: "))
divisor = float(input("Enter the divisor: "))
    
quotient = dividend / divisor
print(f"{dividend} divided by {divisor} is {int(quotient)}")