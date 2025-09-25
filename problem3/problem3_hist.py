import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from problem1.problem1_random import generate_data

def plot_hist():
    data = generate_data() 
    # Histogram for X
    plt.hist(data[:, 0], bins=30, alpha=0.7, color="blue")
    plt.title("Histogram of X")
    plt.savefig("data/histogram_x.png")
    plt.close()

    # Histogram for Y
    plt.hist(data[:, 1], bins=30, alpha=0.7, color="green")
    plt.title("Histogram of Y")
    plt.savefig("data/histogram_y.png")
    plt.close()
    
if __name__ == "__main__":
    plot_hist()
