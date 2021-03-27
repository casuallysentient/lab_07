def shuffle_create(original_list):
    """
    Creates and returns a list with original_list's elements shuffled in any pseudo-random order.

    :param original_list: A list of elements
    :return output_list: A list of the original elements shuffled
    """
    pass


def shuffle_in_place(original_list):
    """
    Shuffles original_list's contents in-place.

    :param original_list: A list of elements
    :return: None
    """
    pass


def main():
    """
    Just some sample behavior based on the README. Feel free to try your own.
    """
    list_one = ["Camille Saint-Saëns", "Antonín Dvořák", "Alexander Borodin", "Bedřich Smetana", "Maurice Ravel"]
    print("ORIGINAL LIST_ONE: {}".format(list_one))

    # First function execution
    print("LIST CREATED BY SHUFFLE_CREATE: {}\n".format(shuffle_create(list_one)))

    list_two = ["A", 0, 0, 5, 1, 3, 2]
    print("ORIGINAL LIST_TWO: {}".format(list_two))

    # Second function execution
    shuffle_in_place(list_two)
    print("LIST_TWO AFTER SHUFFLE_IN_PLACE: {}".format(list_two))


# DO NOT WRITE CODE BELOW THIS LINE


if __name__ == '__main__':
    main()
