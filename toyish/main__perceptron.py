from typing import * 



from Neuron import Neuron
from InputNeuron import InputNeuron
from OutputNeuron import OutputNeuron
from Network import Network
from Connection import Connection
from DataUnit import DataUnit

from Activations.sigmoid import sigmoid
from DerivActivations.sigmod_deriv import sigmoid_deriv

import get_rear_neurons_of
import get_input_neurons
import calculate_weighted_sum

class Perceptron(Neuron):
	def __init__(self, title:str):
		Neuron.__init__(self, title=title)

		#neurons definintion
		i1=InputNeuron(title="i1")
		i2=InputNeuron(title="i2")
		i3=InputNeuron(title="i3")
		p=Neuron(title="p")
		o=OutputNeuron(title="o")

		#neuron placement
		self.neurons = [i1,i2,i3,p,o]


		#neuron connections
		n.connections = [
				Connection(i1, p),
				Connection(i2, p),
				Connection(i3, p),
				Connection(p,  o)]
		

if __name__ ==  "__main__":
	n:Network = Perceptron(title="perceptron")
	#dataset 
	dataset:List[DataUnit] = [
		DataUnit(inputs=[0,0],label=0),
		DataUnit(inputs=[0,1],label=1),
		DataUnit(inputs=[1,0],label=1),
		DataUnit(inputs=[1,1],label=1)]
	


	#training
	dataunit:DataUnit 
	label:float = dataunit.label
	inputs:List[float] = dataunit.inputs
	input_data:int
	input_neuron:Neuron

	input_neurons = get_input_neurons.get(netowrk=n)
	for dataunit in dataset:#one cycle of teaching

		for input_data, input_neuron in zip(inputs,[i1,i2,i3]):#one cycle of loading the data
			input_neuron.output = input_data

		calculated_output = calculate_weighted_sum.calculate(network=n, target_neuron=p)
		expected_output = dataunit.label
		error = weighted_sum - calculated_output 
		




	







