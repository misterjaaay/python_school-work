#!/usr/bin/python
# coding: utf-8

a = 'sabrrtuwacaddabra'
prev = ""
next = ""

for prev in a:
	for next in a:
		if prev <= next:
			print prev


