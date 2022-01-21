import json
from colours.rgb import RGB

def hex_to_rgb(s : str) -> RGB:
    """
    Takes a hex rgb string and returns the rbg values as a tuple.
    >>> hex_to_rgb("#132ada")
    (19, 42, 218)
    """
    s = s.lstrip("#")
    return RGB(int(s[:2], 16), int(s[2:4], 16), int(s[4:6], 16))



def colour_table() -> dict[str, RGB]:
    """Create a colour table from colour json file
    """
    # taken from allison parrish talk
    colors = dict()    
    with open("xkcd.json", 'r') as json_file:
        colors_json = json.loads(json_file.read())
    for item in colors_json['colors']:
        colors[item["color"]] = hex_to_rgb(item["hex"])
    return colors

if __name__ == "__main__":
    import doctest
    doctest.testmod()
