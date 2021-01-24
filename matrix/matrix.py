def matrix(n):
    """Write a function that accepts an integer N
    and returns a NxN spiral matrix.
    """
    matrix = [[0 for j in range(n)] for i in range(n)]
    start_col = 0
    end_col = n - 1
    start_row = 0
    end_row = n - 1
    counter = 1

    while (start_col <= end_col) & (start_row <= end_row):
        print(start_col, end_col, start_row, end_row)

        for i in range(start_col, (end_col + 1)):
            matrix[start_row][i] = counter
            counter += 1
            print(matrix)
        start_row += 1
        for i in range(start_row, end_row + 1):
            matrix[i][end_col] = counter
            counter += 1
            print(matrix)
        end_col -= 1
        for i in range(end_col, (start_col - 1), -1):
            matrix[end_row][i] = counter
            counter += 1
            print(matrix)
        end_row -= 1
        for i in range(end_row, (start_row - 1), -1):
            matrix[i][start_col] = counter
            counter += 1
            print(matrix)
        start_col += 1

        print(start_col, end_col, start_row, end_row)

    return matrix


print(matrix(4))
