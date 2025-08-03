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


    #clearing =======================================
    #methods below clear the outputs of neurons
    def clear_outputs(self)->None:
        i:Neuron 
        for i in self.output_neurons:
            i.output = None


    def clear_mids(self)->None:
        i:List[Neuron]
        j:Neuron 
        for i in self.mid_neurons:
            for j in i:
                j.output = None


    def clear_inputs(self)->None:
        i:Neuron 
        for i in self.input_neurons:
            i.output = None


    def clear(self)->None:
        self.clear_outputs()
        self.clear_mids()
        self.clear_inputs()
    #================================================

    #getting layers 
    def get_layers(self)->List[List[Neuron]]:
        #output will be from input to output
        output:List[List[Neuron]] = []
        return [self.input_neurons]+self.mid_neurons+[self.output_neurons] 
    

    #getting connections ==============
    def get_connections_from_to(self, from_:Neuron, to_:Neuron)->List[Connection]:
        output:List[Connection] = []
        c:Connection
        for c in self.connections:
            if c.from_ == from_ and c.to_ == to_:
                output.append(c)
        return output


    def get_input_connections_of(self, target:Neuron)->List[Connection]:
        """
        A    C     B
        O -------->O

        A : C.from_
        B : C.to_

        C is is an input connection of B 
        C is is an output connection of A
        
        """
        output:List[Connection] = []
        c:Connection
        for c in self.connections:
            if c.to_ == target:
                output.append(c)
        return output
    

    def get_output_connections_of(self, target:Neuron)->List[Connection]:
        output:List[Connection] = []
        c:Connection
        for c in self.connections:
            if c.from_ == target:
                output.append(c)
        return output


    def predict(self, data_unit:DataUnit)->None:
    
            """
            pick the output from output neuron's output
            """
            #first clear the outputs
            self.clear()

            layer_type = List[Neuron]
            layer:List[Neuron]
            layers:List[layer_type] = self.get_layers()

            i:int
            for i in range(len(layers)):
                layer=layers[i]
                neuron:Neuron
                neuron_index:int 
                for neuron_index, neuron in enumerate(layer):
                    print(self)
                    input("====")
                    input_connections:List[Connection] = self.get_input_connections_of(neuron) 
                    output_connection:List[Connection] = self.get_output_connections_of(neuron)
                    is_input_neuron = input_connections.__len__() == 0
                    is_output_neuron = len(output_connection) == 0 
                    if is_input_neuron:
                        # loading data unit 
                        neuron.output = data_unit.inputs[neuron_index]
                    else:
                        c:Connection 
                        weighted_sum:float = 0.0
                        for c in input_connections:
                            from_:Neuron = c.from_
                            weight:float = c.weight
                            prodcut:float = weight * from_.output
                            weighted_sum += prodcut
                        neuron.output = neuron.activation_function(weighted_sum + neuron.bias)

                        #debugging


    def calc_neural_error(self, data_unit:DataUnit)-?float:
        output:List[float] = []
        pass
    
            




    




