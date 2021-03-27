def get_file_contents(file_path):
    """
    Reads the contents of a single-line txt file.

    :param file_path: A string representing the path of the file
    :return: A string containing the contents of the file
    """
    file = open(file_path, 'r')
    new_sequence = file.read()
    file.close()
    return new_sequence


def update_frequencies(old_frequencies, new_sequence):
    """
    Updates a list of nucleotide frequencies to reflect the addition of a new sequence's nucleotides.

    :param old_frequencies: A list of frequency tuples
    :param new_sequence: A string representing a DNA sequence
    :return: An updated list of frequency tuples
    """
    num_a = old_frequencies[0][1]
    num_c = old_frequencies[1][1]
    num_t = old_frequencies[2][1]
    num_g = old_frequencies[3][1]
    for x in range(len(new_sequence)):
        if new_sequence[x] == "A":
            num_a += 1
        elif new_sequence[x] == "C":
            num_c += 1
        elif new_sequence[x] == "T":
            num_t += 1
        elif new_sequence[x] == "G":
            num_g += 1
    return [('A', num_a), ('C', num_c), ('T', num_t), ('G', num_g)]


def main():
    """
    Just some sample behavior based on the README. Feel free to try your own.
    """
    old_frequencies = [("A", 20), ("C", 23), ("T", 125), ("G", 4)]
    # new_sequence = "ACCCGTTA"
    new_sequence = get_file_contents("dna_sequence.txt")
    new_frequencies = update_frequencies(old_frequencies, new_sequence)

    print(new_frequencies)


# DO NOT WRITE CODE BELOW THIS LINE


if __name__ == '__main__':
    main()
