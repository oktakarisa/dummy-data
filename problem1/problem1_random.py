import numpy as np

def generate_data():
    np.random.seed(0)
    mean = [-3, 0]
    cov = [[1.0, 0.8], [0.8, 1.0]]
    data = np.random.multivariate_normal(mean, cov, 500)
    print("Shape of data:", data.shape)
    return data

if __name__ == "__main__":
    data = generate_data()
