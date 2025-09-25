import numpy as np
import pandas as pd
from problem5.problem5_combine import combine_data
from problem1.problem1_random import generate_data

def label_data():
    old_data = generate_data()
    np.random.seed(0)
    mean_new = [0, -3]
    cov = [[1.0, 0.8], [0.8, 1.0]]
    new_data = np.random.multivariate_normal(mean_new, cov, 500)

    combined = np.vstack((old_data, new_data))
    labels = np.array([0]*500 + [1]*500).reshape(-1, 1)

    labeled_data = np.hstack((combined, labels))
    print("Shape of labeled data:", labeled_data.shape)

    # Save as CSV
    df = pd.DataFrame(labeled_data, columns=["x", "y", "label"])
    df.to_csv("../data/labeled_data.csv", index=False)
    print("Labeled data saved as ../data/labeled_data.csv")

    return labeled_data

if __name__ == "__main__":
    label_data()
