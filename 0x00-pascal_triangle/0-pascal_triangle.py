def pascal_triangle(n):
    """
    Returns a list of lists representing the Pascal's Triangle of n.
    """
    if n <= 0:
        return []

    triangle = [[1]]  # Start with the first row

    for i in range(1, n):
        prev_row = triangle[-1]
        curr_row = [1]  # Each row starts and ends with 1

        # Calculate the inner elements of the current row
        for j in range(1, len(prev_row)):
            curr_row.append(prev_row[j - 1] + prev_row[j])

        curr_row.append(1)  # Add the final 1 to the current row
        triangle.append(curr_row)

    return triangle