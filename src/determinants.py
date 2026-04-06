def get_submatrix(matrix, row, col):
    """Returns the submatrix obtained by deleting the given row and column."""
    return [row_list[:col] + row_list[col+1:] for i, row_list in enumerate(matrix) if i != row]

def calculate_determinant(matrix):
    n = len(matrix)

   
    if n == 1:
        return matrix[0][0]

  
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    determinant = 0
    for c in range(n):
       
        minor = get_submatrix(matrix, 0, c)
        cofactor = matrix[0][c] * calculate_determinant(minor)
        if c % 2 == 1:
            determinant -= cofactor
        else:
            determinant += cofactor

    return determinant

print("Enter the matrix row by row. Each row should be numbers separated by spaces.")
print("Press Enter after each row. Type 'done' when finished. (e.g., 1 2 3)")

user_matrix = []
row_num = 0
while True:
    row_input = input(f"Enter row {row_num + 1} (or 'done'): ")
    if row_input.lower() == 'done':
        break
    try:
        row_elements = [float(x) for x in row_input.split()]
        if user_matrix and len(row_elements) != len(user_matrix[0]):
            print("Error: All rows must have the same number of elements.")
            continue
        user_matrix.append(row_elements)
        row_num += 1
    except ValueError:
        print("Invalid input: Please enter valid numbers or 'done'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if not user_matrix:
    print("No matrix entered.")
elif len(user_matrix) != len(user_matrix[0]):
    print("Error: The matrix must be square to calculate the determinant.")
else:
    try:
        det_value = calculate_determinant(user_matrix)
        print(f"The determinant of the matrix is: {det_value}")
    except Exception as e:
        print(f"An error occurred during determinant calculation: {e}")