#!/usr/bin/env python

import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    #print(line)
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    #print(line)
    words = line.split("\n")
    # increase counters
    for word in words:
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # tab-delimited; the trivial word count is 1
        word = word.split(',')
        print '%s\t%s' % (word[4][18:28]+word[0][10:],1)

