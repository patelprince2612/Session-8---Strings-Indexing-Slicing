# 4.
# Given a Flipkart product description string, write a Python script that extracts and 
# prints the first word, last word, and the total number of words using string methods split(), indexing, and len().


description = "Wireless Noise Cancelling Bluetooth Headphones with Mic Deep Bass"

# Split by spaces into a list of words
words = description.split()

first_word = words[0]
last_word = words[-1]
total_words = len(words)

print("First word:", first_word)
print("Last word:", last_word)
print("Total words:", total_words)

