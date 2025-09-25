import numpy as np
from problem4.problem4_addition import add_and_plot

def combine_data():
    data1, data2 = add_and_plot()
    combined = np.vstack((data1, data2))
    print("Combined data shape:", combined.shape)
    return combined

if __name__ == "__main__":
    combine_data()
