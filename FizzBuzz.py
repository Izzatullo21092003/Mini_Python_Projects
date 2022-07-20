for j in range(1, 101):
    if j % 3 == 0 and j % 5 == 0:
        print("FizzBuzz")
    elif j % 3 == 0:
        print("Fizz")
    elif j % 5 == 0:
        print("Buzz")
    else:
        print(j)
