from typing import * 

from InputNeuron import InputNeuron
from Network import Network
from DataUnit import DataUnit

import get_input_neurons

def load(netowrk:Network, data_unit:DataUnit):
    input:float
    input_neurons:List[InputNeuron] = get_input_neurons.get(network=network)
    inputs:List[float] = data_unit.inputs
    for input, input_neuron in zip(inputs, input_neurons):
        input_neuron.output = input