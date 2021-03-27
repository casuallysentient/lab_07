def get_vowel_frequency(corpus):
    """
    Returns a list of frequency percentages for a corpus's vowels.

    :param corpus: Any valid Python string
    :return: List of frequency percentages
    """
    num_a = 0
    num_e = 0
    num_i = 0
    num_o = 0
    num_u = 0
    temp = ""
    for x in range(len(corpus)):
        if corpus[x].isalpha():
            temp = temp + corpus[x]
    corpus = temp
    for x in range(len(corpus)):
        if corpus[x] in ("a", "A"):
            num_a += 1
        elif corpus[x] in ("e", "E"):
            num_e += 1
        elif corpus[x] in ("i", "I"):
            num_i += 1
        elif corpus[x] in ("o", "O"):
            num_o += 1
        elif corpus[x] in ("u", "U"):
            num_u += 1
    a_frequency = round(((num_a / len(corpus)) * 100), 2)
    e_frequency = round(((num_e / len(corpus)) * 100), 2)
    i_frequency = round(((num_i / len(corpus)) * 100), 2)
    o_frequency = round(((num_o / len(corpus)) * 100), 2)
    u_frequency = round(((num_u / len(corpus)) * 100), 2)
    return [['a', a_frequency], ['e', e_frequency], ['i', i_frequency], ['o', o_frequency], ['u', u_frequency]]


def main():
    """
    Just some sample behavior based on the README. Feel free to try your own.
    """
    sample_text = "The French horn (since the 1930s known simply as the \"horn\" in professional music circles) is a brass instrument made of tubing wrapped into a coil with a flared bell. The double horn in F/Bb (technically a variety of German horn) is the horn most often used by players in professional orchestras and bands. A musician who plays a horn is known as a horn player or hornist."
    vowel_frequencies = get_vowel_frequency(sample_text)
    print(vowel_frequencies)


# DO NOT WRITE CODE BELOW THIS LINE


if __name__ == '__main__':
    main()
