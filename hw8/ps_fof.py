# -*- coding: utf-8 -*-
from pyspark import SparkConf, SparkContext
import sys
from itertools import combinations

if(len(sys.argv) != 3):
    print('Usage' + sys.argv[0] + ' <in> <out>')
    sys.exit(1)

# Input file, output file
inputLocation = sys.argv[1]
outputLocation = sys.argv[2]

# Set up spark
conf = SparkConf().setAppName("CountTriangle")
sc = SparkContext(conf=conf)

# Reads in the entire directory.
data = sc.textFile(inputLocation)

'''
Map:
Create function map_combination that gets all combination from mutual list (pick any two)
Key: 3-tuple (triangle) 
Value: 1 (count as once)
Return all the combination
Then Map all the data into key-value pairs, using flatMap

Reduce:
Sum up how many times the combinations appear (sum values by keys), using reduceByKey 
Filter for the ones more than 2 (to form triangle, need at least 2)
'''
# MAP
data = data.map(lambda l: l.split())

def friend_combination(data):
    # create total combination: set combination as key, set value to 1
    comb = []
    N = int(data[0])
    Fn = [int(x) for x in data[1:]] 
    tot_comb = combinations(Fn, 2)
    for t in tot_comb:
        each_comb = [N, t[0], t[1]]
        comb.append((tuple(sorted(each_comb)), 1))
    return comb

map_all = data.flatMap(friend_combination)

# REDUCE: count values by key, filter >= 2
reduce_filter = map_all.reduceByKey(lambda a,b: a+b).filter(lambda a: a[1] >= 2).keys().sortBy(lambda a: a)
# only want keys in the output (key is the combination, value is the count), sort by ascending order

# formatting
triangle = reduce_filter.map(lambda s: str(s[0]) + " " + str(s[1]) + " " + str(s[2]))

# OUTPUT
triangle.saveAsTextFile(outputLocation)
sc.stop()