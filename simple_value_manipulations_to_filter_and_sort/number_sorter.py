# Prog05: Create a program that ask user to input a number, continue asking 
# until the user input is invalid. Display the number from lowest to highest. 
# Clue: sort() function --number_sorter

# Pseudocode
# - set list_num

# - while loop
# - try-except
# - input number
# - except valueerror
# - break

# - sort list_num
# - print list_num

list_num = []

while True:
    try:
        number = float(input("Enter a number: "))
        list_num.append(number)

    except ValueError:
        if list_num:
            print("Printing results...")
        else:
            print("No valid inputs were entered.")
        break

if list_num:
    list_num.sort()
    print(f"\nSorted numbers: {list_num}")