collection = [15, 46, 75, 34, 23] # this is a Python list. .

result = 0

for number in collection: # for each number in the collection
    #result = result + number * result receives the old result + the next number added to it's current total. .
    result += number # result, which is my variable initialized with 0 is gonna receive the the number plus next number for each iteration
    #print(result) * just printing each sum considering each iteration
print(f'The sum of the numbers of the list is {result}.') # final result using f strings. .
