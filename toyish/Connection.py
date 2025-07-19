import random 

from Neuron import Neuron



class Connection:
  def __init__(self, from_:Neuron, to_:Neuron, weight=None):
    self.from_:Neuron = from_
    self.to_:Neuron = to_
    
    if weight is None:
      weight = random.random()
      
    self.weight = weight