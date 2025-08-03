



class Neuron:
    def __init__(self, title:str):
        self.title = title
        self.output = None
        self.bias = 0
        self.activation_function = activation_sigmoid

    def __str__(self)->str:
        return f"<{self.title};{self.output}>"
    
    
        