def sum_floats():
    total = 0.0
    while True:
        user_input = input("Enter hours worked (or 'x' to exit): ")
        if user_input.lower() == "x":
            break  # Exit the loop if the user enters 'x'
        try:
            float_value = float(user_input)
            total += float_value
        except ValueError:
            print("Invalid input! Enter a number or 'x to exit.")
    return total


result = sum_floats()

if result.is_integer():
    print("Total hours is:", int(result))
else:
    print("Total hours is:", result)