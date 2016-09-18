# create a mapping of state to abbreviation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'Californina': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# create a basic set of states and some cities in them
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

# add some more citiies
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print '-' * 30
print "NY State has: ", cities['NY']
print "OR State has: ", cities['OR']

# print some states
print '-' * 30
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbreviation is: ", states['Florida']

# do it by using the state then cities dict
print '-' * 30
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]

# print every state abbreviation
print '-' * 30
for state, abbrev in states.items():
    print "%s is abbreviated %s" % (state, abbrev)
