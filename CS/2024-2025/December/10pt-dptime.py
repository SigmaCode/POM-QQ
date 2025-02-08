import time
import matplotlib.pyplot as plt
from dpsol import dp
from naivesol import naive

# Adjust these values if code takes too long on your machine.
x_vals = range(0, 201000, 1000)
y_vals = []

if __name__ == "__main__":
    
    for T in x_vals:
        start = time.time()
        closest = dp(T, [3, 6, 7, 2])
        y_vals.append(time.time() - start)
        
        print(f"Ran DP T={T} in {y_vals[-1]} seconds.")

            
    plt.plot(x_vals, y_vals, label="DP", color="blue")
    plt.xlabel("Target Potency (T)")
    plt.ylabel("Time (s)")
    plt.title("DP Solution Time")
    plt.show()
    