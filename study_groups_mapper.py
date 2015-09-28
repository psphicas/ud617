#!/usr/bin/python
'''
Study Groups

For each forum thread (that is a question node with all it's answers and comments),
give us a list of students that have posted there - either asked the question,
answered a question or added a comment.

Mapper input record format:

id	title	tagnames	author_id	body	node_type	parent_id	abs_parent_id	added_at	score	state_string	last_edited_id	last_activity_by_id	last_activity_at	active_revision_id	extra	extra_ref_id	extra_count	marked

Mapper output record format:

question_node_id    author_id

The question_node_id is the ID of the original question.
For question nodes, this is the id field
For answer or comment nodes, this is the parent_id field.
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
        elif node_type == "answer" or node_type == "comment":
            # for answer/comment nodes, question_node_id is the parent_id
            question_node_id = line[6]
        else:
            continue

        # find the author id
        author_id = line[3]

        # print the output record
        print "{0}\t{1}".format(question_node_id, author_id)

if __name__ == "__main__":
    mapper()
