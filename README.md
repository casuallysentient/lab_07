## CS-UY 1114 — Lab 7
# Lists, Tuples, and File Input
#### Friday, March 26th, 2021

All lab work must be submitted within 24 hours of the start of your lab period on Gradescope (we will be checking this
using the timestamps of your last submission on Gradescope). This, of course, also means that if you submit a solution
before your allotted lab time, you will get no credit. You must try each problem at least once (that is, submitting at
least one attempt to Gradescope, whether it is correct or not). You are welcome to continue to work on the problems and
continue submitting to Gradescope until you are satisfied with your results. It is your responsibility to remember to
submit your work.

Please note that your overall point value is awarded by the teaching assistants verifying that you attempted and
submitted each problem at least once! For every hour that your work is late on Gradescope, we will deduct 0.5 points
from the total 10-point value of the lab.

Remember that the points awarded by the autograder will not count towards your lab's final grade and will be removed
when the final grades are calculated.
---

### Important Note on Lab Collaboration

While discussion of the lab problems is allowed amongst students in the course, when it is time to implement your
solution, the code must be **entirely** your own work. Submitting code that has been written by someone other than
yourself will, at a minimum, result in receiving a 0 on the lab assignment. Other possible penalties include having
the incident reported to the Office of Student Affairs to be added to your official academic record and/or failing the
course.

---

### Congrats on getting through the first midterm!

I hope everyone was able to do their best on the midterm this week (and even if you feel like you didn't, congrats on
surviving it anyway)! The first midterm covered a lot of the core principles of programming that give beginners trouble
(I certainly had trouble with them), and as such, making it through it is an achievement in and of itself.

From this point forward, we'll be covering concepts that start to tie programming in with more real-world problems, and
so it will start getting more interesting (in my opinion, anyway). As always, we are on standby should you need any
help. Don't hesitate to ask; the second midterm will come faster than you think. Good luck!

— Sebastián.

---

### Problem 1: Vowel Frequency

Your first task is to generate a list that will contain the frequency (as a percentage) of each of the 5
vowels (i.e. `a`, `e`, `i`, `o`, and `u`) in a string. Your function, **`get_vowel_frequency()`** (file:
[**vowel_frequency.py**](vowel_frequency.py)), will accept that string as its single parameter, and return a **list of
lists** in the following format:

```python
[['a', a_freq_percentage], ['e', e_freq_percentage], ['i', i_freq_percentage], ['o', o_freq_percentage], ['u', u_freq_percentage]]
```

Here's an example:
```python
def main():
   sample_text = "Do you hear the people sing?"
   vowel_frequencies = get_vowel_frequency(sample_text)
   print(vowel_frequencies)

main()
```
Output:
```text
[['a', 4.55], ['e', 18.18], ['i', 4.55], ['o', 13.64], ['u', 4.55]]
```

That is, **`a`** makes up 4.55% of the _**characters**_ in `sample_text`, **`e`** makes up 18.18%, etc.

