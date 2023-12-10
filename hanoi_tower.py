import time
import matplotlib.pyplot as plt
def tower_of_hanoi(n, from_rod, to_rod, aux_rod, moves):
    """
    Recursive function to solve Tower of Hanoi puzzle.
    
    Args:
    n (int): Number of disks.
    from_rod (str): The starting rod.
    to_rod (str): The destination rod.
    aux_rod (str): The auxiliary rod.
    moves (list): List to keep track of the moves.
    """
    def move_disk(from_rod, to_rod):
        moves.append((from_rod, to_rod))

    if n == 1:
        move_disk(from_rod, to_rod)
        return
    tower_of_hanoi(n-1, from_rod, aux_rod, to_rod, moves)
    move_disk(from_rod, to_rod)
    tower_of_hanoi(n-1, aux_rod, to_rod, from_rod, moves)

def main():
    # Menginput nilai n
    n = int(input("Enter the number of disks for Tower of Hanoi: "))

    # Mengukur waktu komputasi
    start = time.time()
    moves = []
    tower_of_hanoi(n, 'A', 'C', 'B', moves)
    end = time.time()
    total_time = end - start

    # Menampilkan hasil
    print(f"Time taken for {n} disks: {total_time} seconds")
    print("Moves:")
    counter = 1
    for move in moves:
        print(f"{counter}. Move disk from {move[0]} to {move[1]}")
        counter += 1

    # Untuk plot grafik, kita akan mengulangi proses untuk berbagai nilai n
    n_values = range(1, n+1)
    times = [measure_time(i) for i in n_values]

    # Membuat plot
    plt.plot(n_values, times, marker='o')
    plt.title('Tower of Hanoi Time Complexity')
    plt.xlabel('Number of Disks (n)')
    plt.ylabel('Time (seconds)')
    plt.grid(True)
    plt.show()

def measure_time(n):
    start = time.time()
    moves = []
    tower_of_hanoi(n, 'A', 'C', 'B', moves)
    end = time.time()
    return end - start

# Menjalankan fungsi main
if __name__ == "__main__":
    main()
