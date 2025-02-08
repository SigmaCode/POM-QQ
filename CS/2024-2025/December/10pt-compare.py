import time
import matplotlib.pyplot as plt
from dpsol import dp
from naivesol import naive

# Adjust these values if naive solution is too slow on your machine.
x_vals = range(0, 425, 25)
naive_y_vals = []
dp_y_vals = []

if __name__ == "__main__":
    
    for T in x_vals:
        start = time.time()
        closest = dp(T, [3, 6, 7, 2])
        dp_y_vals.append(time.time() - start)
        
        print(f"Ran DP T={T} in {dp_y_vals[-1]} seconds.")
        
        start = time.time()
        closest = naive(T, 3, 6, 7, 2)
        naive_y_vals.append(time.time() - start)
        
        print(f"Ran Naive T={T} in {naive_y_vals[-1]} seconds.")

            
    plt.plot(x_vals, naive_y_vals, label="Naive", color="red")
    plt.plot(x_vals, dp_y_vals, label="DP", color="blue")
    plt.xlabel("Target Potency (T)")
    plt.ylabel("Time (s)")
    plt.title("Naive vs. DP Solution Time")
    plt.legend()
    plt.show()
    