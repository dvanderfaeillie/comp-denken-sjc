#!/usr/bin/python
# -*- coding: utf-8 -*-

jongens = ['Ronar', 'Tiago', 'Uriel', 'Lars', 'Jules', 'Alec', 'Niels', 'Stan', 'Klaas', 'Iben', 'Timoer', 'Matteo', 'Mahmed', 'Louis', 'Thor', 'Boy', 'Ruben', 'Sem', 'Robin', 'Louis', 'Rik', 'Jarre', 'Lode', 'Nils', 'Simon', 'Jules', 'Noah', 'Wout', 'Igor', 'Lukas', 'Senne', 'Jef', 'Ward', 'Ryan', 'Stephan', 'Ali', 'Falco', 'Jean', 'Seppe', 'Louis', 'Louis', 'Elias', 'Jayson', 'Noah', 'Tom', 'Jaro', 'Silas', 'Maxime', 'Dylan', 'Leandro', 'Maxime', 'Reinoud', 'Roeland', 'Artuur', 'Andreas', 'Michiel', 'Robbe', 'Louis', 'Mauro', 'Kenzo', 'Tristan', 'Matteo', 'Rein', 'Tiemo', 'Bram', 'Mano', 'Tibo', 'Louis', 'Matteo', 'Tijl', 'Arne', 'Merlijn', 'Jarne', 'Michiel', 'Mats', 'Finn', 'Lennert', 'Adam', 'Wout', 'Henry', 'Viktor', 'Adil', 'Yannick', 'Arno', 'Arne', 'Henri', 'Tibo', 'Cédric', 'Jules', 'Lennert', 'Stan', 'Robin', 'Brent', 'Jelle', 'Roan', 'Lucas', 'Gedéon', 'Austin', 'León', 'Elias', 'Gaspard', 'Isaak', 'Eliot']

voornaam = str(input( 'Geef een voornaam in: ' ))
score = jongens.count(voornaam)
voornaam = str(input( 'Geef een voornaam in: ' ))
score = score + jongens.count(voornaam)
voornaam = str(input( 'Geef een voornaam in: ' ))
score = score + jongens.count(voornaam)

print() #generator.py hack
print( score )
