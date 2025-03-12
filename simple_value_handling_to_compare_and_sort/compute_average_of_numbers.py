# Prog05: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the average. 
'''
    set total_sum of numerical inputs to 0
    set frequency_counter to track the number of items

    while loop
        try-except
            input number
            add number to total sum
            add 1 to frequency counter
        except ValueError
    
# Compute for average:
    set average equal to total_sum divided by frequency_counter

    print average
'''

total_sum = 0
frequency_counter = 0

while True:
    try:
        number = float(input("Enter a number: "))
        total_sum += number
        frequency_counter += 1
    except ValueError:
        break

average = total_sum / frequency_counter

print(f"The average of your numbers is: {average}")
