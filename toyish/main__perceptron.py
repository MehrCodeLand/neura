from typing import * 



from Neuron import Neuron
from InputNeuron import InputNeuron
from OutputNeuron import OutputNeuron
from Network import Network
from Connection import Connection
from DataUnit import DataUnit
from Perceptron import Perceptron

from Activations.sigmoid import sigmoid
from DerivActivations.sigmod_deriv import sigmoid_deriv

import get_rear_neurons_of
import get_input_neurons
import calculate_weighted_sum


		

if __name__ ==  "__main__":
	p:Network = Perceptron(title="perceptron")
	#dataset 
	dataset:List[DataUnit] = [
		DataUnit(inputs=[0,0],label=0),
		DataUnit(inputs=[0,1],label=1),
		DataUnit(inputs=[1,0],label=1),
		DataUnit(inputs=[1,1],label=1)]
	
	#training

		




	







