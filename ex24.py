# -*- coding: utf-8 -*-

print "Let's practice everyhing.";
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.';

poem = """
\tThe lovely world
with logic so firmly planted
cannont discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
""";

print "-" * 40;
print poem;
print "-" * 40;

# math that gives equals 5
five = 10 - 2 + 3 -6;
# user information
print "This should be five: %s\n" % five;

# function that takes one argument
def secret_formula(started):
    jelly_beans = started * 500;
    jars = jelly_beans /  1000;
    crates = jars / 100;
    return jelly_beans, jars, crates;

# variable of 10000
start_point = 10000;
# variables is eq function, that takes in one argument
beans, jars, crates = secret_formula(start_point);

# user information
print "With a starting point of: %d" % start_point;
print "We'd have %d beans, %d jars, and %d crates.\n" % (beans, jars, crates);

# assign variable with new value
start_point = start_point / 10;

# user information
print "We can also do that this way:";
print "With a starting point of: %d" % start_point;
# call function to show with new values
print "We'd have %d bean, %d jars, and %d crates." % secret_formula(start_point);
