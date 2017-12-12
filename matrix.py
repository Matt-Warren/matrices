
# takes 2D array and prints it as a matrix
def printMatrix(matrix):
    to_print = ""
    for x in range(0, len(matrix)):
        for y in range(0, len(matrix[x])):
            if y == 0:
                to_print += "[ "
            to_print += matrix[x][y]
            if y != (len(matrix[x]) - 1):
                to_print += ","
        to_print += " ]\n"

    print(to_print)

def printABMatrix(matrix_a, matrix_b):
    to_print = ""
    for x in range(0, len(matrix_a)):
        for y in range(0, len(matrix_a[x])):
            if y == 0:
                to_print += "[ "
            to_print += matrix_a[x][y]
            if y != (len(matrix_a[x]) - 1):
                to_print += ","
        to_print += " ] -> [" + matrix_b[x][0] + "]\n"

    print(to_print)

# size = pair for size of matrix (ie, (3,3))
# matrix = string version of matrix as: 1,2,3:4,5,6:7,8,9:
def parseMatrix(size, matrix):
    # for each row in matrix
    rows = matrix.split(":")

    # creates matrix full of 0's with size supplied
    # print(size)
    # print("first:" + str(size[0]) + " second:" + str(size[1]))
    new_matrix = [[0 for x in range(int(size[0]))] for y in range(int(size[1]))]

    row_counter = 0
    # print(rows)
    for row in rows:
        # print(row)
        values = row.split(",")
        value_counter = 0
        for value in values:
            # print("row=" + str(row_counter) + " col=" + str(value_counter))
            new_matrix[row_counter][value_counter] = value
            value_counter = value_counter + 1
        row_counter = row_counter + 1

    printMatrix(new_matrix)
    return new_matrix

def solve(matrix_a, matrix_b):
    matrix_result = [[]]
    

    return matrix_result

def main():
    num_equations = input("Enter the number of equations to enter: ")
    num_coefficients = input("Enter the number of unknown coefficients: ")

    # print("#eq:" + num_equations + " #coef:" + num_coefficients)
    
    print("Enter your matrix as such:\n")

    sample_str = ""
    for _x in range(1, int(num_equations) + 1):
        for _y in range(1, int(num_coefficients) + 1):
            if _y != 1:
                sample_str = sample_str + ","
            sample_str += "x" + str(_x) + str(_y)
        sample_str += ":\n"

    print(sample_str)
    print("Where ',' separate coefficients and ':' indicates the end of a row.")
    matrix = input("Enter the matrix now:")
    #print(matrix)
    #print(num_coefficients + num_equations)
    matrix_a = parseMatrix((num_coefficients, num_equations), matrix)

    value_matrix = input("Enter the value matrix now (B):")
    matrix_b = parseMatrix((1, num_equations), value_matrix)
    printABMatrix(matrix_a, matrix_b)








main()
