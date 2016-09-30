 ## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
     pass

## is-a object
class Dog(Animal):

    def __init__(self, name):
        ## ??
        self.name = name

## is-a object
class Cat(Animal):

    def __init__(self, name):
        ## ??
        self.name = name

## is-a object
class Person(object):

    def __init__(self, name):
        ## ??
        self.name = name

        ## has-a pet of some kind
        self.pet = None

## is-a object
class Employee(Person):

    def __init__(self, name, salary):
        ## is-a object of name
        super(Employee, self).__init__(name)
        ## has-a salary
        self.salary = salary

## is-a object
class Fish(object):
    pass

## is-a object
class Salmon(Fish):
    pass

## is-a object
class Halibut(Fish):
    pass

## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")

## has-a pet satan
mary.pet = satan

## is-a Employee
frank = Employee("Frank", 120000)

## has-a pet rover
frank.pet = rover

## is-a
flipper = Fish()

## ??
crouse = Salmon()

## has-a Halibut
harry = Halibut()
