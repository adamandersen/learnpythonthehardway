# import arguments only from sys
from sys import argv

# take argument from commandline
script, filename = argv;

# print some user information
print "We're going to erase %r." % filename;
print "If you don't want that, hit CTRL+C (^C).";
print "If you do want that, hit RETURN.";

# user choiese
raw_input("?");

# user information
print "Opening the file...";
# open the file given
target = open(filename, 'w');
# user information
print "Truncating the file. Goodbye!";
# empthy the content
target.truncate();
# user information
print "Now I'm going to ask you for three lines.";
# user input
line1 = raw_input("line 1: ");
line2 = raw_input("line 2: ");
line3 = raw_input("line 3: ");
# user information
print "I'm going to write these to the file.";
# write input to filename on each line
target.write(line1);
target.write("\n");
target.write(line2);
target.write("\n");
target.write(line3);
target.write("\n");
# user information
print "And finally, we close it"
# close the file so it won't corrupt the file new comment
target.close
