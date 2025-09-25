import numpy as np
import matplotlib.pyplot as plt
from problem1.problem1_random import generate_data

def plot_histograms():
    data = generate_data()

    # Histogram for X
    plt.hist(data[:, 0], bins=30, alpha=0.7)
    plt.title("Histogram of X dimension")
    plt.xlabel("X values")
    plt.ylabel("Frequency")
    plt.xlim(-7, 2)
    plt.savefig("../data/histogram_x.png")
    plt.close()

    # Histogram for Y
    plt.hist(data[:, 1], bins=30, alpha=0.7)
    plt.title("Histogram of Y dimension")
    plt.xlabel("Y values")
    plt.ylabel("Frequency")
    plt.xlim(-4, 4)
    plt.savefig("../data/histogram_y.png")
    plt.close()

    print("Histograms saved as ../data/histogram_x.png and ../data/histogram_y.png")

if __name__ == "__main__":
    plot_histograms()
