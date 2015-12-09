#!/usr/bin/python
# coding: utf-8
vowels = 'aeiou'
var_string = raw_input("Enter any word or phrase in English:")
total = 0
for vowel in vowels:
	total += var_string.lower().count(vowel)
print "Total count of vowels in %s is %d" % (var_string, total)

