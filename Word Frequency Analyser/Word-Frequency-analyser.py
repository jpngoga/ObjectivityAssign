
def count(elements):
	# check if each word has '.' at its last. If so then ignore '.'
	if elements[-1] == '.':
		elements = elements[0:len(elements) - 1]

	# if there exists a key as "elements" then simply
	# increase its value.
	if elements in dictionary:
		dictionary[elements] += 1

	# if the dictionary does not have the key as "elements"
	# then create a key "elements" and assign its value to 1.
	else:
		dictionary.update({elements: 1})


# driver input to check the program.

Sentence = "Apple Mango Orange Mango Guava Guava Mango apple mango apple orange  orange orange apple orange guava mango mango Banana Avocado Mango strawberry Mango Grape Orange Papaye Guava Guava Mango"

# Declare a dictionary
dictionary = {}

# split all the word of the string.
lst = Sentence.split()

# take each word from lst and pass it to the method count.
for elements in lst:
	count(elements)

# print the keys and its corresponding values.
for allKeys in dictionary:
	print ("Frequency of ", allKeys, end = " ")
	print (":", end = " ")
	print (dictionary[allKeys], end = " ")
	print()

