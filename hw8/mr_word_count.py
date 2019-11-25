# -*- coding: utf-8 -*-
"""
Problem 1-1

Write an mrjob job that takes text as input and counts how many times each word occurs in the text.
Your script should strip punctuation like full stops, commas and semicolons, but you may treat hyphens, apostrophes, etc. as you wish. 
Simplest is to treat, e.g., “John’s” as two words, “John” and “s”, but feel free to do more complicated processing if you wish.
Your script should ignore case, so that “Cat” and “cat” are considered the same word.
Your output should be a collection of (word,count) pairs.
Please save your script in a file called mr_word_count.py and include it in your submission.


"""
from mrjob.job import MRJob
import re

WORD_RE = re.compile(r"[\w']+")


class MRWordCount(MRJob):
	
	# Mapper: read each word as key, set value = 1
	def mapper(self, _, line):
		for word in WORD_RE.findall(line):
			yield word.lower(), 1
	
	# reducer: count frequency for each word
	def reducer(self, key, value):
		yield key, sum(value)

if __name__ == '__main__':
    MRWordCount.run()