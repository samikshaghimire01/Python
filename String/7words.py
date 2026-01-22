# Write a function that takes a string as input and returns a list of all the words in the 
# string that are longer than 5 characters. While returning the words, alternately capitalize the letters.

def alternate_capitalize_long_words(sentence):
    
    words = sentence.split()
    long_words = [word for word in words if len(word) > 5]
    
    # Function
    def alt_capitalize(word):
        result = ""
        for i, char in enumerate(word):
            if i % 2 == 0:
                result += char.upper()
            else:
                result += char.lower()
        return result
    
    
    return [alt_capitalize(word) for word in long_words]

text = "Python programming language is powerful and versatile"
print(alternate_capitalize_long_words(text))
