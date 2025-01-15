# Multiply all preceeding numbers until you get to 1. E.g. for the number 3! = 3x2x1 = 6 - if the number is 0, than it results 1. .

number = int(input('Type the number to calculate the Factorial: '))
print()
if number < 0:
    print('Type just positive numbers')
else:
    factorial = 1
    for i in range(1, number + 1): # if we want to include the number itself in the iteration we need to apply the + 1 to the loop range. .
        factorial *= i
        print(f'{factorial // i} * {i} = {factorial}') # // performs integer division, discarding the decimal part.
        #print(factorial)
    print()
print(f'The result of the factorial of the number {number} is {factorial}')



'''

1 * 1 equals 1 integer divided per 1 = 1  # Initial calculation, 1 * 1 = 1, integer division 1 // 1 = 1
1 * 2 equals 2 integer divided per 2 = 1  # After multiplying, 1 * 2 = 2, integer division 2 // 2 = 1
2 * 3 equals 6 integer divided per 3 = 2  # After multiplying, 2 * 3 = 6, integer division 6 // 3 = 2
6 * 4 equals 24 integer divided per 4 = 6  # After multiplying, 6 * 4 = 24, integer division 24 // 4 = 6
24 * 5 equals 120 integer divided per 5 = 24  # After multiplying, 24 * 5 = 120, integer division 120 // 5 = 24

'''
