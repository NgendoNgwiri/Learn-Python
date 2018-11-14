#!/bin/python
import random #generating Random numbers
import sys #operating system
import os #operating system

#you cant edit tuples files, it is a fixed entry
cities =("Nairobi","Mombasa","Kisumu")
Numbers =(10,35,22,45,74)
print(cities)
print(Numbers)

new_cities =list(cities)
print(new_cities)
new_cities.append("Nyeri")
new_cities.append ("Nakuru")
#convert a list to a tuple
Cities=tuple(new_cities)
print(cities)
print(new_cities)

