from sys import argv

# take one argument in. Any text file
script, filename = argv;

# prompt format
prompt = '> '

# open the passed textfile
txt = open(filename);

# print the textfile name to the console
print "Here's your file %r:" % filename;

# read the open textfile and print the context in the console
print txt.read();

# user information
print "Type the filename again:";

# enter another textfile
file_again = raw_input(prompt);

# open the textfile
txt_again = open(file_again);

# print out the cached opened textfile
print txt_again.read();
