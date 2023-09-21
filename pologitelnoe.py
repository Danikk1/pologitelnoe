def sum_digits(number):
    sum = 0
    for digit in str(number):
        sum += int(digit)
    return sum
print(sum_digits(1234))