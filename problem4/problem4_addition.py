import numpy as np
import matplotlib
matplotlib.use("Agg")  # non-GUI backend, safe for saving files
import matplotlib.pyplot as plt
from problem1.problem1_random import generate_data

def add_and_plot():
    data1 = generate_data()
    np.random.seed(0)
    mean2 = [0, -3]
    cov = [[1.0, 0.8],
           [0.8, 1.0]]
    data2 = np.random.multivariate_normal(mean2, cov, 500)

    plt.scatter(data1[:, 0], data1[:, 1], alpha=0.6, label="Problem 1 data")
    plt.scatter(data2[:, 0], data2[:, 1], alpha=0.6, label="Problem 4 data")
    plt.title("Combined Scatter Plot")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend()
    plt.savefig("data/combined_scatter.png")
    plt.close()

    return data1, data2

if __name__ == "__main__":
    add_and_plot()