As you can see, we rounded the percentages to the second decimal place. Please do the same using the
[**round**](https://docs.python.org/3/library/functions.html#round) function!

By the way, you may ***not*** assume that the input text will contain any the five vowels, so make sure to
account for that possibility!

### Problem 2: Nucleotide Arithmetic

Remember our good ole friend, the DNA sequence? In this case we want to create a function named **`update_frequencies()`**,
that will accept two parameters arguments.  One parameter is a list of existing frequency counts for nucleotides. The
second parameter is a string representing a DNA sequence. The function will update the previous nucleotide frequency
counts based on the occurrence of the nucleotides in the string value passed to `update_frequencies()`. Consider the
following code:

```python
def main():
   old_frequencies = [("A", 20), ("C", 23), ("T", 125), ("G", 4)]
   new_sequence = "ACCCGTTA"
   new_frequencies = update_frequencies(old_frequencies, new_sequence)

   print(new_frequencies)

main()
```
The code displayed in the `main()` function will result in the following output (a list of **tuples**):
```text
[('A', 22), ('C', 26), ('T', 127), ('G', 5)]
```

I suggest making sure that you get `update_frequencies()` working to these standards before moving on to the next step!

Let's go a step further with this program. Let's say we have a file called [**dna_sequence.txt**](dna_sequence.txt)
that has the following content:

```text
TAATATCACATCATTAGACACTAATTGCCTCTGCCAAAATTCTGTCCACAAGCGTTTTAGTTCGCCCCAGTAAAGTTGTCAATAACGACCACCAAATCCGCATGTTACGGGACTTCTT
ATTAATTCTTTTTTCGTGGGGAGCAGCGGATCTTAATGGATGGCGCCAGGTGGTATGGAAGCTAATAGCGCGGGTGAGAGGGTAATCAGCCGTCTCCACCAACACAACGCTATCGGGT
CATACTATAAGATTCCGCAATGCGACTACTTATAAGATGCCTTAACGGTATCCGCAACTTGCGATGTGCCTGCTATGCTTAAATGCATATCTCGCCCAGTAGCTTTCCAATATGAGAG
CATCAATTGTAGATCGGGCCGGGATAATCATGTCGTCACGGAACTTACTGTAAGAGTAATAATTTAAAAGAGATGTCGGTTTGCTGGTTCACGTAAAGGTCCCTCGCGCTACCTCTAA
GTAAGTGAGCGGTCGTGACATTATCCCTGATTTTCTCACTACTATTAGTACTCACGGCGCAATTCCACCACAGCCTTGTCTCGCCAGAATGCCAGTCAGCATAAGGAAGAGCTCAAGG
CAGGTCAACTCGCACTGTGAGGGTCACATGGGCGTTCGGCACTACCGACACGAACCTCAGTTAGCGTACATCCTACCAGAGGTCTGTGGCCCCGTGGTCAAAAGTGCGGGTTTCGTAT
TTGCTGCTCGTCAGTACTTTCAGAATCATGACCTGCACGGCAAAGAGACGCTTATTATGGAGCTCGACATGGCAATAACGCGACGAATCTACGTCACGACGAGAATAGTGTAAACGAA
GCTGCTGACGGCGGAAGCGTCAAAGGGGTCTGTGAATTGTTATTCGCGAAAAACATCCGTCCCCGTGGGGGATAGTCACCGACGCCGTTTTATAGAAGCCTAGGGGAACAGGTTGGTT
TAACTAGCTTAAGAAAGTAAATTCTGGGATTATACTGTAGTAATCACTAATTTACG
```

That is, it contains a **single line** of nucleotides. Create a second function, **`get_file_contents()`**, that will:

1. Accept the name of the file in string form as a parameter.
2. Open the file and read its contents into a string.
3. Close the file.
4. Return the string of nucleotides.

Utilizing `get_file_contents()` we can modify our earlier code to look and behave as follows:

```python
def main():
   old_frequencies = [("A", 20), ("C", 23), ("T", 125), ("G", 4)]
   new_sequence = get_file_contents("dna_sequence.txt")
   new_frequencies = update_frequencies(old_frequencies, new_sequence)

   print(new_frequencies)

main()
```
Output:
```text
[('A', 290), ('C', 256), ('T', 382), ('G', 244)]
```

You may assume that the list of old frequencies will follow the exact format and nucleotide/frequency pairings will
always follow the same ordering. Write your functions in the file [**update_frequencies.py**](update_frequencies.py).

### Problem 3: Now you're doing the CS student shuffle.

We'll continue with a question from pedagogical programming's great canon: the list shuffle. In the file
[**shuffling_lists.py**](shuffling_lists.py), create two simple functions.

1. The first, **`shuffle_create()`**, will accept one list parameter and return a **new list** with the same elements
from the list that was passed in, but shuffled in any random order.
2. The second, **`shuffle_in_place()`**, will accept one list parameter and shuffle its elements in-place (that is, the
function does not create a new list) in any random order.

For example, let's say you have the following two lists:

```python
list_one = ["Camille Saint-Saëns", "Antonín Dvořák", "Alexander Borodin", "Bedřich Smetana", "Maurice Ravel"]
list_two = ["A", 0, 0, 5, 1, 3, 2]
```

We would like to shuffle `list_one` by **creating** a new list, and shuffle `list_two` by shuffling the
elements **in the original list**.

Consider the following code:

```python
def main():
   list_one = ["Camille Saint-Saëns", "Antonín Dvořák", "Alexander Borodin", "Bedřich Smetana", "Maurice Ravel"]
   print("ORIGINAL LIST_ONE: {}".format(list_one))

   # First function execution; notice that shuffle_create() is returning a new list
   print("LIST CREATED BY SHUFFLE_CREATE: {}\n".format(shuffle_create(list_one)))

   list_two = ["A", 0, 0, 5, 1, 3, 2]
   print("ORIGINAL LIST_TWO: {}".format(list_two))

   # Second function execution
   shuffle_in_place(list_two)  # notice that shuffle_in_place() is not returning anything
   print("LIST_TWO AFTER SHUFFLE_IN_PLACE: {}".format(list_two))

main()
```
A possible output (since the behavior is pseudo-random):

```text
ORIGINAL LIST_ONE: ['Camille Saint-Saëns', 'Antonín Dvořák', 'Alexander Borodin', 'Bedřich Smetana', 'Maurice Ravel']
LIST CREATED BY SHUFFLE_CREATE: ['Maurice Ravel', 'Camille Saint-Saëns', 'Alexander Borodin', 'Antonín Dvořák', 'Bedřich Smetana']

ORIGINAL LIST_TWO: ['A', 0, 0, 5, 1, 3, 2]
LIST_TWO AFTER SHUFFLE_IN_PLACE: [0, 1, 2, 'A', 5, 3, 0]
```

Some explanation as to what qualifies as a "shuffle" is probably in order. For **`shuffle_create()`**, use the
**`random`** module’s functions such as **`randrange()`**/**`randint()`** and `list` methods such as **`pop()`**, and
**`append()`**. These methods and function will be useful for  taking elements randomly from your original list, and
adding them to your new list, which should initially be empty.

For shuffling in place, it's worth clarifying what in-place actually _means_. We're not creating a new list, but rather
editing the original list. In other words, we're replacing the element at index _**i**_ with the element at index
_**j**_. Think about how to achieve this until none of the elements from the original list are in their original
location.

Hopefully, this goes without saying, but you should _**not**_ use the **`shuffle()`** function from the **`random`**
module. If you do, ***you will not receive credit for this problem***, as it literally does all the work for you, and
therefore does not count as an attempt. The **`sample()`** function is also not permitted in your solution.

In general, if we ask a question in a homework assignment, lab, or exam that can be solved
by making one or two calls to functions that already belong to a module, you can assume that we want you to write them
yourselves. If you're ever in doubt, please please please ask!

### Problem 4: Of Code And Poetry

Haiku are poems that follow a 5-7-5 syllabic structure. That is, the first line contains 5 syllables, the second
contains 7 syllables, and the last contains 5 syllables:

> Clouds murmur darkly
>
> it is a blinding habit—
>
> gazing at the moon

— _Basho_.

The first sentence can be broken down into five syllables (`clouds` + `mur` + `mur` + `dark` + `ly` = 5 syllables), the
second sentence into 7 (`it` + `is` + `a` + `blind` + `ing` + `ha` + `bit` = 7 syllables), and the last into 5
(`ga` + `zing` + `at` + `the` + `moon` = 5 syllables).

Write a function, **`is_haiku()`**, that returns the `bool` **`True`** if an input string is a haiku, or the `bool`
**`False`** if it is not. The function accepts one parameter, **`input_string`**, which has  the following format:

```python
sample_input_string = "clouds ,mur,mur ,dark,ly /it ,is ,a ,blin,ding ,ha,bit /ga,zing ,at ,the ,moon "
```

As you can see, syllables are separated by commas (**`,`**), and lines are separated by forward-slashes (**`/`)**.
Notice that the final syllables of each word contain an extra space (e.g. `"clouds "`). The function **`is_haiku`**
will return **`True`** if and only if:

1. The haiku contains 3 lines.
2. The first line contains 5 syllables.
3. The second line contains 7 syllables.
4. The third line contains 5 syllables.

Consider the sample executions below and feel free to try your own:

```python
print(is_haiku("clouds ,mur,mur ,dark,ly/it ,is ,a ,blin,ding ,ha,bit/ga,zing ,at ,the ,moon "))  # prints ‘True’

print(is_haiku("clouds ,mur,mur ,dark,ly/it ,is ,a ,blin,ding ,ha,bit/ga,zing "))  # prints ‘False’
```

Write your function in the file [**haiku.py**](haiku.py).

**HINT**: While there are multiple ways to approach this problem, the string method **`split()`** may be particularly
useful. See its official documentation [**here**](https://docs.python.org/3/library/stdtypes.html#str.split) if you
need a refresher.

### Problem 5 (Optional): Now, let's make it presentable

Write a function, **`haiku_string_parser()`**, that takes in one parameter, **`input_string`**, checks if it is a haiku
based on its structure and returns a reformatted, easy-to-read string. Consider the following program and the output
give that `haiku_string` has been assigned a valid haiku:

```python
def main():
   haiku_string = "clouds ,mur,mur ,dark,ly /it ,is ,a ,blin,ding ,ha,bit /ga,zing ,at ,the ,moon "
   formatted_haiku = haiku_string_parser(haiku_string)
   print(formatted_haiku)

main()
```
Output:
```text
clouds murmur darkly
it is a blinding habit
gazing at the moon
```

If **`input_string`** is not a haiku based on its structure, then **`haiku_string_parser()`** will simply return an
empty string (you don’t _have_ to use the **`is_haiku()`** function from problem 4 to do this, but it’d be a lot cooler
if you
did). This function should also be written inside the file [**haiku.py**](haiku.py).

**HINTS:**

- In order to create a line-break (newline) in a string, you can use the **`\n`** character.
- You might also want to consider using the string method **`join()`**. See
[**here**](https://docs.python.org/3/library/stdtypes.html#str.join).
- You may also want to keep in mind that the original, un-parsed string includes spaces after every last syllable of a
word. While this space is necessary to separate words in the same line, it should not be included in the _last word_ of
each line.
