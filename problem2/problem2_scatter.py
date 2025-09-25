import matplotlib
matplotlib.use("Agg")  # non-GUI backend, safe for saving files
import matplotlib.pyplot as plt
from problem1.problem1_random import generate_data

def plot_scatter():
    data = generate_data()
    plt.scatter(data[:, 0], data[:, 1], alpha=0.6, label="Problem 1 data")
    plt.title("Scatter Plot of Problem 1 Data")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend()
    plt.savefig("data/scatter_plot.png")
    plt.close()
    
if __name__ == "__main__":
    plot_scatter()
