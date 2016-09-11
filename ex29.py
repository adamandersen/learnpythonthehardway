# set variables
people = 24;
cars = 25;
trucks = 26;

# if cars is more than pepole do
if cars > people:
    print "We should take the cars.";
# if cars is less then people do
elif cars < people:
    print "We should not take the cars.";

#if trucks has value grass then cars do
if trucks > cars:
    print "That's too many trucks.";
# if trucks is less then do
elif trucks < cars:
    print "Maybe we could take the trucks.";
# if no conditions meet do
else:
    print "We still can't decide.";

# if people is greater then do
if people > trucks:
    print "Alright, let's just take the trucks.";
else:
    print "Fine, lets's stay home then."
