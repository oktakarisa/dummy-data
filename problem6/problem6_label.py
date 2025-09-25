import numpy as np
import pandas as pd
from problem5.problem5_combine import combine_data

def label_data():
    data1_size = 500
    data2_size = 500

    combined = combine_data()
    labels = np.array([0] * data1_size + [1] * data2_size).reshape(-1, 1)
    labeled_data = np.hstack((combined, labels))

    df = pd.DataFrame(labeled_data, columns=["X", "Y", "Label"])
    df.to_csv("data/labeled_data.csv", index=False)
    print("Labeled data shape:", labeled_data.shape)
    return labeled_data

if __name__ == "__main__":
    label_data()
