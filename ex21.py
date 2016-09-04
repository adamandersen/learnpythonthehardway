# function to addtion
def add(a, b):
    print "ADDING %d + %d" % (a, b);
    return a + b;

# function to subtract
def subtract(a, b):
    print "SUBSTRACTING %d - %d" % (a, b);
    return a - b;

# function to multiply
def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b);
    return a * b;

# function to divide
def divide(a, b):
    print "DIVIDING %d / %d" % (a, b);
    return a / b;

# user information
print "Let's do some math with just functions";
# use variables as function to do math
age = add(30, 5);
height = subtract(78, 4);
weight = multiply(90, 2);
iq = divide(100, 2);

print "Age: %d, Height: %d, Weight: %d" % (age, height, weight);


# A puzzel for the extra credit, tyoe in anyway
print "Here is a puzzle.";
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
print "That becomes: ", what, "Can you do it by hand?"
