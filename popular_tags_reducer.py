#!/usr/bin/python
'''
Top Tags

Output Top 10 tags, ordered by the number of questions they appear in.

Reducer input record format:

tag     count

Reducer output record format:

tag     count

Note: The expected input from the mapper will have count = 1
'''

import sys
from collections import Counter

def reducer():

    # Use a Counter to keep running track of top tags and their counts.
    # The size of the Counter will be at most n+1 elements,
    # which should be fine from a memory perspective.
    tag_counts = Counter()
    n = 10
    last_tag = None
    total = 0

    for line in sys.stdin:
        tag, count = line.strip().split("\t")

        # if we switched tags, see if we need to shrink the counter
        if last_tag and last_tag != tag and len(tag_counts) > n:
            tag_counts = Counter(dict(tag_counts.most_common(n)))

        last_tag = tag
        count = int(count)
        tag_counts[tag] += count

    # print the output records
    for tag, count in tag_counts.most_common(n):
        print "{0}\t{1}".format(tag, count)

if __name__ == "__main__":
    reducer()
