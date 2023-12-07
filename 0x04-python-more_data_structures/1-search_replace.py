#!/usr/bin/python3
# 1-search_replaced.py
# Brennan D Baraban <375@holbertonschool.cm


def search_replace(my_list, search, replace):
"""Replce all occurances of an element by another in a new list."""
new_list = my list[:]
for i in range(len(new_list)):
if new_list[i] == search:
new_list[i] = replace
return (new_list)
