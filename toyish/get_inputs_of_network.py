from typing import * 


from Network import Network 
from InputNeuron import InputNeuron
from Neuron import Neuron 
from InputNeuron import InputNeuron

def get(network:Network)->List[InputNeuron]:
    i:Neuron 
    output:List[InputNeuron]
    for i in network.neurons:
        if isinstance(i, InputNeuron):
            output.append(i)
        else:
            continue 
    return output
        
