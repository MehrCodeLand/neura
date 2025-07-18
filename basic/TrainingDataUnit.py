from typing import * 




class TrainingDataUnit:
    def __init__(self, inputs:List[float], label:float):
        self.inputs:List[float] = inputs 
        self.label:float = label