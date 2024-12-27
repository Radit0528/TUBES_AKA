#Wisnu Rananta Raditya Putra 2311102013
#Fattah Rizqy Adhipratama 2311102019

import timeit
import random
import matplotlib.pyplot as plt

def merge_sort_recursive(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        merge_sort_recursive(left_half)
        merge_sort_recursive(right_half)
        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i][1] < right_half[j][1]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

def merge_sort_iterative(arr):
    width = 1
    n = len(arr)
    while width < n:
        for i in range(0, n, 2 * width):
            left = arr[i:i + width]
            right = arr[i + width:i + 2 * width]
            i_left = i_right = 0
            for k in range(i, min(i + 2 * width, n)):
                if i_left < len(left) and (i_right >= len(right) or left[i_left][1] <= right[i_right][1]):
                    arr[k] = left[i_left]
                    i_left += 1
                else:
                    arr[k] = right[i_right]
                    i_right += 1
        width *= 2

def generate_randomized_games(max_size):
    games = []
    for i in range(max_size):
        name = f"Game {i+1}"
        size_gb = random.randint(10, 100) 
        games.append(((name, size_gb), size_gb))
    random.shuffle(games)  
    return games

def stringify_games(games):
    return [f"{game[0][0]} ({game[0][1]} GB)" for game in games]

if __name__ == "__main__":
    inputs = []
    recursive_times = []
    iterative_times = []

    for max_size in [4, 5, 6, 7]:  
        games = generate_randomized_games(max_size)
        print(f"\nJumlah Game: {max_size}")
        print("Game Sebelum Pengurutan:", stringify_games(games))

        # Rekursif
        recursive_games = games[:]
        recursive_time = timeit.timeit(lambda: merge_sort_recursive(recursive_games), number=1)
        print("\nHasil Pengurutan Rekursif:", stringify_games(recursive_games))
        print(f"Waktu Eksekusi Rekursif: {recursive_time:.6f} detik")

        # Iteratif
        iterative_games = games[:]
        iterative_time = timeit.timeit(lambda: merge_sort_iterative(iterative_games), number=1)
        print("\nHasil Pengurutan Iteratif:", stringify_games(iterative_games))
        print(f"Waktu Eksekusi Iteratif: {iterative_time:.6f} detik")
        print("\n===================================================================================")

        # Menyimpan data untuk Grafik
        inputs.append(max_size)
        recursive_times.append(recursive_time)
        iterative_times.append(iterative_time)

    # Menampilkan Grafik
    plt.figure(figsize=(10, 6))
    plt.plot(inputs, recursive_times, marker="o", label="Rekursif")
    plt.plot(inputs, iterative_times, marker="o", label="Iteratif")
    plt.title("Perbandingan Waktu Eksekusi Merge Sort Rekursif dan Iteratif")
    plt.xlabel("Jumlah Game")
    plt.ylabel("Waktu Eksekusi (detik)")
    plt.legend()
    plt.grid()
    plt.show()
