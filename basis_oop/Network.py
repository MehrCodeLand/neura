

from Connection import Connection
from Neuron import Neuron


class Network:
    def __init__(self):
        self.neurons:Dict[str, Neuron] = {}
        self.connections = []
        self.data_set = []



def get_input_neurons(network:Network)->List[Neuron]:
    """
    inoput neuron is a neuron which has no incoming connection
    """
    for n in network.neurons: 
        n #the current neuron being processed
        c:int = 0 #incoming connection count
        i:Connection
        for i in network.connections:
            if i.to_ == n
