#!/usr/bin/python
# coding: utf-8

var_string = 'wowhatamanwowowowpalehche'
ind = 1
count = 0
template = 'wow'
while ind != -1:
    ind = var_string.find(template)
    if ind >= 0:
        count += 1
    var_string = var_string[ind+1:]
print count
