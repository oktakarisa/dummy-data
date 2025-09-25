import numpy as np
import matplotlib.pyplot as plt
from problem1.problem1_random import generate_data

def add_and_plot():
    np.random.seed(0)
    mean_new = [0, -3]
    cov = [[1.0, 0.8], [0.8, 1.0]]
    new_data = np.random.multivariate_normal(mean_new, cov, 500)

    old_data = generate_data()

    plt.scatter(old_data[:, 0], old_data[:, 1], alpha=0.6, label="0")
    plt.scatter(new_data[:, 0], new_data[:, 1], alpha=0.6, label="1")
    plt.title("Combined Scatter Plot")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.legend()
    plt.savefig("../data/combined_scatter.png")
    plt.close()

    print("Combined scatter saved as ../data/combined_scatter.png")
    return old_data, new_data

if __name__ == "__main__":
    add_and_plot()
