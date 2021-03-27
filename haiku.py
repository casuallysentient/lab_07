def is_haiku(input_string):
    """
    Checks if input_string follows the syllabic and line structure of a haiku and outputs True if so.

    :param input_string: A string
    :return: True or False
    """
    split_lines = input_string.split("/")
    if len(split_lines) == 3:
        line_1 = split_lines[0]
        words_1 = line_1.split(',')
        line_2 = split_lines[1]
        words_2 = line_2.split(',')
        line_3 = split_lines[2]
        words_3 = line_3.split(',')
        if len(words_1) == 5 and len(words_2) == 7 and len(words_3) == 5:
            return True
    return False


def haiku_string_parser(input_string):
    """
    --OPTIONAL--
    Formats a haiku single-line string into a multi-line, readable form if input_string is in fact a haiku.

    :param input_string: A single-line string representing a haiku's syllabic and line division.
    :return: A multi-line representation of input_string.
    """
    split_lines = input_string.split("/")
    if len(split_lines) == 3:
        line_1 = split_lines[0]
        words_1 = line_1.split(',')
        line_2 = split_lines[1]
        words_2 = line_2.split(',')
        line_3 = split_lines[2]
        words_3 = line_3.split(',')
        if len(words_1) == 5 and len(words_2) == 7 and len(words_3) == 5:
            return ("".join(words_1)).rstrip() + "\n" + ("".join(words_2)).rstrip() + "\n" + ("".join(words_3)).rstrip()
    return ""


def main():
    """
    Just some sample behavior based on the README. Feel free to try your own.
    """
    haiku_string = "clouds ,mur,mur ,dark,ly /it ,is ,a ,blin,ding ,ha,bit /ga,zing ,at ,the ,moon "
    if is_haiku(haiku_string) is not None and is_haiku(haiku_string):
        print("This is a valid haiku based on its structure.")
    elif is_haiku(haiku_string) is not None and not is_haiku(haiku_string):
        print("This is not a valid haiku based on its structure.")

    formatted_haiku = haiku_string_parser(haiku_string)  # Optional
    print(formatted_haiku)                               # Optional


# DO NOT WRITE CODE BELOW THIS LINE

if __name__ == '__main__':
    main()
