# imports the functions written in ex25.py
import ex25

# the sentence to use
sentence = "All good things come to those who wait.";

# break up all the words with split from function
words = ex25.break_words(sentence);
print words, "\n";

# sort the words alphabetic
sorted_words = ex25.sort_words(words);
print sorted_words, "\n";

# print first and last word still from split function
ex25.print_first_word(words);
ex25.print_last_word(words);
print words, "\n";

# print first and last word after sorted out
ex25.print_first_word(sorted_words);
ex25.print_last_word(sorted_words);
print sorted_words, "\n";

# prints the first and last unsorted and then sorted out_file
ex25.print_first_and_last(sentence);
ex25.print_first_and_last_sorted(sentence);

# shows the functions comment for help
help(ex25);
