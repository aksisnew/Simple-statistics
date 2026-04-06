def calculate_mean(numbers):
    if not numbers:
        return None
    total = sum(numbers)
    count = len(numbers)
    mean = total / count
    return mean


numbers_list = [10, 20, 30, 40, 50]
mean_value = calculate_mean(numbers_list)

if mean_value is not None:
    print(f"The mean of {numbers_list} is: {mean_value}")
else:
    print("No numbers provided to calculate the mean.")

print("Please enter numbers, separated by spaces (e.g., 10 20 30 40 50):")
user_input_mean = input()

try:
    input_numbers_mean = [float(x) for x in user_input_mean.split()]
    mean_from_input = calculate_mean(input_numbers_mean)
    if mean_from_input is not None:
        print(f"The mean of the input numbers is: {mean_from_input}")
    else:
        print("No numbers were entered to calculate the mean.")
except ValueError:
    print("Invalid input: Please enter valid numbers.")
except Exception as e:
    print(f"An error occurred: {e}")