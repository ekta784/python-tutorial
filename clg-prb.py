import numpy as np

data = [6,55,-3,7,9,0]

if len(data) > 0:
    data_array = np.array(data)  
    
    data_range = np.max(data_array) - np.min(data_array)
    variance = np.var(data_array)
    std_deviation = np.std(data_array)
    
    print("Range:", data_range)
    print("Variance:", variance)
    print("Standard Deviation:", std_deviation)
else:
    print("The dataset is empty. Please provide some data.")

