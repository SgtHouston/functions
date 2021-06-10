# Write a letter_histogram program that asks the user for input, 
# and prints a dictionary containing the tally of how many times 
# each letter in the alphabet was used in the word.
# For example Please enter a word: banana --> {'a': 3, 'b': 1, 'n': 2}

def letter_summary(word):
    
    dictionary = {}
    
    for letter in word:
        count = word.count(letter)
        dictionary[letter] = count
    return dictionary


word_input = input("Please enter a word: ")

print(letter_summary(word_input))

