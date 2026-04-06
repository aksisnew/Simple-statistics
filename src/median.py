def find_median(numbers):
    if not numbers:
        return None 

    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)

    if n % 2 == 1: 
        median = sorted_numbers[n // 2]
    else: 
        mid1 = sorted_numbers[n // 2 - 1]
        mid2 = sorted_numbers[n // 2]
        median = (mid1 + mid2) / 2
    return median

print("Please enter numbers, separated by spaces (e.g., 10 20 30 40 50):")
user_input = input()

try:
    input_numbers = [float(x) for x in user_input.split()]
    if input_numbers:
        median_value = find_median(input_numbers)
        if median_value is not None:
            print(f"The median of the input numbers is: {median_value}")
        else:
            print("No numbers were entered to calculate the median.")
    else:
        print("No numbers were entered.")
except ValueError:
    print("Invalid input: Please enter valid numbers.")
except Exception as e:
    print(f"An error occurred: {e}")
