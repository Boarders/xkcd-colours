from .rgb import *


def find_cols(col_name : str, ct : dict[str, RGB]) -> dict[str, RGB]:
    """
    Find the subdictionary with the given name as a substring
    """
    return {col : rgb for col, rgb in ct.items() if col_name in col}

def average_rgb(ct : dict[str, RGB]) -> RGB:
    """
    Function which finds the average rgb value from a colour table
    >>> str(average_rgb({"c1": RGB(1,1,1), "c2": RGB(3,3,3)}))
    '(2, 2, 2)'
    """
    average = RGB(0,0,0)
    num = 0
    for col, rgb in ct.items():
        average += rgb
        num += 1
    return RGB(average.r / num, average.g / num, average.b / num)
        
        
if __name__ == "__main__":
    import doctest
    doctest.testmod()
