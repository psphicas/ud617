#!/usr/bin/python
'''
Students and Posting Time on Forums

Find for each student what is the hour during which the student has posted the most posts.

Reducer input record format

question_node_id    node_type   body_length

Reducer output record format

question_node_id    question_length   average_answer_length
'''

import sys

def reducer():

    last_question = None
    question_length = 0
    answer_count = 0
    answer_length_total = 0

    for line in sys.stdin:
        question_node_id, node_type, body_length = line.strip().split("\t")
        try:
            body_length = int(body_length)
        except ValueError:
            continue

        if last_question and question_node_id != last_question:
            average_answer_length = float(answer_length_total) / answer_count if answer_count else 0
            print "{0}\t{1}\t{2}".format(last_question, question_length, average_answer_length)
            question_length = 0
            answer_count = 0
            answer_length_total = 0

        last_question = question_node_id

        if node_type == "question":
            question_length = body_length
        elif node_type == "answer":
            answer_count += 1
            answer_length_total += body_length

    if last_question != None:
        average_answer_length = float(answer_length_total) / answer_count if answer_count else 0
        print "{0}\t{1}\t{2}".format(last_question, question_length, average_answer_length)

if __name__ == "__main__":
    reducer()
