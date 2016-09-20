# -*- coding: utf-8 -*-
import ex40_mystuff as mystuff

mystuff.apple()
print mystuff.tangerine


# This is my class
class Song(object):

    # This is my inisiation, will create an empty object for me
    def __init__(self, lyrics):
        self.lyrics = lyrics

    # a function that loops through every line and prints it
    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

# fill up the object in the class Song with this variable
happy_bday = Song(["Happy birthday to you",
                    "I don't want to get sued",
                    "So I'll stop right there"])

# a different variable to fill up the object in Song class
bulls_on_parade = Song(["\nThey rally around tha family",
                        "With pocket full of shells"])

chrismax_song = Song(["\n\t*Last Chrismas",
                        "\t*I gave you my heart",
                        "\t*but the very next day",
                        "\t*You gave it away.\n"])
happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

chrismax_song.sing_me_a_song()
