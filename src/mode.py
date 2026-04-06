def find_mode(numbers):
    if not numbers:
        return []

    counts = {}
    for num in numbers:
        counts[num] = counts.get(num, 0) + 1

    max_freq = 0
    if counts:
        max_freq = max(counts.values())

    modes = []
    if max_freq > 0:
        for num, freq in counts.items():
            if freq == max_freq:
                modes.append(num)

    if max_freq == 1 and len(modes) == len(numbers):
        return []

    return sorted(list(set(modes))) 

print("Please enter numbers, separated by spaces (e.g., 1 2 2 3 4 4 4 5):")
user_input = input()

try:
    input_numbers = [float(x) for x in user_input.split()]
    if input_numbers:
        modes = find_mode(input_numbers)
        if modes:
            print(f"The mode(s) of the input numbers are: {modes}")
        else:
            print("There is no distinct mode for the given numbers (all numbers are unique or equally frequent).")
    else:
        print("No numbers were entered.")
except ValueError:
    print("Invalid input: Please enter valid numbers.")
except Exception as e:
    print(f"An error occurred: {e}")
