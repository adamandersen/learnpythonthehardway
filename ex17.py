from sys import argv;
from os.path import exists;

script, from_file, to_file = argv;

# user information
#print "Copying from %s to %s" % (from_file, to_file);

# we could do these two on one line, how?
indata = open(from_file).read();


# user information
print "The input file is %d bytes long" % len(indata);
print "Does the output file exist? %r " % exists(to_file);
print "Ready, hit RETURN to continue, CTRL+C to abort.";
# user input
raw_input();

# write file
out_file = open(to_file, 'w');
out_file.write(indata);

# user information
print "Alright, all done.";

# clsoe all opened files
out_file.close();
in_file.close();
