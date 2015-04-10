# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 20:18:33 2015

@author: root
"""

import random

print ("Wybierz liczbe z zakresu 1-100")
print ("zadaniem komputera bedzie odgadniecie jaka to liczba")

moja = int (input("Podaj liczbe "))
y = 0
c = 1
lista = 0
d = 100
while y != moja:
	y = random.randint(c,d)
	print ("liczba kompa: ",y)
	lista += 1
	if y > moja:
		print ("za duzo")
		d = y
		print ("przedzial: ",c,d)
	elif y < moja:
		print ("za malo")
		c = y
		print ("przedzial: ",c,d)
	else:
		print ("znalazlem")
		print ("moja = ",moja)
		print ("Kompa = ",y)
		print ("w tylu ruchach znalazles: ",lista)
