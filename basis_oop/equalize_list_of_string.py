
from typing import * 

import get_max_line_len


def equalize(target:List[str], padding_char=" ")->None:
    max_line_length = get_max_line_len.get(target=target)
    for i in range(len(target)):
        len_diff = max_line_length-len(target[i])
        target[i] += padding_char * len_diff
    
