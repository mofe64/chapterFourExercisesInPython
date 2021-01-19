counter = 0
numbers = []
largest = 0
second_Largest = 0
while counter < 10:
    number_string = input("Enter a number ")
    number = int(number_string)
    numbers.append(number)
    counter += 1

for number in numbers:
    if largest < number:
        second_Largest = largest
        largest = number

print(f"Largest number is {largest}")
print(f"Second largest is {second_Largest}")
