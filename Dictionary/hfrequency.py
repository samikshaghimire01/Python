# Write a function that takes a string as input and returns a dictionary where the keys are
#  the words in the string and the values are the frequencies of those words.

def word_frequency(text):
    words = text.split()
    freq_dict = {}
    
    for word in words:
        freq_dict[word] = freq_dict.get(word, 0) + 1
    
    return freq_dict

input_text = 'the quick brown fox jumps over the lazy dog'
print(word_frequency(input_text))