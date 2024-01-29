def initialize_matrix():
    rows = int(input("Enter the number of Rows: "))
    cols = int(input("Enter the number of Columns: "))

    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            element = int(input('Enter element at pos ' + str(i+1) + 'x' + str(j+1) + ': '))
            row.append(element)
        matrix.append(row)

    return matrix


def matrix_addition(mat1, mat2):
    result = []
    for i in range(len(mat1)):
        row = []
        for j in range(len(mat1[0])):
            row.append(mat1[i][j] + mat2[i][j])
        result.append(row)
    return result


def matrix_subtraction(mat1, mat2):
    result = []
    for i in range(len(mat1)):
        row = []
        for j in range(len(mat1[0])):
            row.append(mat1[i][j] - mat2[i][j])
        result.append(row)
    return result


def matrix_multiplication(mat1, mat2):
    result = []
    for i in range(len(mat1)):
        row = []
        for j in range(len(mat2[0])):
            element = 0
            for k in range(len(mat1[0])):
                element += mat1[i][k] * mat2[k][j]
            row.append(element)
        result.append(row)
    return result

def print_matrix(matrix):
    print('-------Result-------')
    for row in matrix:
        print(row)


def main():
    print("Enter 1st Matrix:")
    mat1 = initialize_matrix()

    print("\nEnter 2nd Matrix:")
    mat2 = initialize_matrix()

    operation = input("\nChoose operation - Addition (+), Subtraction (-), Multiplication (*): ")

    if operation == '+':
        if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
            print("*** ERROR ***")
            print("Matrix dimensions do not match for addition.")
        else:
            result = matrix_addition(mat1, mat2)
            print_matrix(result)
    elif operation == '-':
        if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
            print("*** ERROR ***")
            print("Matrix dimensions do not match for subtraction.")
        else:
            result = matrix_subtraction(mat1, mat2)
            print_matrix(result)
    elif operation == '*':
        if len(mat1[0]) != len(mat2):
            print("*** ERROR ***")
            print("Number of columns in the matrix 1 must be equal to the number of rows in the matrix 2 for multiplication.")
        else:
            result = matrix_multiplication(mat1, mat2)
            print_matrix(result)
    else:
        print("Invalid operation. Please choose +, -, or *.")


if __name__ == "__main__":
    main()