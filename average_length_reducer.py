#!/usr/bin/python
'''
Post and Answer Length

Process the forum_node data and output the length of the post and the average answer (just answer, not comment) length for each post. 

Reducer input record format

question_node_id    node_type   body_length

Reducer output record format

question_node_id    question_length   average_answer_length
'''

import sys

def reducer():

    last_question = None
    question_length = None
    answer_count = 0
    answer_length_total = 0

    for line in sys.stdin:
        question_node_id, node_type, body_length = line.strip().split("\t")
        try:
            body_length = int(body_length)
        except ValueError:
            continue

        if last_question and question_node_id != last_question:
            average_answer_length = float(answer_length_total) / answer_count if answer_count else None
            print "{0}\t{1}\t{2}".format(last_question, question_length, average_answer_length)
            question_length = None
            answer_count = 0
            answer_length_total = 0

        last_question = question_node_id

        if node_type == "question":
            question_length = body_length
        elif node_type == "answer":
            answer_count += 1
            answer_length_total += body_length

    if last_question != None:
        average_answer_length = float(answer_length_total) / answer_count if answer_count else None
        print "{0}\t{1}\t{2}".format(last_question, question_length, average_answer_length)

if __name__ == "__main__":
    reducer()
