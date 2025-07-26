import random 


class Connection:
    def __init__(self, from_, to_):
        self.from_ = from_
        self.to_ = to_
        self.weight = random.random()