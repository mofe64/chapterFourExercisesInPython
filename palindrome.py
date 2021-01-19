number = input("Enter a values to check if its a palindrome ")
isPalindrome = number == number[::-1]
if isPalindrome:
    print(f"{number} is a palindrome")
else:
    print(f"{number} is not a palindrome")
