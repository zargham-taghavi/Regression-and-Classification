import numpy as np
import matplotlib.pyplot as plt

x = np.array((1, 2))
y = np.array([300, 500])
# print(type(x), x)
# print(type(y), y)
# Set the title
plt.title("Housing Prices")
# Set the y-axis label
plt.ylabel('Price (in 1000s of dollars)')
# Set the x-axis label
plt.xlabel('Size (1000 sqft)')
plt.scatter(x,y,c="red",marker="x")
plt.show()
w=200
b=100
def compute_model_output(x_array, w, b):
    f_wb = np.zeros(len(x_array))
    for i in range(len(x_array)):
        f_wb[i] = w*x_array[i]+b
    return f_wb

tmp_f_wb = compute_model_output(x, w, b,)

# Plot our model prediction
plt.plot(x, tmp_f_wb, c='b',label='Our Prediction')
# Set the title
plt.title("Housing Prices")
# Set the y-axis label
plt.ylabel('Price (in 1000s of dollars)')
# Set the x-axis label
plt.xlabel('Size (1000 sqft)')

# Plot the data points
plt.scatter(x, y, marker='x', c='r',label='Actual Values')
plt.legend()
plt.show()