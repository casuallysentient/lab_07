def get_file_contents(file_path):
    """
    Reads the contents of a single-line txt file.

    :param file_path: A string representing the path of the file
    :return: A string containing the contents of the file
    """
    pass


def update_frequencies(old_frequencies, new_sequence):
    """
    Updates a list of nucleotide frequencies to reflect the addition of a new sequence's nucleotides.

    :param old_frequencies: A list of frequency tuples
    :param new_sequence: A string representing a DNA sequence
    :return: An updated list of frequency tuples
    """
    pass


def main():
    """
    Just some sample behavior based on the README. Feel free to try your own.
    """
    old_frequencies = [("A", 20), ("C", 23), ("T", 125), ("G", 4)]
    # new_sequence = "ACCCGTTA"
    new_sequence = get_file_contents(DNA_FILE_NAME)
    new_frequencies = update_frequencies(old_frequencies, new_sequence)

    print(new_frequencies)


# DO NOT WRITE CODE BELOW THIS LINE


if __name__ == '__main__':
    main()
