
from Network import Network 
from Neuron import Neuron
from Connection import Connection

import get_rear_connections_of
import get_rear_neurons_of

def calculate(network:Neuron, target_neuron:Neuron):
    rear_connections = get_rear_connections_of.get(network=network, target_neuron=target_neuron)
    rear_neurons = get_rear_neurons_of.get(network=network, target_neuron=target_neuron)

    output:float = 0.0

    connection:Connection 
    for connection in rear_connections:
        output += connection.from_.output * connection.weight

    return output


