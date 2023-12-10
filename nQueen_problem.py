import time
import matplotlib.pyplot as plt

def is_safe(board, row, col, n):
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_nq_util(board, col, n):
    if col >= n:
        print_board ( " ".join(str(i) for i in j) for j in board)
        return True

    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1

            if solve_nq_util(board, col + 1, n):
                return True

            board[i][col] = 0

    return False

def solve_n_queens_recursive(n):
    board = [[0 for _ in range(n)] for _ in range(n)]

    if not solve_nq_util(board, 0, n):
        return False

    return True

def print_board(board):
    for row in board:
        print(row)
    print()

def non_recursive_solve_n_queens(n):
    positions = [-1] * n
    row, col = 0, 0
    while row < n:
        while col < n:
            if is_valid(positions, row, col):
                positions[row] = col
                col = 0
                break
            else:
                col += 1

        if positions[row] == -1:
            if row == 0:
                break
            else:
                row -= 1
                col = positions[row] + 1
                positions[row] = -1
                continue

        if row == n - 1:
            col = positions[row] + 1
            positions[row] = -1
            continue

        row += 1

        # print(positions)

    return True

def is_valid(positions, row, col):
    for i in range(row):
        if positions[i] == col or \
           positions[i] - i == col - row or \
           positions[i] + i == col + row:
            return False
    return True

def main():
    n = int(input("Masukkan jumlah ratu: "))
    n_values = list(range(1, n + 1))
    recursive_times = []
    non_recursive_times = []

    for n in n_values:
        start_time = time.time()
        solve_n_queens_recursive(n)
        end_time = time.time()
        recursive_times.append((end_time - start_time) * 1000)  # Konversi detik ke milidetik
        print(f"Pendekatan Rekursif ke {n} : {(end_time - start_time) * 1000:.6f} ms")

        start_time = time.time()
        non_recursive_solve_n_queens(n)
        end_time = time.time()
        non_recursive_times.append((end_time - start_time) * 1000)  # Konversi detik ke milidetik
        print(f"Pendekatan Non-Rekursif ke {n}: {(end_time - start_time) * 1000:.6f} ms")

    plt.figure(figsize=(10, 6))
    plt.plot(n_values, recursive_times, marker='o', label='Pendekatan Rekursif')
    plt.plot(n_values, non_recursive_times, marker='x', label='Pendekatan Non-Rekursif')
    plt.xlabel('n (Jumlah Ratu)')
    plt.ylabel('Waktu Komputasi (ms)')
    plt.title('Waktu Komputasi n-Queens: Rekursif vs Non-Rekursif')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
