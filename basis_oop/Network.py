from typing import * 

from Connection import Connection
from Neuron import Neuron
from DataUnit import DataUnit

import equalize_list_of_string

class Network:
    def __init__(self):
        self.input_neurons:List[Neuron] = []
        self.mid_neurons:List[List[Neuron]] = [] #a matrix of neurons where each row is a layer of mid neurons 
        self.output_neurons:List[Neuron] = []
        self.connections = []
        self.data_set = []
    
    def __str__(self):
        lines:List[str] = []
        Q:List[Neuron]
        for Q in [self.input_neurons] + self.mid_neurons + [self.output_neurons]:
            for i in range(len(Q)):
                if i == len(lines):
                    lines.append("")
                lines[i] += "  " + Q[i].__str__()
            equalize_list_of_string.equalize(target=lines)



        output = "Neurons:\n"
        for i in lines:
            output += i + "\n"


        output += "Connections:\n"
        c:Connection
        counter = 0 
        for c in self.connections:
            counter += 1
            output += c.__str__() + "  "
            if counter % 4 == 0:
                output += "\n"

        
        
        return output



    def clear_output(self)->None:
        i:Neuron 
        for i in self.output_neurons:
            i.output = None


    def clear_mids(self)->None:
        i:List[Neuron]
        j:Neuron 
        for i in self.mid_neurons:
            for j in i:
                j.output = None


    def clear_input_neurons(self)->None:
        i:Neuron 
        for i in self.input_neurons:
            i.output = None


    def clear(self)->None:
        self.clear_output()
        self.clear_mid_outputs()
        self.clear_input_neurons()


    def load_data_unit(self, data_unit:DataUnit)->None:
        #check if is compatible 
        data_unit_input_count:int = data_unit.inputs.__len__()
        self_input_count:int = self.input_neurons.__len__()
        if data_unit_input_count != self_input_count:
            raise ValueError(f"given data unit has input size of {data_unit_input_count} while the network demands {self_input_count} inputs")
        
        #laod the data 
        i:int
        for i in range(len(data_unit.inputs)):
            self.input_neurons[i].output = data_unit.inputs[i]


    
    def 

            




    




