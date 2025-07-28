
from typing import * 


class DataUnit:
    def __init__(self, inputs:List[float], expected_outs:List[float]):
        self.inputs:List[float] = inputs
        self.expected_outs:List[float] = expected_outs