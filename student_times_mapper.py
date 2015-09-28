#!/usr/bin/python
'''
Students and Posting Time on Forums

Find for each student what is the hour during which the student has posted the most posts.

Mapper input record format:

id	title	tagnames	author_id	body	node_type	parent_id	abs_parent_id	added_at	score	state_string	last_edited_id	last_activity_by_id	last_activity_at	active_revision_id	extra	extra_ref_id	extra_count	marked

Mapper output record format:

author_id   hour

The hour is derived from the added_at field.
'''

import sys
import csv

def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t', quotechar='"')

    for line in reader:
        # read the appropriate fields
        author_id, date_added = line[3], line[8]

        try:
            # ensure that the author_id is numeric
            author_id = int(author_id)

            # ensure that the hour is numeric
            # example: 2015-02-21 05:08:03.824261+00
            #                     ^^
            # hour is at string slice [11:13]
            hour = int(date_added[11:13])

            # print the output record
            print "{0}\t{1}".format(author_id, hour)

        except ValueError:
            # skip lines that cause problems
            # (for example, the header row)
            continue

if __name__ == "__main__":
    mapper()
