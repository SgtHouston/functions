# Write a letter_histogram program that asks the user for input, 
# and prints a dictionary containing the tally of how many times 
# each letter in the alphabet was used in the word.
# For example Please enter a word: banana --> {'a': 3, 'b': 1, 'n': 2}


def letter_histogram(word):
    letter_count_dict = {}
    
    for letter in word:
        letter_count_dict[letter] += 1
    print(letter_count_dict)


letter_histogram("banana")
print(letter_histogram("banana"))

