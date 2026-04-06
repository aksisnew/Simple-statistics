def predict_next_numbers(numbers):
    if len(numbers) != 5:
        return "Please provide exactly 5 numbers."

    is_arithmetic = True
    if len(numbers) > 1:
        diff = numbers[1] - numbers[0]
        for i in range(2, len(numbers)):
            if numbers[i] - numbers[i-1] != diff:
                is_arithmetic = False
                break

    if is_arithmetic and len(numbers) > 1:
        predictions = []
        last_num = numbers[-1]
        for _ in range(5):
            last_num += diff
            predictions.append(last_num)
        return predictions

    is_geometric = True
    if len(numbers) > 1 and numbers[0] != 0:
        ratio = numbers[1] / numbers[0]
        for i in range(2, len(numbers)):
            if numbers[i-1] == 0 or numbers[i] / numbers[i-1] != ratio:
                is_geometric = False
                break

    if is_geometric and len(numbers) > 1:
        predictions = []
        last_num = numbers[-1]
        for _ in range(5):
            last_num *= ratio
            predictions.append(last_num)
        return predictions

    predictions = [numbers[-1]] * 5
    return predictions

print("Please enter 5 numbers, separated by spaces:")
user_input = input()
try:
    input_numbers = [float(x) for x in user_input.split()]
    if len(input_numbers) == 5:
        next_five = predict_next_numbers(input_numbers)
        print(f"Based on your input, the predicted next 5 numbers are: {next_five}")
    else:
        print("Invalid input: Please enter exactly 5 numbers.")
except ValueError:
    print("Invalid input: Please enter valid numbers.")
