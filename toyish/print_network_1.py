from typing import * 

from Network import Network
from Neuron import Neuron 
from Connection import Connection


def print_network(network:Network)->None:
    i:Neuron 
    for i in network.neurons:
        print(i):
    i:Connection
    for i in network.connections:
        print(i)

