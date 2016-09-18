# -*- coding: utf-8 -*-
animals = ['bear', 'tiger', 'penguin', 'zebra']

print animals[2]

for papkasse in animals:
    print papkasse


print """
Jeg har set en %s i Zoo. En %s så jeg i Knuttenborg Safaripark.
I madagasker er der en %s der hedder Martin.
Også kommmer de sejste %s altid for, at rede dagen""" % (animals[0], animals[1], animals[3], animals[2])
