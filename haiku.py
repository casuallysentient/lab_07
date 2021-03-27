def is_haiku(input_string):
    """
    Checks if input_string follows the syllabic and line structure of a haiku and outputs True if so.

    :param input_string: A string
    :return: True or False
    """
    pass


def haiku_string_parser(input_string):
    """
    --OPTIONAL--
    Formats a haiku single-line string into a multi-line, readable form if input_string is in fact a haiku.

    :param input_string: A single-line string representing a haiku's syllabic and line division.
    :return: A multi-line representation of input_string.
    """
    pass

def main():
    """
    Just some sample behavior based on the README. Feel free to try your own.
    """
    haiku_string = "clouds ,mur,mur ,dark,ly /it ,is ,a ,blin,ding ,ha,bit /ga,zing ,at ,the ,moon "
    if is_haiku(haiku_string) is not None and is_haiku(haiku_string):
        print("This is a valid haiku based on its structure.")
    elif is_haiku(haiku_string) is not None and not is_haiku(haiku_string):
        print("This is not a valid haiku based on its structure.")

    # formatted_haiku = haiku_string_parser(haiku_string)  # Optional
    # print(formatted_haiku)                               # Optional


# DO NOT WRITE CODE BELOW THIS LINE

if __name__ == '__main__':
    main()
