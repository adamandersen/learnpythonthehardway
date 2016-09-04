# -*- coding: utf-8 -*-
# import  arguments from sys
from sys import argv;

# take one argument
script, input_file = argv;

# function to print file
def print_all(f):
    print f.read();

def rewind(f):
    f.seek(0);

# print line number in console
def print_a_line(line_count, f):
    print "\n",line_count, f.readline();

# open user input file given.
current_file = open(input_file);

# user information
print "First let's print the whole file:\n";

# call function to print the entier file to console
print_all(current_file);

# user information
print "Now let's rewind, kind of like a tape."
rewind(current_file);

# user information
print "Let's print three lines:";

# variable to count line number, start count from 1
current_line = 1;



# variable to print line number + 1
# call function and pass arguments in directly
print_a_line(current_line, current_file);

current_line = current_line + 1;
print_a_line(current_line, current_file);

current_line = current_line + 1;
print_a_line(current_line, current_file);

current_line = current_line + 1;
print_a_line(current_line, current_file);
