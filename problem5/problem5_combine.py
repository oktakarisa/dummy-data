import numpy as np
from problem4.problem4_addition import add_and_plot

def combine_data():
    old_data, new_data = add_and_plot()
    combined = np.vstack((old_data, new_data))
    print("Shape of combined data:", combined.shape)
    return combined

if __name__ == "__main__":
    combine_data()
