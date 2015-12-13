#!/usr/bin/python
# coding: utf-8
text = raw_input("Type any text here to find palindromes: ")
raw_text = text
total = 0
pattern = ",.:;!?"

text = text.lower().translate(None, pattern).split()

for x in raw_text:
	if x == x[::-1]:
		total += 1
print "The number of palindromes in string '%s' is: %s" % (raw_text, total)
	

