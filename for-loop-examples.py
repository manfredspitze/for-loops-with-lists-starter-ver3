# FOR Loop Examples (Python)

# FOR Loop: When you only want your loop 
# to iterate (loop) a certain number of times


# Multiplication Table Using range ( ) Function
number = 7
for i in range(1, 11):
  result = i * number
  print(f'{number} X {i} = {result}')


print()
print()

# Loop Through All List Items (List Iteration)
total = 0
my_numbers = [10, 20, 30, 40, 50]
num_elements = len(my_numbers)
for index in range(num_elements):
    total = total + my_numbers[index]
print(f'SUM of numbers in the list: {total}')

print()
print()

# Loop Through All List Items (List Iteration)
animals = ['cat', 'dog', 'hamster']
for animal in animals:
    print(f'One of my pets is a(n) {animal}.')
print('All these animals have a tail.')

print()
print()