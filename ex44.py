# -*- coding: utf-8 -*-
class Parent(object):

    def override(self):
        print "PARENT implicit()"

class Child(Parent):

    def override(self):
        #for self.somename in name():
        #    print somename

        print "CHILD override()"

dad = Parent()
son = Child()

#dad.implicit()
#son.implicit()

dad.override()
son.override()
