import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Password Generator!")
nr_le = int(input("The number of characters in your password: "))
nr_nu = int(input("The number of number in your password: "))
nr_sb = int(input("The number of symbols in your password: "))
password = []
for char in range(1, nr_le + 1):
    password.append(random.choice(letters))
for char in range(1, nr_nu + 1):
    password += random.choice(numbers)
for char in range(1, nr_sb + 1):
    password += random.choice(symbols)
random.shuffle(password)
x = "".join(password)
print(f"\nYour password is: {x}")
