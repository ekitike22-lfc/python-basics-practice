number = int(input('Provide a three digits number: '))

if number < 100 or number > 999:
    print("Please provide a three-digit number.")
else:
    # extract digits
    hundreds = number // 100
    tens = (number % 100) // 10
    ones = number % 10
    sum_of_digits = hundreds + tens + ones
    product_of_digits = hundreds * tens * ones

    # prints
    print("Hundreds:", hundreds)
    print("Tens:", tens)
    print("Ones:", ones)
    print("Sum of digits:", sum_of_digits)
    print("Product of digits:", product_of_digits)
