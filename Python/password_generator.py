# Use an import statement at the top
import random

word_file = "words.txt"
word_list = []

#fill up the word_list
with open(word_file,'r') as words:
	for line in words:
		# remove white space and make everything lowercase
		word = line.strip().lower()
		# don't include words that are too long or too short
		if 3 < len(word) < 8:
			word_list.append(word)

# Add your function generate_password here
# It should return a string consisting of three random words 
# concatenated together without spaces
def generate_password():
    result_list = []
    password = ''
    while (len(result_list) < 3):
        result_list.append(word_list.pop(random.randint(0, len(word_list) - 1)))
    for word in result_list:
        password += word
    return password


# test your function
print(generate_password())