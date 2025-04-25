from typing import Union

class Why(Exception):
    pass

def divide(str_with_ints: str) -> Union[float, str]:
    """
    Returns the result of dividing two numbers or an error message.
    :arg
        str_with_ints: str, ex. "4 2";
    :return
        result of dividing: float, ex. 2.0 (4 / 2 = 2.0);
        error response in "Error code: {error message}: str;
    """
    if len(str_with_ints.split()) != 2:
        raise Why('There should be two numbers')
    if str_with_ints.split()[1] == '0':
        raise Why('division by zero')
    for string in str_with_ints.split():
        if not string.isdigit():
            raise Why(f'invalid literal for int() with base 10: \'{string}\'')
    return int(str_with_ints.split()[0]) / int(str_with_ints.split()[1])