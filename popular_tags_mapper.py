#!/usr/bin/python
'''
Top Tags

Output Top 10 tags, ordered by the number of questions they appear in.


Mapper input record format:

id	title	tagnames	author_id	body	node_type	parent_id	abs_parent_id	added_at	score	state_string	last_edited_id	last_activity_by_id	last_activity_at	active_revision_id	extra	extra_ref_id	extra_count	marked

Mapper output record format:

tag     1
'''

import sys
import csv

def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t', quotechar='"')

    for line in reader:

        # read the node type
        node_type = line[5]

        # we are only interested in question nodes
        if node_type != "question":
            continue

        # get the tags
        tagnames = line[2]

        # print the output records
        for tag in tagnames.split():
            print "{0}\t1".format(tag)

if __name__ == "__main__":
    mapper()
