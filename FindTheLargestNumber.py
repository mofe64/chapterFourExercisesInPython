counter = 0
numbers = []
largest = 0
while counter < 10:
    number_string = input("Enter a number")
    number = int(number_string)
    numbers.append(number)
    counter += 1

for number in numbers:
    if largest < number:
        largest = number

print(f"Largest number is {largest}")
