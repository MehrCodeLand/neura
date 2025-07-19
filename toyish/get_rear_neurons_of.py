from typing import * 

from Network import Network
from Neuron import Neuron
from Connection import Connection

def get(network:Network, target_neuron:Neuron)->List[Neuron]:
    output:List[Neuron] = []
    connection:Connection
    for connection in network.connections:
        if connection.to_ == target_neuron:
            output.append(connection.from_)
    return output   
    