

from Neuron import Neuron 
from Network import Network
from Connection import Connection

def get(network:Network, target_neuron:Neuron):
    connection:Connection

    output:List[Connection] = list()

    for connection in network.connections:
        if connection.to_neuron == target_neuron:
            output.append(connection)

    return output