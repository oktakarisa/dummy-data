import numpy as np
import matplotlib.pyplot as plt
from problem1.problem1_random import generate_data

def plot_scatter():
    data = generate_data()
    plt.scatter(data[:, 0], data[:, 1], alpha=0.6)
    plt.title("Scatter Plot of Dummy Data")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.savefig("../data/scatter_plot.png")
    plt.close()
    print("Scatter plot saved as ../data/scatter_plot.png")

if __name__ == "__main__":
    plot_scatter()
