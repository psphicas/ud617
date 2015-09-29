#!/usr/bin/python
# Here you will be able to combine the values that come from 2 sources
# Value that starts with A will be the user data
# Values that start with B will be forum node data

'''
Mapper input record formats:

user_ptr_id	"A"	reputation	gold	silver	bronze

OR

author_id	"B"	id	title	tagnames	node_type	parent_id	abs_parent_id	added_at	score

Mapper output record format:
id	title	tagnames	author_id	node_type	parent_id	abs_parent_id	added_at	score	reputation	gold	silver	bronze

'''
import sys
import csv
import warnings

def reducer():

    # buffer holds posts ("B" records) if we haven't
    # seen the corresponding author ("A") record yet
    buffer = []

    # prev_author is the author_id of the last record
    prev_author = None

    # author_info holds the "A" record for prev_author
    author_info = None

    reader = csv.reader(sys.stdin, delimiter='\t', quotechar='"')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

    for data in reader:

        # save the author id
        author_id = data[0]

        # if we had an author switch and haven't gotten
        # the author info yet, we are losing data :(
        if prev_author and author_id != prev_author:
            if len(buffer) > 0:
                warnings.warn("discarding posts with missing author info")
            buffer = []
            author_info = None

        # "A" is an author record
        if data[1] == "A":

            # save the author_info
            author_info = data[2:]

            # empty out the buffer
            for d in buffer:
                output = d[2:5] + d[:1] + d[5:] + author_info
                writer.writerow(output)
            buffer = []

        # "B" records represent posts
        elif data[1] == "B":

            # if we have the author info already, print the record
            if author_info:
                output = data[2:5] + data[:1] + data[5:] + author_info
                writer.writerow(output)
            # if not, save the line for later
            else:
                buffer.append(data)

        prev_author = author_id

    # if there are any stragglers, dump a warning
    if prev_author and len(buffer) > 0:
        warnings.warn("discarding posts with missing author info")

if __name__ == "__main__":
    reducer()

