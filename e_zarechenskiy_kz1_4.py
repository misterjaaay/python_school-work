#!/usr/bin/python
# coding: utf-8

var_string = 'wowhatamanwowowowpalehche'
index = 1
count = 0
template = 'wow'
while index != -1:
    index = var_string.find(template)
    if index >= 0:
        count += 1
    var_string = var_string[index+1:]
print count
