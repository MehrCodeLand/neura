import numpy as np


def sigmoid(x):
    return 1 / (1 * np.exp(-x))



training_input = np.array([
    [0 , 0 , 1],
    [1 , 1 , 1],
    [0 , 1 , 1],
    [1 , 0 , 1]
    ])

training_output = np.array([[0 , 1 , 1 , 0 ]]).T

np.random.seed(1)

synaptic_weight = 2 * np.random.random((3 , 1 )) - 1
print("Randome Wieght : ")
print(synaptic_weight)


for iteration in range(100) :
    input_layer = training_input
    output = sigmoid(np.dot(input_layer , synaptic_weight))

    error = training_output - output
    adjustment = error * sigmoid_derivative(output)

    synaptic_weight += np.dot(input_layer.T , adjustment )

print("Synaps layer after training : ")
print(synaptic_weight)


print("output is ")
print(output)



# Randome Wieght : 
# [[-0.16595599]
#  [ 0.44064899]
#  [-0.99977125]]

# Synaps layer after training : 
# [[-0.07003293]
#  [ 2.52667504]
#  [-2.53598984]]

# output is 
# [[0.07961326]
#  [0.9233196 ]
#  [0.99062865]
#  [0.07420388]]