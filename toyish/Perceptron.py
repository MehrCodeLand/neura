from typing import * 


from Neuron import Neuron
from InputNeuron import InputNeuron
from OutputNeuron import OutputNeuron
from Connection import Connection

import generate_readble_random_string

class Perceptron(Neuron):
	def __init__(self, title:str, input_size:int):
		Neuron.__init__(self, title=title)

		#neurons definintion
		input_neurons:List[InputNeuron] = []
		
        #forming input neurons 
		for i in range(input_size):
			title:str = "input-"+generate_readble_random_string()
			input_neurons.append(InputNeuron(title=title))

        #forming the core and output neuron
		perceptron_core=Neuron(title="perceptron_core"+generate_readble_random_string())
		output_neuron=OutputNeuron(title="output_neuron"+generate_readble_random_string())

		#neuron placement
		self.neurons = input_neurons+[perceptron_core,output_neuron]
		

        #forming input_to_p connections
		inputs_to_p:List[Connection] = []
		i:InputNeuron
		for i in input_neurons:
			inputs_to_p.append(
				Connection(from_=i, to_=perceptron_core)
            )
			
		#neuron connections
		self.connections = [Connection(perceptron_core,  o)]+inputs_to_p