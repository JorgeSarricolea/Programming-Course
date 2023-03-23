# Write a program with a function that receives a string of text and returns the longest word in the string.

def find_longest_word(text):
    """
    This function receives a string of text and returns the longest word in the string.
    """
    words = text.split()
    longest_word = ''
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word


# Example usage:
text = "To swing on spiral, of our divinity and still beeing a human"
longest_word = find_longest_word(text)
print("The longest word in the text is:", longest_word)
