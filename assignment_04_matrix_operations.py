# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
#

# =============================================================================
# YOUR CODE BELOW
# =============================================================================

def read_matrix(rows, cols, label=""):
    print(f"\nEnter {label} matrix ({rows} x {cols}):")
    matrix = []
    for i in range(rows):
        while True:
            row_input = input(f"Enter row {i + 1}: ").split()
            if len(row_input) != cols:
                print(f"Error: Expected {cols} values, got {len(row_input)}. Try again.")
                continue
            matrix.append([float(val) for val in row_input])
            break
    return matrix


def print_matrix(matrix, title="Matrix"):
    print(f"\n{title}:")
    for row in matrix:
        print("  ".join(f"{val:g}" for val in row))


def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    # Result has swapped dimensions: cols x rows
    result = []
    for j in range(cols):
        new_row = []
        for i in range(rows):
            new_row.append(matrix[i][j])
        result.append(new_row)
    return result


def add_matrices(matrix_a, matrix_b):
    rows = len(matrix_a)
    cols = len(matrix_a[0])

    result = []
    for i in range(rows):
        new_row = []
        for j in range(cols):
            new_row.append(matrix_a[i][j] + matrix_b[i][j])
        result.append(new_row)
    return