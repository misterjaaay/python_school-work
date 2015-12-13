#!/usr/bin/python
# coding: utf-8

string = '1486371'
even = ""
odd = ""

for i in string:
	if int(i) % 2 == 0:
		even += i
	else:
		odd += i
		
odd = sorted(odd)
even = sorted(even)
change_string = "".join(odd+even[::-1] )

print change_string
