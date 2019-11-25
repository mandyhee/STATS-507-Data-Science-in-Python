# -*- coding: utf-8 -*-
"""
Problem 2-1
Write a mrjob program called mr_summary_stats.py that
takes as input a sequence of (label,value) pairs and outputs a collection of (label, number of samples, mean, variance) 4-tuples, 
in which one 4-tuple appears for each class label in the data, and the mean and variance are the sample mean and variance, 
respectively, of all the values for that class label.

Two reduce steps: first compute summation, then statistics
"""

from mrjob.job import MRJob
from mrjob.step import MRStep
from functools import reduce
import sys


class MRSummaryStatistics(MRJob):

    def steps(self):
        return [
            MRStep(mapper = self.mapper_get_label_value,
                   reducer = self.reducer_summation),
            MRStep(reducer = self.reducer_statistic)
        ]

    def mapper_get_label_value(self, _, line):
        each_line = line.split()
        # if elements after split is not equal to 2, exit
        if len(each_line) != 2:
            print(line)
            sys.exit(1)
        label = int(each_line[0])
        values = float(each_line[1])
        yield label, values

    def reducer_summation(self, label, values):
        # input: key = label, value
        # output: key = label, value (3-tuple: number of sample, sum of value, sum of square of value)
        # n = a[0]+1
        # sum = a[1]+b
        # sum of square = a[2]+b
        yield (label, reduce(lambda a, b: (a[0]+1, a[1]+b, a[2]+b**2), values, (0.0,0.0,0.0)))

    def reducer_statistic(self, label, values):
        # input: key = label, value (3-tuple: number of sample, sum of value, sum of square of value)
        # output: 4-tuple(label, n, mean, variance)
        # mean = sum/n
        # variance = sum of square/n - (sum/n)**2
        yield (label, reduce(lambda a,b: (b[0], b[1]/b[0], b[2]/b[0]-(b[1]/b[0])**2), values, (0,0,0)))

if __name__ == '__main__':
    MRSummaryStatistics.run()





