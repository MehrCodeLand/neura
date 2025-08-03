import random 

from Neuron import Neuron


class Connection:
    def __init__(self, from_:Neuron, to_:Neuron):
        self.from_:Neuron = from_
        self.to_:Neuron = to_
        self.weight:float = random.random()


    def __str__(self)->str:
        return f"<{self.from_.title} {self.to_.title} {self.weight}>"