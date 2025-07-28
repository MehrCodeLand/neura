


class Neuron:
    def __init__(self, title:str):
        self.title = title
        self.output = None
        self.bias = 0

    def __str__(self)->str:
        return f"<{self.title};o:{self.output};b:{self.bias}>"
    
    
        