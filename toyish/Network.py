from typing import *


from Neuron import Neuron
from Connection import Connection
from DataUnit import DataUnit
from InputNeuron import InputNeuron

import  get_input_neurons
import load_data_unit

#"fuck MIcrosoft"
# -someone said that

class Network:
    def __init__(self, title):
        self.neurons:List[Neuron] = []
        self.connections:List[Connection] = []
        self.title = title


    def load_data_unit(self, data_unit:DataUnit):
        load_data_unit(network=self, data_unit=data_unit)

            


