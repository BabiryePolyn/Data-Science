sum_even = 0

for number in range(1, 101):
    if number % 2 == 0:  # Check if number is even
        sum_even = sum_even + number

print(f"The sum of all even numbers between 1 and 100 is: {sum_even}")