import random


"""You’ll need to make a class that works like this:

it is instantiated with a path to a file on disk that contains words, one word per line

it reads that file, and makes an attribute of a list of those words
it prints out “[num-of-words-read] words read”
(it doesn't need to do all of this directly in the __init__ method; it might be a good idea for the __init__ method to call other functions to do some of this.)

it provides a method, random(), which returns a random word from that list of words

Note: the random method should not re-read the list of words each time; it should work with the already-read-in list of words.

For example, assume you have a file at /Users/student/words.txt that looks like this:

cat
dog
porcupine"""

class WordFinder:
    """Word Finder: finds random words from a dictionary."""
    def __init__(self, file):
        """Initiates new class of word finder, which takes STRING of the path of TXT file"""
        word_file = open(file, "r")
        self.words = self.read_file(word_file)
        print(f"{len(self.words)} words read")
    def read_file(self, word_file):
        """Opens the file, returns a list with each single word in word_file
        """
        return [word.strip() for word in word_file]
    def random(self):
        """get random choice of our words list"""
        return random.choice(self.words)

class SpecialWordFinder(WordFinder):
    def read_file(self, word_file):
        """will check to see if word is a valid word (no blanks or starts with #)"""
        return [word.strip() for word in word_file if word.strip() and not word.startswith("#")]


