import colours as c

def main():
    colours = c.colour_table()
    reds =  c.find_cols("red", colours)
    print("average red: %s" % str(c.average_rgb(reds)))

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()
