from typing import * 

from Network import Network 
from Neuron import Neuron
from InputNeuron import InputNeuron

def get(network:Network):
    output:List[InputNeuron] = []
    neuron:Neuron 
    for neuron in network.neurons: 
        if isinstance(neuron, InputNeuron) == True:
            output.append(neuron)
    return output 
        


