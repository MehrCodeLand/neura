from typing import * 


def get(target:List[str])->int:
    max_line_length = 0
    i:str
    for i in target:
        if len(i) > max_line_length:
            max_line_length = len(i)
    return max_line_length