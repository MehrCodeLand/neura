from typing import *


from Neuron import Neuron
from Connection import Connection


"fuck MIcrosoft"

class Network:
    def __init__(self):
        self.neurons:List[Neuron] = []
        self.connections:List[Connection] = []