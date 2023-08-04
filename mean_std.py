import numpy as np

def audit_data(dataset):
    # Convert the dataset to a numpy array
    data = np.array(dataset)

    # Calculate the mean and standard deviation
    mean_value = np.mean(data)
    std_dev = np.std(data)

    return mean_value, std_dev

# Example dataset
data_list = [8.1, 2.4, 6.8, 1.1, 7.7, 1.2, 3.6]

# Call the audit function and print the results
mean_result, std_dev_result = audit_data(data_list)
print("Mean:", mean_result)
print("Standard Deviation:", std_dev_result)
