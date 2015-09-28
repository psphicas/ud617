#!/usr/bin/python
'''
Study Groups

For each forum thread (that is a question node with all it's answers and comments),
give us a list of students that have posted there - either asked the question,
answered a question or added a comment.

Reducer input record format:

question_node_id    author_id

Reducer output record format:

question_node_id    author_id_list
'''

import sys

def reducer():

    last_question = None
    contributers = []

    for line in sys.stdin:
        question_node_id, author_id = line.strip().split("\t")
        author_id = int(author_id)

        if last_question and last_question != question_node_id:
            print "{0}\t{1}".format(last_question, contributers)
            contributers = []
        last_question = question_node_id
        contributers.append(author_id)
        
    if last_question:
        print "{0}\t{1}".format(last_question, contributers)


if __name__ == "__main__":
    reducer()
