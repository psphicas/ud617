#!/usr/bin/python
'''
Post and Answer Length

Process the forum_node data and output the length of the post and the average answer (just answer, not comment) length for each post. 


Mapper input record format:

id	title	tagnames	author_id	body	node_type	parent_id	abs_parent_id	added_at	score	state_string	last_edited_id	last_activity_by_id	last_activity_at	active_revision_id	extra	extra_ref_id	extra_count	marked

Mapper output record format:

question_node_id    node_type   body_length

The question_node_id is the ID of the original question.
For question nodes, this is the id field
For answer nodes, this is the parent_id field.

The body_length is the string length of the body field.
'''

import sys
import csv

def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t', quotechar='"')

    for line in reader:

        # read the node type
        node_type = line[5]

        if node_type == "question":
            # for question nodes, question_node_id is just the id
            question_node_id = line[0]
        elif node_type == "answer":
            # for answer nodes, question_node_id is the parent_id
            question_node_id = line[6]
        else:
            continue

        # find the length of the body
        body_length = len(line[4])

        # print the output record
        print "{0}\t{1}\t{2}".format(question_node_id, node_type, body_length)

if __name__ == "__main__":
    mapper()
