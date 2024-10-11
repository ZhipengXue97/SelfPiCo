# Extracted from https://stackoverflow.com/questions/4289331/how-to-extract-numbers-from-a-string-in-python
def get_first_nbr_from_str(input_str):
    '''
    :param input_str: strings that contains digit and words
    :return: the number extracted from the input_str
    demo:
    'ab324.23.123xyz': 324.23
    '.5abc44': 0.5
    '''
    if not input_str and not isinstance(input_str, str):
        return 0
    out_number = ''
    for ele in input_str:
        if (ele == '.' and '.' not in out_number) or ele.isdigit():
            out_number += ele
        elif out_number:
            break
    return float(out_number)

