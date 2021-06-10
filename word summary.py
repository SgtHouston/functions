# Write a word_histogram program that asks the user for a sentence as 
# its input, and prints a dictionary containing the tally of how many 
# times each word in the alphabet was used in the text. 
# For example:Please enter a sentence: 
# To be or not to be {'to': 2, 'be': 2, 'or': 1, 'not': 1}

sentence_input = input("Please enter a sentence: ")

def letter_summary(sentence_input):
    dictionary = {}
    word_list = sentence_input.split()
    
    for word in word_list:
        count = word_list.count(word)
        dictionary[word] = count
    
    return dictionary




print(letter_summary(sentence_input))

