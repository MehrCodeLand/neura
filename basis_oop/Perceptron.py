#la imports
from typing import * 


from Network import Network
from Neuron import Neuron 
from Connection import Connection
from DataUnit import DataUnit

import generate_readble_random_string

#network 

class Perceptron(Network):
    def __init__(self, input_size:int):
        Network.__init__(self)
        #input neurons 
        for i in range(input_size):
            the_neuron:Neuron = Neuron(title="input_"+generate_readble_random_string.generate())
            self.input_neurons.append(the_neuron)

        #core neuron 
        core:Neuron = Neuron(title="core")
        self.mid_neurons.append([core])
        
        #output neuron 
        output_neuron:Neuron = Neuron(title="output")
        self.output_neurons.append(output_neuron)

        #making input to core connections
        input_neuron:Neuron
        for input_neuron in self.input_neurons:
            the_connection = Connection(from_=input_neuron, to_=core)
            self.connections.append(the_connection)

        #making core to output connection
        core_to_output_connection:Connection = Connection(from_=core, to_=output_neuron)
        self.connections.append(core_to_output_connection)


        #done making perceptron 





       
        



if __name__ == "__main__":
    dataset:List[DataUnit] = [ #AND gate 
        DataUnit([1.0, 1.0],[1.0]),#first argument is the inputs ; #second argument is the expected outputs
        DataUnit([1.0, 0.0],[0.0]),
        DataUnit([0.0, 1.0],[0.0]),
        DataUnit([0.0, 0.0],[0.0])
    ]

    p = Perceptron(2)
    print(p)
